"""
Privacy-preserving pipeline implementation (PAPILLON-inspired).

See models/privacy/README.md for attribution and citation details.
"""

import os

import dspy
import mlflow

from tagforge.models.privacy import local_lm, openai_lm


class CreateOnePrompt(dspy.Signature):
    """
    You are a helpful assistant that is very mindful of user privacy.
    You have access to a powerful large language model that you can query.
    Given a user request, create a prompt for your large language model that preserves
    user privacy, so that this model can help you complete the user request.
    Provide the prompt directly without any preamble.
    DO NOT COMPLETE THE USER QUERY, ONLY GENERATE A PROMPT.
    """

    user_query = dspy.InputField(desc="The user's request to be fulfilled.")
    curated_prompt = dspy.OutputField()


class InfoAggregator(dspy.Signature):
    """
    You are a helpful assistant.
    For inspiration, we found a potentially related response from a powerful large language model.
    Given the original user query and the remote model’s response, produce a final answer.
    You may re-use non-sensitive details from the original query.
    Do not introduce any extra PII.
    """

    user_query = dspy.InputField(desc="The user's request to be fulfilled.")
    related_llm_response = dspy.InputField(
        desc="information from a powerful LLM responding to a related request"
    )
    response = dspy.OutputField(desc="your final response to the user's request.")


class PrivacyModel(dspy.Module):
    def __init__(self, untrusted_model=None):
        self.prompt_creator = dspy.ChainOfThought(CreateOnePrompt)
        self.info_aggregator = dspy.Predict(InfoAggregator)
        self._set_lm()

        if untrusted_model:
            self.untrusted_model = untrusted_model
        else:
            self.untrusted_model = dspy.settings.lm

    def _set_lm(self):
        self.prompt_creator.set_lm(local_lm)
        self.info_aggregator.set_lm(local_lm)

    def load(self, *args, **kwargs):
        super().load(*args, **kwargs)
        self._set_lm()

    def forward(self, user_query):
        try:
            prompt = self.prompt_creator(user_query=user_query).curated_prompt

            response = self.untrusted_model(prompt)
            if isinstance(response, list):
                response = response[0]
            elif hasattr(response, "completions"):
                response = response.completions[0].text
            else:
                response = str(response)

            output = self.info_aggregator(
                user_query=user_query, related_llm_response=response
            )
        except Exception as e:
            print(f"Error in PrivacyModel: {e}")
            return dspy.Prediction(prompt="", output="", gptResponse="")

        return dspy.Prediction(
            prompt=prompt, output=output.response, gptResponse=response
        )


if __name__ == "__main__":
    dspy.configure(lm=openai_lm, cache=False)

    dspy.configure_cache(
        enable_disk_cache=False,
        enable_memory_cache=False,
    )

    mlflow.dspy.autolog(
        log_compiles=True,
        log_evals=True,
        log_traces_from_compile=True,
    )

    mlflow.set_tracking_uri("http://localhost:5000")  # Use local MLflow server
    # mlflow.set_experiment("DSPy-Privacy")

    pm = PrivacyModel()
    optimized_pm = PrivacyModel()
    weights = os.path.join(os.path.dirname(__file__), "optimized_privacy.json")
    optimized_pm.load(weights)

    prompts = [
        "Hello, my name is John Smith, how many legs does a caterpillar have?",
        "Hello my name is Taj mahal, and I'm from Taj Mahal, where is Taj Mahal Located?",
        str(
            {
                "name": "Matt",
                "occupation": "Software Engineer",
                "skills": ["AWS", "Databricks", "DSPy"],
                "hobbies": ["reading", "Lego"],
            }
        ),
        "test query",
        "I am a software engineer who makes 100k a year, what are my options for roles?",
    ]

    for prompt in prompts:
        print("Initial Prompt:", prompt)
        print("Base:", pm(prompt))
        print("Optimized:", optimized_pm(prompt), "\n")
