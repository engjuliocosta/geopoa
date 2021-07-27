# Generated by Django 3.2.4 on 2021-07-16 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geonode_themes', '0011_auto_20200727_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='body_color',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='body_text_color',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='contact_administrative_area',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='contact_city',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='contact_country',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='contact_delivery_point',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='contact_email',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='contact_facsimile',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='contact_name',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='contact_position',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='contact_postal_code',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='contact_street',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='contact_voice',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='contactus',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_accept_close_reload',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_animate_speed_hide',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_animate_speed_show',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_as_popup',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_background',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_bar_enabled',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_bar_head',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_bar_heading_text',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_bar_text',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_border',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_border_on',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_button_1_as_button',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_button_1_button_colour',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_button_1_button_hover',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_button_1_link_colour',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_button_1_new_win',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_button_2_as_button',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_button_2_button_colour',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_button_2_button_hover',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_button_2_hidebar',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_button_2_link_colour',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_button_3_as_button',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_button_3_button_colour',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_button_3_button_hover',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_button_3_link_colour',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_button_3_new_win',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_button_4_as_button',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_button_4_button_colour',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_button_4_button_hover',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_button_4_link_colour',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_cookie_bar_as',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_data_controller',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_data_controller_address',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_data_controller_email',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_data_controller_phone',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_font_family',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_header_fix',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_leave_url',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_logging_on',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_notify_animate_hide',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_notify_animate_show',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_notify_div_id',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_notify_position_horizontal',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_notify_position_vertical',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_popup_overlay',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_popup_showagain_position',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_reject_close_reload',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_scroll_close',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_scroll_close_reload',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_show_once',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_show_once_yn',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_showagain_background',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_showagain_border',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_showagain_div_id',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_showagain_head',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_showagain_tab',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_showagain_x_position',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_text',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='cookie_law_info_widget_position',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='copyright',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='copyright_color',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='footer_bg_color',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='footer_href_color',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='footer_text_color',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='jumbotron_color',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='jumbotron_cta_hide',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='jumbotron_cta_link',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='jumbotron_cta_text',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='jumbotron_text_color',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='jumbotron_title_color',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='navbar_color',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='navbar_dropdown_menu',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='navbar_dropdown_menu_divider',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='navbar_dropdown_menu_hover',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='navbar_dropdown_menu_text',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='navbar_text_color',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='navbar_text_hover',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='navbar_text_hover_focus',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='partners',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='partners_title',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='search_bg_color',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='search_link_color',
        ),
        migrations.RemoveField(
            model_name='geonodethemecustomization',
            name='search_title_color',
        ),
        migrations.AddField(
            model_name='geonodethemecustomization',
            name='variant',
            field=models.CharField(blank=True, default='light', help_text="Name of the theme variant, can be 'ligh', 'dark', or a custom variant name.", max_length=100, null=True),
        ),
    ]