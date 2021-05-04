from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors  # 避免循环导入
from ..models import Permission


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)


