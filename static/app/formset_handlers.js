window.onload = function () {
    (function ($) {
        $("#customer-group").hide();
        $("#employee-group").hide();

        $('#id_role').on("change", function () {
            const roles = this.value;
            if (roles === "customer") {
                $("#customer-group").show();
            } else {
                $("#customer-group").hide();
            }

            if (roles === "employee" || roles === "manager") {
                $("#employee-group").show();
            } else {
                $("#employee-group").hide();
            }
        })

    })(django.jQuery);
}