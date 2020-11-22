# Bharat Agri code assessment

### setup virtual environment

-  `python3 -m venv <env_name>`
-  `source ./<env_name>/bin/activate`
-  `pip install -r requirements.txt`

### setup redis
- `docker run  -p 6379:6379 --name redis_celery1 -d redis`

### setup rabbitmq

- `brew install rabbitmq`
-  `rabbitmq-server `

### 2. Start a celery worker.
- You'll need a worker to get things done, run the following command in a separate terminal tab:

`celery worker -A celery_worker.celery --loglevel=info --pool=solo`

### 3. Start the app.

Open a new terminal tab and start the app:
`python3 script_run.py`

### 4. Try it!
On your browser, go to: `http://localhost:1947/test.txt/it-works!`
