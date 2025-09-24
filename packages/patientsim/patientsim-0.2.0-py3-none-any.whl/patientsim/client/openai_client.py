import os
from openai import OpenAI
from dotenv import load_dotenv
from typing import List, Optional

from patientsim.utils import log



class GPTClient:
    def __init__(self, model: str, api_key: Optional[str] = None):
        # Initialize
        self.model = model
        self._init_environment(api_key)
        self.histories = list()
        self.token_usages = dict()
        self.__first_turn = True


    def _init_environment(self, api_key: Optional[str] = None) -> None:
        """
        Initialize OpenAI client.

        Args:
            api_key (Optional[str]): API key for OpenAI. If not provided, it will
                                     be loaded from environment variables.
        """
        if not api_key:
            load_dotenv(override=True)
            api_key = os.environ.get("OPENAI_API_KEY", None)
        self.client = OpenAI(api_key=api_key)

    
    def reset_history(self, verbose: bool = True) -> None:
        """
        Reset the conversation history.

        Args:
            verbose (bool): Whether to print verbose output. Defaults to True.
        """
        self.__first_turn = True
        self.histories = list()
        self.token_usages = dict()
        if verbose:
            log('Conversation history has been reset.', color=True)

    
    def __make_payload(self, user_prompt: str) -> List[dict]:
        """
        Create a payload for API calls to the GPT model.

        Args:
            user_prompt (str): User prompt.

        Returns:
            List[dict]: Payload including prompts and image data.
        """
        payloads = list()
        user_contents = {"role": "user", "content": []}

        # User prompts
        user_contents["content"].append(
            {"type": "text", "text": user_prompt}
        )
    
        payloads.append(user_contents)
        
        return payloads


    def __call__(self,
                 user_prompt: str,
                 system_prompt: Optional[str] = None,
                 using_multi_turn: bool = True,
                 greeting: Optional[str] = None,
                 verbose: bool = True,
                 **kwargs) -> str:
        """
        Sends a chat completion request to the model with optional image input and system prompt.

        Args:
            user_prompt (str): The main user prompt or query to send to the model.
            system_prompt (Optional[str], optional): An optional system-level prompt to set context or behavior. Defaults to None.
            using_multi_turn (bool): Whether to structure it as multi-turn. Defaults to True.
            greeting (Optional[str]): An optional greeting message to include in the conversation. Defaults to None.
            verbose (bool): Whether to print verbose output. Defaults to True.

        Raises:
            e: Any exception raised during the API call is re-raised.

        Returns:
            str: The model's response message.
        """
        try:
            # To ensure empty history
            if not using_multi_turn:
                self.reset_history(verbose)
            
            if self.__first_turn:
                # System prompt
                if system_prompt:
                    self.histories.append({"role": "system", "content": system_prompt})
            
                # Greeting
                if greeting and self.__first_turn:
                    self.histories.append({"role": "assistant", "content": greeting})
                
                self.__first_turn = False
                    
            # User prompt
            self.histories += self.__make_payload(user_prompt)
            
            # Model response
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.histories,
                **kwargs
            )
            assistant_msg = response.choices[0].message
            self.histories.append({"role": assistant_msg.role, "content": assistant_msg.content})

            # Logging token usage
            if response.usage:
                self.token_usages.setdefault("prompt_tokens", []).append(response.usage.prompt_tokens)
                self.token_usages.setdefault("completion_tokens", []).append(response.usage.completion_tokens)
                self.token_usages.setdefault("total_tokens", []).append(response.usage.total_tokens)

            return assistant_msg.content
        
        except Exception as e:
            raise e
