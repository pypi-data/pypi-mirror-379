"""
Training and evaluation logic for PAPILLON-style privacy pipeline.

See models/privacy/README.md for attribution and citation details.
"""

from functools import lru_cache

import dspy
import mlflow
from datasets import load_dataset

from tagforge.models.privacy import local_lm, openai_lm
from tagforge.models.privacy.model import PrivacyModel


def load_data():
    pupa_new = load_dataset("Columbia-NLP/PUPA", "pupa_new")
    pupa_tnb = load_dataset("Columbia-NLP/PUPA", "pupa_tnb")
    return pupa_new, pupa_tnb


def generate_examples(data):
    examples = [
        dspy.Example(
            {
                "target_response": x["target_response"],
                "user_query": x["user_query"],
                "pii_str": x["pii_units"],
            }
        ).with_inputs("user_query")
        for x in data["train"]
    ]

    return examples


class JudgeQuality(dspy.Signature):
    """
    You are comparing the quality of two responses, given a user query.
    Is response A at least as good as response B?
    """

    user_query = dspy.InputField(desc="The user's request to be fulfilled.")
    response_A = dspy.InputField()
    response_B = dspy.InputField()
    judgement: bool = dspy.OutputField()


class JudgeLeakage(dspy.Signature):
    """
    Count the number of information pieces in `pii` that are simultaneously
    (i) forms of PII and (ii) are leaked into the prompt given.
    Don't count the cases where the leaked information is a celebrity name.
    Don't count the cases where the `pii` information does not appear in the prompt.
    """

    pii = dspy.InputField()
    prompt = dspy.InputField()
    num_pii_leaked: int = dspy.OutputField()


class LLMJudge(dspy.Module):
    def __init__(self):
        self.quality_judge = dspy.ChainOfThought(JudgeQuality)
        self.leakage_judge = dspy.ChainOfThought(JudgeLeakage)

    def forward(
        self, user_query, og_resp, new_resp=None, updated_query=None, pii_str=None
    ):
        judgement_1 = self.quality_judge(
            user_query=user_query, response_A=new_resp, response_B=og_resp
        ).judgement
        judgement_2 = self.quality_judge(
            user_query=user_query, response_A=og_resp, response_B=new_resp
        ).judgement
        judgement = judgement_1 or (judgement_1 == judgement_2)

        pii = list(set(pii_str.split("||")))
        pii_score = self.leakage_judge(pii=pii, prompt=updated_query).num_pii_leaked
        pii_score = pii_score / len(pii) if len(pii) > 0 else 0

        return dspy.Prediction(quality=judgement, leakage=pii_score)


@lru_cache(maxsize=1)
def llm_judge():
    judge = LLMJudge()
    return judge


def compute_metrics(gold, pred, trace=None):
    judge = llm_judge()
    return judge(
        user_query=gold.user_query,
        new_resp=pred.output,
        og_resp=gold.target_response,
        updated_query=pred.prompt,
        pii_str=gold.pii_str,
    )


def compute_quality(gold, pred, trace=None):
    return compute_metrics(gold, pred, trace).quality


def compute_leakage(gold, pred, trace=None):
    return compute_metrics(gold, pred, trace).leakage


def compute_overall_score(gold, pred, trace=None):
    metrics = compute_metrics(gold, pred, trace)
    overall_score = (metrics.quality + (1 - metrics.leakage)) / 2.0
    return overall_score >= 1.0 if trace is not None else overall_score


if __name__ == "__main__":
    dspy.configure(lm=openai_lm, experimental=True)

    mlflow.dspy.autolog(
        log_compiles=True,
        log_evals=True,
        log_traces_from_compile=True,
    )

    mlflow.set_tracking_uri("http://localhost:5000")  # Use local MLflow server
    mlflow.set_experiment("DSPy-Privacy-Optimization")

    pupa_new, pupa_tnb = load_data()
    new_examples = generate_examples(pupa_new)
    tnb_examples = generate_examples(pupa_tnb)

    models = dict(prompt_model=openai_lm, task_model=local_lm)
    optimizer = dspy.SIMBA(metric=compute_overall_score)

    zeroshot = PrivacyModel(untrusted_model=openai_lm)
    kwargs = dict()
    opt_privacy = optimizer.compile(zeroshot, trainset=new_examples, **kwargs)

    kwargs = dict(
        num_threads=16,
        display_progress=True,
        display_table=5,
        max_errors=10,
    )
    evaluate = dspy.Evaluate(
        metric=compute_overall_score, devset=tnb_examples, **kwargs
    )

    evaluate(opt_privacy, metric=compute_quality)
    evaluate(opt_privacy, metric=compute_leakage)

    opt_privacy.save("optimized_privacy.json")
