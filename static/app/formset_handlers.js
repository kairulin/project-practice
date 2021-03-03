window.onload = function () {
    (function ($) {
        console.log('hi')
        $("#customers-group").hide();
        $("#employees-group").hide();

        $('#id_role').on("change", function () {
            const roles = this.value;
            if (roles === "customer") {
                $("#customers-group").show();
            } else {
                $("#customers-group").hide();
            }

            if (roles === "employee" || roles === "manager") {
                $("#employees-group").show();
            } else {
                $("#employees-group").hide();
            }
        })

    })(django.jQuery);
}