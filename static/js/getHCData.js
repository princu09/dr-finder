$('.hcSearch').submit(function (e) {
    e.preventDefault();
    $('.hcList').empty();
    $.ajax({
        type: "get",
        url: "",
        data: {
            hcNo: $('#hcNo').val()
        },
        // dataType: "dataType",
        success: function (response) {
            $('.hcList').append(`
<div class="jumbotron mt-5 py-3 px-3">
<h1 class="h4 font-weight-bold mb-3"><i class="fas fa-user-circle text-dark"></i> User Id : <span class="text-success">${response.uID}</span></h1>
<div class="accordion" id="accordionExample">
    <div class="card">
        <div class="card-header" id="headingOne">
            <h2 class="mb-0">
                <button class="btn btn-link btn-block text-left" type="button" data-toggle="collapse"
                    data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                    Health Card Details
                </button>
            </h2>
        </div>
        <div id="collapseOne" class="collapse" aria-labelledby="headingOne" data-parent="#accordionExample">
            <div class="card-body">
                <p class="lead">Name : ${response.fName} ${response.lName}</p>
                <p class="lead">Health Card Number : ${response.hcNo}</p>
            </div>
        </div>
    </div>
    <div class="card">
        <div class="card-header" id="headingTwo">
            <h2 class="mb-0">
                <button class="btn btn-link btn-block text-left collapsed" type="button" data-toggle="collapse"
                    data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                    User Personal Details
                </button>
            </h2>
        </div>
        <div id="collapseTwo" class="collapse show" aria-labelledby="headingTwo" data-parent="#accordionExample">
            <div class="card-body">
                <p class="lead">Name : ${response.fName} ${response.lName}</p>
                <p class="lead">Mobile : ${response.mobile}</p>
                <p class="lead">Email : ${response.email}</p>
                <p class="lead">Date of Birth : ${response.dob}</p>
                <p class="lead">Blood Group : ${response.bloodGroup}</p>
                <p class="lead">Address : ${response.address}</p>
                <p class="lead">City : ${response.city}</p>
                <p class="lead">State : ${response.state}</p>
                <p class="lead">Status : ${response.status}</p>
                <p class="lead">Health Card : ${response.healthCard}</p>
                <p class="lead">Health Card Approve By Admin : ${response.healthCardAcceptByAdmin}</p>
                <p class="lead">Last Login : ${response.last_login}</p>
                <p class="lead">Date Joined : ${response.date_joined}</p>
                <p class="lead">Staff : <span class="text-uppercase">${response.staff}</span></p>
                <p class="lead">Super User : <span class="text-uppercase">${response.superUser}</span></p>
            </div>
        </div>
    </div>
</div>
</div>`);
        }
    });
});