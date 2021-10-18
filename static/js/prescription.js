$('#addItem').click(function (e) {
    e.preventDefault();
    tabletName = $('#name').val();
    qty = $('#quantity').val();
    days = $('#days').val();
    mrng = "";
    aftn = "";
    evng = "";
    ngt = "";
    if ($('#mrng').is(':checked')) {
        mrng = $('#mrng').val()
    }
    if ($('#aftn').is(':checked')) {
        aftn = $('#aftn').val()
    }
    if ($('#evng').is(':checked')) {
        evng = $('#evng').val()
    }
    if ($('#ngt').is(':checked')) {
        ngt = $('#ngt').val()
    }

    if ((tabletName == "") || (qty == "") || (days == "")) {

    } else {
        submitPrescriptions = `
            <div class="container d-flex my-2" id="deleteId">
                <div class="col-md-3">
                    <input type="text" value="${tabletName}" id="tName" class="border-0" name="tblName" readonly>
                </div>
                <div class="col-md-2 my-2">
                    <input type="text" value="${qty}" id="tQty" class="border-0" name="tblQty" readonly>
                </div>
                <div class="col-md-2 my-2">
                    <input type="text" value="${days}" id="tDays" class="border-0" name="tblDays" readonly>
                </div>
                <div class="col-md-5 my-2">
                    <input type="text" value="${mrng} ${aftn} ${evng} ${ngt}" id="tTime" class="border-0" name="tblTime" readonly>
                    <button class="btn btn-sm btn-outline-danger" id="deleteData" type="button">
                        <i class="fas fa-trash-alt"></i>
                    </button>
                </div>
            </div>`;

        $('#lastTitle').after(submitPrescriptions);
    }

    $('#deleteData').click(function (e) {
        e.preventDefault();
        $(this).parent().parent('#deleteId').remove();
    });
});

$('#addBillItem').click(function (e) {
    e.preventDefault();
    billName = $('#name').val();
    bill = $('#bill').val();
    if ((billName == "") || (bill == "")) { } else {
        submitPrescriptions = `
            <div class="container d-flex my-2" id="deleteId2">
                <div class="col-md-6">
                    <input type="text" value="${billName}" id="" class="border-0" name="billName" readonly>
                </div>
                <div class="col-md-6">
                <input type="text" value="${bill}" id="" class="border-0" name="bill" readonly>
                </div>
                <button class="btn btn-sm btn-outline-danger" id="deleteData2" type="button"><i class="fas fa-trash-alt"></i></button>
            </div>`;

        $('#lastTitle').after(submitPrescriptions);
    }

    $('#deleteData2').click(function (e) {
        e.preventDefault();
        $(this).parent('#deleteId2').remove();
    });
});