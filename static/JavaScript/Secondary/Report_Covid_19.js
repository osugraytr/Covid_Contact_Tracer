// Hides the first div and shows the second div
function Hide_Show( Div_To_Hide, Div_To_Show ) { // String, String -> None
    //console.log($("#" + Div_To_Hide)[0]);
    //console.log($("#" + Div_To_Show)[0]);

    // Re-Assign to a changable element
    Div_To_Hide = $("#" + Div_To_Hide);
    Div_To_Show = $("#" + Div_To_Show);

    // Hide this Div
    Div_To_Hide.removeClass("g-show");
    Div_To_Hide.addClass("g-hidden");

    // Show this Div
    Div_To_Show.removeClass("g-hidden");
    Div_To_Show.addClass("g-show");
}

// Show a single Div
function Show( Div_To_Show ) {
    Div_To_Show = $("#" + Div_To_Show);
    // Show this Div
    Div_To_Show.removeClass("g-hidden");
    Div_To_Show.addClass("g-show");
}

// Starts the questioneer by showing the Who Page Element
function Questioneer_Handler( To_Step ) {
    

    if( To_Step == 1 ){
        console.log("Hide Welcome_Page and show the Who_Page");
        Hide_Show("Welcome_Page", "Who_Page");
    }
    else if( To_Step == 2 ){
        console.log("Hide Who_Page and show the What_Page");
        Hide_Show("Who_Page", "What_Page");
    }
    else if ( To_Step == 3 ) {
        console.log("Hide What_Page and show the When_Page");
        Hide_Show("What_Page", "When_Page");
    }
}

var Positive_Test = "";
var Positive_Test_Date = "";
var Was_Exposed_Date = "";

function When_Handler( To_Question ) {

    if (To_Question == "Was Exposed") {
        console.log($("#Exposed_Date")[0].value);
        Was_Exposed_Date = $("#Exposed_Date")[0].value;

        Show("Covid_Test_Container");
    }
    else if (To_Question == "Test Positive: Yes") {
        
        $("#Covid_Test_Bool_No")[0].checked = false;

        $("#Covid_Test_Bool_Yes")[0].disabled = true;

        $("#Covid_Test_Bool_No")[0].disabled = false;
        console.log("Positive_Test:\t" + Positive_Test);
        if (Positive_Test == "No") {
            console.log("Yes after NO");
            Hide_Show("Vaxinated_Question_Container", "Positive_Test_Date_Container");
        }
        else {
            console.log("Yes");
            Show("Positive_Test_Date_Container");
        }
        Positive_Test = "Yes";
    }
    else if ( To_Question == "Test Positive: No" ) {

        $("#Covid_Test_Bool_Yes")[0].checked = false;
        $("#Covid_Test_Bool_No")[0].disabled = true;
        $("#Covid_Test_Bool_Yes")[0].disabled = false;

        console.log("Positive_Test:\t" + Positive_Test);
        if (Positive_Test == "Yes") {
            console.log("No after Yes");
            Hide_Show("Positive_Test_Date_Container", "Vaxinated_Question_Container");
            //Show("Vaxinated_Question_Container");
        }
        else {
            console.log("NO");
            Show("Vaxinated_Question_Container");
        }
        Positive_Test = "No";
    }
    else if ( To_Question == "Test Positive Date" ) {
        console.log("No");
        Show("Vaxinated_Question_Container");
    }
    else if ( To_Question == "Vaxinated" ) {
        Show("To_Question_4_Button");
    }
}