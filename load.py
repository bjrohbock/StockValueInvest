from prefect import flow

@flow
def load():
    print('this is a test')

load()