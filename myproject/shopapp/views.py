from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def index(request):
    logger.info('INDEX page raised')
    html="""
    <h1>My first site</h1>
    <p>---my first site---</p>
    """
    return HttpResponse(html)


def main(request):
    logger.info('MAIN page raised')
    html="""
    <h1>My main page</h1>
    <p><---My main page--></p>
    """
    return HttpResponse(html)


def about(request):
    logger.info('ABOUT page raised')
    html="""
    <h1>Page about me</h1> 
    <p><---Page about me---></p>
    """
    return HttpResponse(html)