function Get_All_Countries() {
    JSON_Obj = { "Default": "None" }
    JSON_Obj = JSON.stringify(JSON_Obj)

    $.ajax({
        type: 'POST',
        url: "/Get_All_Countries",
        contentType: "application/json",
        data: JSON_Obj,
        success: function (Results) {

            console.log(Results)

            Countries_Container = $("#Countries_Container");
            Countries_Container.empty();

            for ( Country in Results['Countries'] ){
                console.log( Country )
                console.log( Results['Countries'][Country] )
                Countries_Container.append(Results['Countries'][Country] + "<br>")
            }

        }
    });
}