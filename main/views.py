import logging

from json import JSONDecodeError
from flask import Blueprint, render_template, request
from functions import get_posts_by_word

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    search_query = request.args.get('s', '')
    logging.info('Поиск')
    try:
        posts = get_posts_by_word(search_query)
    except FileNotFoundError:
        logging.error('File not found')
        return 'File not found'
    except JSONDecodeError:
        return 'Unable to decode JSON'
    return render_template('post_list.html', query=search_query, posts=posts)
