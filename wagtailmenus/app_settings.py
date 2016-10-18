# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

ACTIVE_CLASS = getattr(
    settings, 'WAGTAILMENUS_ACTIVE_CLASS', 'active')

ACTIVE_ANCESTOR_CLASS = getattr(
    settings, 'WAGTAILMENUS_ACTIVE_ANCESTOR_CLASS', 'ancestor')

MAINMENU_MENU_ICON = getattr(
    settings, 'WAGTAILMENUS_MAINMENU_MENU_ICON', 'list-ol')

FLATMENU_MENU_ICON = getattr(
    settings, 'WAGTAILMENUS_FLATMENU_MENU_ICON', 'list-ol')

SECTION_ROOT_DEPTH = getattr(
    settings, 'WAGTAILMENUS_SECTION_ROOT_DEPTH', 3)

DEFAULT_MAIN_MENU_TEMPLATE = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_MAIN_MENU_TEMPLATE',
    'menus/main_menu.html')

DEFAULT_FLAT_MENU_TEMPLATE = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_FLAT_MENU_TEMPLATE',
    'menus/flat_menu.html')

DEFAULT_SECTION_MENU_TEMPLATE = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_SECTION_MENU_TEMPLATE',
    'menus/section_menu.html')

DEFAULT_CHILDREN_MENU_TEMPLATE = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_CHILDREN_MENU_TEMPLATE',
    'menus/children_menu.html')

DEFAULT_SUB_MENU_TEMPLATE = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_SUB_MENU_TEMPLATE',
    'menus/sub_menu.html')

DEFAULT_MAIN_MENU_MAX_LEVELS = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_MAIN_MENU_MAX_LEVELS', 2
)

DEFAULT_SECTION_MENU_MAX_LEVELS = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_SECTION_MENU_MAX_LEVELS', 2
)

DEFAULT_CHILDREN_MENU_MAX_LEVELS = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_CHILDREN_MENU_MAX_LEVELS', 1
)

DEFAULT_FLAT_MENU_MAX_LEVELS = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_FLAT_MENU_MAX_LEVELS', 1
)


FLAT_MENUS_FALL_BACK_TO_DEFAULT_SITE_MENUS = getattr(
    settings, 'WAGTAILMENUS_FLAT_MENUS_FALL_BACK_TO_DEFAULT_SITE_MENUS', False
)

MAX_LEVELS_CHOICES = (
    (1, _('1: No sub-navigation (flat)')),
    (2, _('2: Allow 1 level of sub-navigation')),
    (3, _('3: Allow 2 levels of sub-navigation')),
    (4, _('4: Allow 3 levels of sub-navigation')),
)

USE_SPECIFIC_OFF = 0
USE_SPECIFIC_AUTO = 1
USE_SPECIFIC_TOP_LEVEL = 2
USE_SPECIFIC_ALWAYS = 3
USE_SPECIFIC_CHOICES = (
    (USE_SPECIFIC_OFF, _("OFF (Most efficient)")),
    (USE_SPECIFIC_AUTO, _("AUTO")),
    (USE_SPECIFIC_TOP_LEVEL, _("TOP-LEVEL")),
    (USE_SPECIFIC_ALWAYS, _("ALWAYS (Least efficient)")),
)

USE_SPECIFIC_HELP_TEXT = _(
    "NOTE: Some menu functionality may be dependant on this setting. Please "
    "only change if you know what you're doing.")

DEFAULT_SECTION_MENU_USE_SPECIFIC = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_SECTION_MENU_USE_SPECIFIC',
    USE_SPECIFIC_AUTO
)

DEFAULT_CHILDREN_MENU_USE_SPECIFIC = getattr(
    settings, 'WAGTAILMENUS_DEFAULT_CHILDREN_MENU_USE_SPECIFIC',
    USE_SPECIFIC_AUTO
)
