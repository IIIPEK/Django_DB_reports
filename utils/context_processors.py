"""
Shared context processors and utilities for DJ01 project.
This module contains functions that can be used across multiple apps
to maintain consistency in templates and views.
"""

import datetime
from copy import deepcopy
from django.urls import reverse, NoReverseMatch

# Shared site data
SITE_INFO = {
    'app_name': 'Генератор отчетов',
    'current_year': datetime.datetime.now().year,
}

# Base menu structure
DEFAULT_MENU = [
    {
        'title': 'Отчеты',
        'submenu': [
            {'title': '<i class="bi bi-card-list"></i> Просмотреть', 'url_name': 'main:index', 'login_required': None},
            {'title': '<i class="bi bi-pencil-square"></i> Изменить', 'url_name': 'main:edit', 'login_required': True},
            {'title': '<i class="bi bi-alarm"></i> Рассылки', 'url_name': 'main:alerts', 'login_required': True},
        ],
    },
    {
        'title': '<i class="bi bi-person-fill"></i> Пользователь',
        'submenu': [
            {'title': '<i class="bi bi-person-badge-fill"></i> Профиль', 'url_name': 'users:profile', 'login_required': True},
            {'title': '<i class="bi bi-person-fill-gear"></i> Редактировать профиль', 'url_name': 'users:profile_edit', 'login_required': True},
            {'title': '<i class="bi bi-box-arrow-right"></i> Выход', 'url_name': 'users:logout', 'login_required': True},
            {'title': '<i class="bi bi-person-fill-add"></i> Регистрация', 'url_name': 'users:register', 'login_required': False},
            {'title': '<i class="bi bi-box-arrow-in-right"></i> Вход', 'url_name': 'users:login', 'login_required': False},
        ],
    },
    {'title': 'Контакты', 'url_name': 'contacts:contacts', 'active': False, 'login_required': None},
]

# Footer data
FOOTER_INFO = {
    'description': 'Генератор отчетов и рассылок',
    'links': [
        {'title': 'Политика конфиденциальности', 'url': '/privacy/'},
        {'title': 'Условия использования', 'url': '/terms/'},
        {'title': 'Карта сайта', 'url': '/sitemap/'},
    ],
    'address': 'Arenduse 6, Kohtla-Järve, Estonia',
    'phone': '+372 5124595',
    'email': 'admin@freen.com',
}

def process_menu(items, path):
    for item in items:
        if 'submenu' in item:
            process_menu(item['submenu'], path)
        else:
            try:
                item['url'] = reverse(item['url_name'])
            except NoReverseMatch:
                print(f"Warning: No reverse match for {item['url_name']}")
                item['url'] = '#'

            if item['url'] == '/':
                item['active'] = (path == '/')
            else:
                if path.endswith('/edit/'):
                    item['active'] = (path == item['url'])
                else:
                    item['active'] = path.startswith(item['url'])

def get_base_context(request):
    """
    Creates a base context with common data for all pages.
    Sets the active menu item.

    Args:
        request (request): Request object

    Returns:
        dict: Context dictionary with common data
    """
    # Copy menu items to avoid modifying the original
    menu_items = deepcopy(DEFAULT_MENU)

    process_menu(menu_items, request.path)


    # Create base context
    context = {
        **SITE_INFO,
        'menu_items': menu_items,
        'footer': FOOTER_INFO,
        'is_authenticated': request.user.is_authenticated,
    }

    return context
