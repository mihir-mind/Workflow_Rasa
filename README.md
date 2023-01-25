1. rains a model using your NLU data and stories, saves trained model in ./models.
    ```
    rasa train
    ```

2. Run Rasa model:
    ```
    rasa run  -m models --endpoints endpoints.yml
    ```

3. Debug Rasa model:
    ```
    rasa run --debug
    ```

4. Loads your trained model and lets you talk to your assistant on the command line.
    ```
    rasa shell
    ```

5. Rasa run actions
    ```
    rasa run actions
    ```