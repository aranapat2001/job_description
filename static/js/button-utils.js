function adjustAllButtons(val) {
    $("#generateJobDescription").prop("disabled", val);
    $("#generateSummaryButton").prop("disabled", val)
    $("#generateQuestionsButton").prop("disabled", val)
}

function enableAllButtons() {
    adjustAllButtons(false);
}

function disableAllButtons() {
    adjustAllButtons(true);
}

function adjustButtonsOnGeneratedContent() {
    enableAllButtons();

    // check for content
    var advertCreated = $('#chat_response').text().trim() !== "";


    // enable or disable the buttons based on generated content
    $("#generateSummaryButton").prop('disabled', !advertCreated);
    $("#generateQuestionsButton").prop('disabled', !advertCreated);
}

$(document).ready(function () {
    adjustButtonsOnGeneratedContent();
});