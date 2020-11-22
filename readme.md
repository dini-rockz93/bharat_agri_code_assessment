# Bharat Agri code assessment

### 1. setup virtual environment

-  `python3 -m venv <env_name>`
-  `source ./<env_name>/bin/activate`
-  `pip install -r requirements.txt`

### 2. setup redis
- `docker run  -p 6379:6379 --name redis_celery1 -d redis`

### 3. setup rabbitmq

- `brew install rabbitmq`
-  `rabbitmq-server `

### 4 start a celery worker.
- You'll need a worker to get things done, run the following command in a separate terminal tab:

`celery worker -A celery_worker.celery --loglevel=info --pool=solo`

### 5. start the app.

Open a new terminal tab and start the app:
`python3 script_run.py`

### 6. run it!
On your browser, go to: `http://localhost:1947/test.txt/it-works!`
