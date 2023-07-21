from celery import shared_task


@shared_task(bind=True)
def generate_file(*args,**kwargs):
    print("Soy yo de nuevo")