from fastapi import Body, Form, File, Request
from fastapi.datastructures import UploadFile
from settings import ENV_TEMPLATES, APP
from fastapi.responses import Response
from services import count_pixels_from_image
from loguru import logger


logger.add('logs/request_response_logs.json', level='INFO', 
    format='{time} {level} {message}', rotation='10 MB', 
    compression='zip', serialize=True)


@APP.get('/')
def index_page():
    """Main page with form for image download."""
    template = ENV_TEMPLATES.get_template('index.html')
    return Response(template.render(), media_type='text/html')


@APP.post('/')
def get_image_from_main_page(request: Request, image: UploadFile = File(...)):
    """Receives a image from form. Send it to pixel counting. 
    Return result of counting in template."""
    logger.info(request.scope)

    template = ENV_TEMPLATES.get_template('index.html')
    try:
        result_of_counting = count_pixels_from_image(image.file)
    except Exception:
        logger.exception('Caught something critical.')
        result_of_counting = 'Unsupported type of image. Load another image(png or jpg).'

    response = Response(template.render(result=result_of_counting), 
        media_type='text/html')
    logger.info(result_of_counting, response.status_code, response.headers)
    
    return response