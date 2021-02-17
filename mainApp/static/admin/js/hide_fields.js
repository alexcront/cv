hide_page=false;
django.jQuery(document).ready(function(){
    if (django.jQuery('#id_is_current_job').is(':checked')) {
        django.jQuery(".field-year_end").hide();
        django.jQuery(".field-month_end").hide();
        hide_page=true;
    } else {
        django.jQuery(".field-year_end").show();
        django.jQuery(".field-month_end").show();
        hide_page=false;
    }
    django.jQuery("#id_is_current_job").click(function(){
        hide_page=!hide_page;
        if (hide_page) {
            django.jQuery(".field-year_end").hide();
            django.jQuery(".field-month_end").hide();
        } else {
            django.jQuery(".field-year_end").show();
            django.jQuery(".field-month_end").show();
        }
    })
})