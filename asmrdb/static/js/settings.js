let css_btn = document.getElementById("css_check");
let css_input = document.getElementById("custom_css");
let theme_input = document.getElementById("custom_theme");

css_btn.addEventListener('click', () => {
    if (css_btn.checked == true)
    {
        theme_input.disabled = true;
        theme_input.required = false;

        css_input.disabled = false;
        css_input.required = true;
    } else {
        theme_input.disabled = false;
        theme_input.required = true;

        css_input.disabled = true;
        css_input.required = false;
    }
});
