// Show information panel
function showInstructions() {
    if ($('#instructions').is(":visible")) {
        $('#instructions').hide()
    } else {
        $('#instructions').show()
    };
}

// Character count functionality
function characterCount() {
    var charCount = this.value.length;
    document.getElementById('charCount').textContent = `${charCount}/40`;
}
document.getElementById('profession').addEventListener('input', characterCount);

// Character count functionality
function freqEur() {
    var frequency = this.value;
    document.getElementById('freq-eur').textContent = `€/${frequency}`;
}
document.getElementById('freq-pay').addEventListener('change', freqEur);

// Initialize values on page load
function characterCountProfession() {
    // Initialize profession character count
    var professionInput = document.getElementById('profession');
    var charCount = professionInput.value.length;
    document.getElementById('charCount').textContent = `${charCount}/40`;

    // Initialize frequency display
    var freqPayInput = document.getElementById('freq-pay');
    var frequency = freqPayInput.value;
    document.getElementById('freq-eur').textContent = `€/${frequency}`;
}
document.addEventListener('DOMContentLoaded', characterCountProfession);

// Numeric input validation functionality
var numericInputEmployees = document.getElementById('num-employees');
var numericInputMinPay = document.getElementById('min-pay');
var numericInputMaxPay = document.getElementById('max-pay');
var numericInputBonus = document.getElementById('bonus');

function validateNumericInput() {
    var value1 = numericInputEmployees.value;
    var value2 = numericInputMinPay.value;
    var value3 = numericInputMaxPay.value;
    var value4 = numericInputBonus.value;

    // Employees
    if (/^\d+$/.test(value1) || (value1 === "")) {
        numericInputEmployees.classList.remove('invalid-input');
        
    } else {
        numericInputEmployees.classList.add('invalid-input'); 
    };

    // Minimum Pay
    if (/^\d+$/.test(value2) || (value2 === "")) {
        numericInputMinPay.classList.remove('invalid-input');
        
    } else {
        numericInputMinPay.classList.add('invalid-input'); 
    };

    // Maximum Pay
    if (/^\d+$/.test(value3) || (value3 === "")) {
        numericInputMaxPay.classList.remove('invalid-input');
        
    } else {
        numericInputMaxPay.classList.add('invalid-input'); 
    };

    // Bonus Pay
    if (/^\d+$/.test(value4) || (value4 === "")) {
        numericInputBonus.classList.remove('invalid-input');
        
    } else {
        numericInputBonus.classList.add('invalid-input'); 
    }
}

numericInputEmployees.addEventListener('input', validateNumericInput);
numericInputMinPay.addEventListener('input', validateNumericInput);
numericInputMaxPay.addEventListener('input', validateNumericInput);
numericInputBonus.addEventListener('input', validateNumericInput);

// Initial validation on page load
window.addEventListener('load', validateNumericInput);

// Function to validate URL
function validateURL() {
    var urlInput = document.getElementById('client-url');
    var url = urlInput.value;
    var pattern = new RegExp('^(https?:\\/\\/)?'+ // protocol
        '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // domain name
        '((\\d{1,3}\\.){3}\\d{1,3}))'+ // OR ip (v4) address
        '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // port and path
        '(\\?[;&a-z\\d%_.~+=-]*)?'+ // query string
        '(\\#[-a-z\\d_]*)?$','i'); // fragment locator
    if(!pattern.test(url)) {
        urlInput.classList.add('invalid-input');
    } else {
        urlInput.classList.remove('invalid-input');
    }
}


// Add event listeners
var urlInput = document.getElementById('client-url');
urlInput.addEventListener('input', validateURL);

// Function to toggle date input visibility
function toggleDateInput() {
    var jobType = document.getElementById('contract-type').value;
    var startDateInputContainer = document.getElementById('startDateInputContainer');
    var endDateInputContainer = document.getElementById('endDateInputContainer');
    if (jobType === 'temporal') {
        startDateInputContainer.classList.remove('hidden');
        endDateInputContainer.classList.remove('hidden');
    } else {
        startDateInputContainer.classList.add('hidden');
        endDateInputContainer.classList.add('hidden');
    }
}

// Function to toggle vehicle checkbox visibility
function toggleVehicleCheckbox() {
    var drivingLicense = document.getElementById('driving-license').value;
    var VehicleCheckboxContainer = document.getElementById('VehicleCheckboxContainer');
    if (drivingLicense.trim() !== '') {
        VehicleCheckboxContainer.classList.remove('hidden');
        VehicleCheckboxContainer.disabled = false;
    } else {
        VehicleCheckboxContainer.classList.add('hidden');
        VehicleCheckboxContainer.disabled = true;
    }
}

// Function to toggle emoji checkbox visibility
function toggleEmojisCheckbox() {
    var templateName = document.getElementById('template-name').value;
    var EmojisCheckboxContainer = document.getElementById('EmojisCheckboxContainer');
    var emojisCheckbox = document.getElementById('emojis');
    if (templateName === 'multiposting') {
        EmojisCheckboxContainer.classList.add('hidden');
        emojisCheckbox.disabled = true;
    } else {
        EmojisCheckboxContainer.classList.remove('hidden');
        emojisCheckbox.disabled = false;
    }
}

function toggleRetribucion() {
    var freqPay = document.getElementById('freq-pay').value
    var retribucionContainer = document.getElementById('retribucion');
    if (freqPay.trim() !== '') {
        retribucionContainer.classList.remove('hidden');
    } else {
        retribucionContainer.classList.add('hidden');
    }
}

// Function to toggle bonus input visibility
function toggleBonusInput() {
    var jobType = document.getElementById('contract-type').value;
    var bonusInputContainer = document.getElementById('bonus');
    var bonusLabel1InputContainer = document.getElementById('label-bonus-1');
    var bonusLabel2InputContainer = document.getElementById('label-bonus-2');
    if (jobType === 'indefinido') {
        bonusInputContainer.classList.remove('hidden');
        bonusLabel1InputContainer.classList.remove('hidden');
        bonusLabel2InputContainer.classList.remove('hidden');
        bonusInputContainer.disabled = false;
    } else {
        bonusInputContainer.classList.add('hidden');
        bonusLabel1InputContainer.classList.add('hidden');
        bonusLabel2InputContainer.classList.add('hidden');
        bonusInputContainer.disabled = true;
    }
}

// Hit enter adds a new line in textarea inputs
document.querySelectorAll('textarea').forEach(function(textarea) {
    textarea.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            // Insert a new line
            event.preventDefault();
            const start = this.selectionStart;
            const end = this.selectionEnd;
            this.value = this.value.substring(0, start) + '\n' + this.value.substring(end);
            this.selectionStart = this.selectionEnd = start + 1;
        }
    });
});

// Copy Job Advert
function copyToClipboard(elementId, copy_type) {
    // Get the element by its ID
    var copyElement = document.getElementById(elementId);

    var contentToCopy;

    // If it's an input or textarea element, select its content
    if (copyElement.tagName === "INPUT" || copyElement.tagName === "TEXTAREA") {
        copyElement.select();
        copyElement.setSelectionRange(0, 99999); // For mobile devices
        contentToCopy = copyElement.value;

    } else {
        // Handle other elements, depending on the type of content to copy
        if (copy_type === "rich") {
            contentToCopy = copyElement.innerHTML; // Copy rich (HTML) content
        } else {
            contentToCopy = copyElement.innerText; // Copy plain text content
        }
    }

    // Use the Clipboard API to copy the content to the clipboard
    navigator.clipboard.writeText(contentToCopy).then(function() {
        alert('Texto copiado al portapapeles');
    }).catch(function(error) {
        console.error('Could not copy text: ', error);
    });
}


function copyRichJobDescription() {
    copyToClipboard("chat_response", "rich");
}

function copyPlainJobDescription() {
    copyToClipboard("chat_response", "plain");
}

function copyPlainSummary() {
    copyToClipboard("summary_display", "plain");
}

function copyPlainQuestions() {
    copyToClipboard("questions_display", "plain");
}

// Add event listener for dropdown change
var templateName = document.getElementById('template-name');
templateName.addEventListener('change', toggleEmojisCheckbox);

// Add event listener for dropdown change
var freqPay = document.getElementById('freq-pay')
freqPay.addEventListener('change', toggleRetribucion);

// Add event listener for dropdown change
var jobType = document.getElementById('contract-type');
jobType.addEventListener('change', toggleDateInput);

// Add event listener for dropdown change
var drivingLicense = document.getElementById('driving-license');
drivingLicense.addEventListener('change', toggleVehicleCheckbox);

// Add event listener for dropdown change
var jobType2 = document.getElementById('contract-type');
jobType2.addEventListener('change', toggleBonusInput);

// Initial check to set date input and vehicle, emojis checkboxs visibility on page load
window.addEventListener('load', toggleDateInput);
window.addEventListener('load', toggleVehicleCheckbox);
window.addEventListener('load', toggleBonusInput);
window.addEventListener('load', toggleEmojisCheckbox);
window.addEventListener('load', toggleRetribucion);

document.addEventListener('DOMContentLoaded', () => {
    const inputContainer = document.getElementById('input-container');
    const benefitInput = document.getElementById('benefit-input');
    const benefitBoxes = document.querySelectorAll('.benefit-box');
    const selectedBenefits = document.getElementById('selected-benefits');
    const benefitsStorage = document.getElementById('benefits-storage');

    // Initialize the benefit list as a Set to ensure uniqueness
    let benefitSet = new Set(benefitsStorage.value 
        ? benefitsStorage.value.split(',').map(benefit => benefit.trim()).filter(benefit => benefit !== '') 
        : []);

    inputContainer.addEventListener('click', () => {
        inputContainer.classList.add('expanded');
    });

    benefitInput.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            event.preventDefault();
            const benefit = benefitInput.value.trim();
            if (benefit && !isBenefitSelected(benefit)) {
                addBenefit(benefit);
                benefitInput.value = '';
            }
        }
    });

    benefitBoxes.forEach(box => {
        box.addEventListener('click', () => {
            const benefit = box.getAttribute('data-benefit');
            if (!isBenefitSelected(benefit)) {
                addBenefit(benefit);
            }
        });
    });

    function addBenefit(benefit) {
        if (benefit && !benefitSet.has(benefit)) {
            benefitSet.add(benefit);
            updateBenefitsStorage();
            renderBenefit(benefit);
        }
    }

    function isBenefitSelected(benefit) {
        return benefitSet.has(benefit);
    }

    function renderBenefit(benefit) {
        // Check if benefit is already rendered
        if (selectedBenefits.querySelector(`[data-benefit="${benefit}"]`)) {
            return;
        }

        const benefitElement = document.createElement('div');
        benefitElement.classList.add('green-box');
        benefitElement.setAttribute('data-benefit', benefit);
        benefitElement.textContent = benefit;

        const closeBtn = document.createElement('span');
        closeBtn.className = 'close-btn';
        closeBtn.textContent = 'X';
        // Attach the removeBenefit function to the onclick attribute
        closeBtn.setAttribute('onclick', `removeBenefit(this.parentElement, '${benefit}')`);

        benefitElement.appendChild(closeBtn);
        selectedBenefits.appendChild(benefitElement);
    }

    function updateBenefitsStorage() {
        benefitsStorage.value = Array.from(benefitSet).join(', ');
    }

    // Render benefits from the hidden input field on page load
    benefitSet.forEach(benefit => {
        renderBenefit(benefit);
    });

    // Make removeBenefit globally accessible
    window.removeBenefit = function(benefitElement, benefit) {
        // Remove the benefit element from the DOM
        selectedBenefits.removeChild(benefitElement);

        // Update the benefitSet by removing the benefit
        benefitSet.delete(benefit);

        // Update the hidden input field
        updateBenefitsStorage();
    };
});


// Prevent submitting the form by hitting enter
$(document).on("keydown", "form", function(event) { 
    return event.key != "Enter";
});

////////////////////////////////////////////////////////////////////////////////

//////////////////////// Job Advert Versioning ////////////////////////
// Static Logic
//     1. flicking between version buttons assigned new content to container

// Dynamic Logic:
//     1. when page session is created
//         -> initialise local storage

//     2. when first job advert is created
//         -> show job ad version container
//         -> show latest version button
//         -> assign latest version button with text for latest output

//     3. when all subsequent job adverts are created
//         -> show version-x button
//         -> assign version-x button with text from latest-version
//         -> assign latest version button with text for latest output

//
let selectedButton = null;
let numVersion = 6;
dummy_summaries_dict = {};
dummy_questions_dict = {};

sessionStorage.setItem('numButton', 1);
sessionStorage.setItem('summaries', dummy_summaries_dict);
sessionStorage.setItem('questions_list', dummy_questions_dict);

function changeVersion(button) {
    var id = button.id;
    var numButton = parseInt(id.slice(-1));

    sessionStorage.setItem('numButton', numButton);

    var job_ad_html = sessionStorage.getItem(id);
    var job_ad_summary_html = sessionStorage.getItem(id + '-summary');
    var job_ad_questions_html = sessionStorage.getItem(id + '-questions');


    document.getElementById("chat_response").innerHTML = job_ad_html;
    document.getElementById("summary_display").innerHTML = job_ad_summary_html;
    document.getElementById("questions_display").innerHTML = job_ad_questions_html;


    // Update parametres
    var business_unit = sessionStorage.getItem(id + '-business_unit');
    document.getElementById("business-unit").value = business_unit;

    var template_name = sessionStorage.getItem(id + '-template_name');
    document.getElementById("template-name").value = template_name;

    var template_structure = sessionStorage.getItem(id + '-template_structure');
    document.getElementById("template-structure").setAttribute("value", template_structure);

    var emojis = sessionStorage.getItem(id + '-emojis');
    document.getElementById("emojis").setAttribute("value", emojis);

    var tone = sessionStorage.getItem(id + '-tone');
    document.getElementById("tone").value = tone;

    var language = sessionStorage.getItem(id + '-language');
    document.getElementById("language").value = language;

    var client_sector = sessionStorage.getItem(id + '-client_sector');
    document.getElementById("client-sector").setAttribute("value", client_sector);

    var client_url = sessionStorage.getItem(id + '-client_url');
    document.getElementById("client-url").setAttribute("value", client_url);

    var profession = sessionStorage.getItem(id + '-profession');
    document.getElementById("profession").setAttribute("value", profession);

    var city = sessionStorage.getItem(id + '-city');
    document.getElementById("city").setAttribute("value", city);

    var province = sessionStorage.getItem(id + '-province');
    document.getElementById("province").setAttribute("value", province);

    var min_pay = sessionStorage.getItem(id + '-min_pay');
    document.getElementById("min-pay").setAttribute("value", min_pay);

    var max_pay = sessionStorage.getItem(id + '-max_pay');
    document.getElementById("max-pay").setAttribute("value", max_pay);

    var freq_pay = sessionStorage.getItem(id + '-freq_pay');
    document.getElementById("freq-pay").value = freq_pay;

    var bonus = sessionStorage.getItem(id + '-bonus');
    document.getElementById("bonus").setAttribute("value", bonus);

    var benefits_storage = sessionStorage.getItem(id + '-benefits_storage');
    document.getElementById("benefits-storage").value = benefits_storage;

    var contract_type = sessionStorage.getItem(id + '-contract_type');
    document.getElementById("contract-type").value = contract_type;

    var work_rate = sessionStorage.getItem(id + '-work_rate');
    document.getElementById("work-rate").value =  work_rate;

    var num_employees = sessionStorage.getItem(id + '-num_employees');
    document.getElementById("num-employees").setAttribute("value", num_employees);

    var start_date = sessionStorage.getItem(id + '-start_date');
    document.getElementById("start-date").setAttribute("value", start_date);

    var end_date = sessionStorage.getItem(id + '-end_date');
    document.getElementById("end-date").setAttribute("value", end_date);

    var schedule = sessionStorage.getItem(id + '-schedule');
    document.getElementById("schedule").value = schedule;

    var skills = sessionStorage.getItem(id + '-skills');
    document.getElementById("skills").value = skills;

    var driving_license = sessionStorage.getItem(id + '-driving_license');
    document.getElementById("driving-license").setAttribute("value", driving_license);

    var vehicle = sessionStorage.getItem(id + '-vehicle');
    document.getElementById("vehicle").setAttribute("value", vehicle);

    var work_type = sessionStorage.getItem(id + '-work_type');
    document.getElementById("work-type").value = work_type;

    document.getElementById("questions_topic").value = '';
    // var questions_topic = sessionStorage.getItem(id + '-questions_topic');
    // document.getElementById("questions_topic").setAttribute("value", questions_topic);

    toggleDateInput();
    toggleVehicleCheckbox();
    toggleEmojisCheckbox();
    toggleRetribucion();
    toggleBonusInput();
    characterCountProfession();
    validateNumericInput();

    if ((job_ad_summary_html) && (job_ad_summary_html.trim() != '')) {
        document.getElementById("summary_display").removeAttribute("hidden");
    } else {
        document.getElementById("summary_display").setAttribute("hidden", true);
    };

    if ((job_ad_questions_html) && (job_ad_questions_html.trim() != '')) {
        document.getElementById("questions_display").removeAttribute("hidden");
    } else {
        document.getElementById("questions_display").setAttribute("hidden", true);
    };
    
    if (selectedButton && selectedButton !== button) {
        selectedButton.classList.remove('btn-clicked');
        selectedButton.classList.add('btn-primary'); 
    }

    // Toggle the 'btn-clicked' class on the clicked button
    button.classList.remove('btn-primary'); 
    button.classList.add('btn-clicked');

    for(var i = 1; i <= numVersion; i++){
        var otherButton = document.getElementById("version-" + i);
        if(i !== numButton){
            otherButton.classList.remove('btn-clicked'); 
            otherButton.classList.add('btn-primary');
        }
    }

    selectedButton = button;
}

document.addEventListener('DOMContentLoaded', () => {
    // 1. get version number
    var version_count = sessionStorage.getItem('versionCounter');
    if (version_count == null) {
        version_count = 0;
    } else {
        version_count = parseInt(version_count) || 0;
    }

    // 2. get job ad html
    job_ad = document.getElementById("chat_response").innerHTML;

    // 3. if job ad_html is not empty
    if (job_ad.trim().length > 0) {

        // increment version number
        version_count += 1;
        sessionStorage.setItem('versionCounter', version_count);
        sessionStorage.setItem('numButton', version_count);

        // show container
        document.getElementById('version-container').removeAttribute("hidden");

        // show all buttons
        for(var i = 1; i <= (version_count); i++){
            document.getElementById('version-' + i + '-container').removeAttribute("hidden");
            var otherButton = document.getElementById('version-' + i);
            if (i !== version_count) {
            otherButton.classList.remove('btn-clicked');
            otherButton.classList.add('btn-primary');
            }
        }

        // store job add data to button
        sessionStorage.setItem('version-' + version_count, job_ad);

        // store all parametres used
        business_unit = document.getElementById("business-unit").value;
        if (business_unit != null) {sessionStorage.setItem('version-' + version_count + '-business_unit', business_unit);
            console.log(business_unit);
        };

        template_name = document.getElementById("template-name").value;
        if (template_name != null) {sessionStorage.setItem('version-' + version_count + '-template_name', template_name)};

        template_structure = document.getElementById("template-structure").value;
        if (template_structure != null) {sessionStorage.setItem('version-' + version_count + '-template_structure', template_structure)};

        emojis = document.getElementById("emojis").value;
        if (emojis != null) {sessionStorage.setItem('version-' + version_count + '-emojis', emojis)};

        tone = document.getElementById("tone").value;
        if (tone != null) {sessionStorage.setItem('version-' + version_count + '-tone', tone)};

        language = document.getElementById("language").value;
        if (language != null) {sessionStorage.setItem('version-' + version_count + '-language', language)};

        client_sector = document.getElementById("client-sector").value;
        if (client_sector != null) {sessionStorage.setItem('version-' + version_count + '-client_sector', client_sector)};

        client_url = document.getElementById("client-url").value;
        if (client_url != null) {sessionStorage.setItem('version-' + version_count + '-client_url', client_url)};

        profession = document.getElementById("profession").value;
        if (profession != null) {sessionStorage.setItem('version-' + version_count + '-profession', profession);
            console.log(profession);
        };

        city = document.getElementById("city").value;
        if (city != null) {sessionStorage.setItem('version-' + version_count + '-city', city)};

        province = document.getElementById("province").value;
        if (province != null) {sessionStorage.setItem('version-' + version_count + '-province', province)};

        min_pay = document.getElementById("min-pay").value;
        if (min_pay != null) {sessionStorage.setItem('version-' + version_count + '-min_pay', min_pay)};

        max_pay = document.getElementById("max-pay").value;
        if (max_pay != null) {sessionStorage.setItem('version-' + version_count + '-max_pay', max_pay)};

        freq_pay = document.getElementById("freq-pay").value;
        if (freq_pay != null) {sessionStorage.setItem('version-' + version_count + '-freq_pay', freq_pay)};

        bonus = document.getElementById("bonus").value;
        if (bonus != null) {sessionStorage.setItem('version-' + version_count + '-bonus', bonus)};

        benefits_storage = document.getElementById("benefits-storage").value;
        if (benefits_storage != null) {sessionStorage.setItem('version-' + version_count + '-benefits_storage', benefits_storage)};

        contract_type = document.getElementById("contract-type").value;
        if (contract_type != null) {sessionStorage.setItem('version-' + version_count + '-contract_type', contract_type)};

        work_rate = document.getElementById("work-rate").value;
        if (work_rate != null) {sessionStorage.setItem('version-' + version_count + '-work_rate', work_rate)};

        num_employees = document.getElementById("num-employees").value;
        if (num_employees != null) {sessionStorage.setItem('version-' + version_count + '-num_employees', num_employees);
            console.log(num_employees);
        };

        start_date = document.getElementById("start-date").value;
        if (start_date != null) {sessionStorage.setItem('version-' + version_count + '-start_date', start_date)};

        end_date = document.getElementById("end-date").value;
        if (end_date != null) {sessionStorage.setItem('version-' + version_count + '-end_date', end_date)};

        schedule = document.getElementById("schedule").value;
        if (schedule != null) {sessionStorage.setItem('version-' + version_count + '-schedule', schedule)};

        skills = document.getElementById("skills").value;
        if (skills != null) {sessionStorage.setItem('version-' + version_count + '-skills', skills)};

        driving_license = document.getElementById("driving-license").value;
        if (driving_license != null) {sessionStorage.setItem('version-' + version_count + '-driving_license', driving_license)};

        vehicle = document.getElementById("vehicle").value;
        if (vehicle != null) {sessionStorage.setItem('version-' + version_count + '-vehicle', vehicle)};

        work_type = document.getElementById("work-type").value;
        if (work_type != null) {sessionStorage.setItem('version-' + version_count + '-work_type', work_type)};

        // questions_topic = document.getElementById("questions_topic").value;
        // if (questions_topic != null) {sessionStorage.setItem('version-' + version_count + '-questions_topic', questions_topic)};

    } else {
        // reset version counter if cleared
        version_count = 0;
        sessionStorage.setItem('versionCounter', version_count);
    };

    toggleDateInput();
    toggleVehicleCheckbox();
    toggleEmojisCheckbox();
    toggleRetribucion();
    toggleBonusInput();
    validateNumericInput();
});
////////////////////// Job Advert Versioning END ////////////////////////


// 
async function generateSummary() {
    const chatResponse = document.getElementById('chat_response').innerHTML;

    if (!chatResponse.trim()) {
        alert("Please enter some text.");
        return;
    }

    // Call backend API to generate summary
    const summary = await getSummaryFromAPI(chatResponse);

    // Version number
    const version_number = sessionStorage.getItem('numButton');

    // Display the summary
    displaySummary(summary);

    job_ad_summary = document.getElementById("summary_display").innerHTML;

    if (job_ad_summary.trim().length > 0) {
        // show container
        document.getElementById('summary_display').removeAttribute("hidden");
        document.getElementById('copyButtonsContainer').classList.remove('hidden');
        // store job add data to button
        sessionStorage.setItem('version-' + version_number + '-summary', job_ad_summary);

    };
}

async function getSummaryFromAPI(chatResponse) {
    const response = await fetch('/generate_summary', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ chat_response: chatResponse })
    });

    if (!response.ok) {
        const errorData = await response.json();
        alert(`Error: ${errorData.error}`);
        return '';
    }

    const data = await response.json();
    return data.summary;
}

function displaySummary(summary) {
    const summariesDiv = document.getElementById('summary_display');
    if (summary.trim() != '') {
        summariesDiv.removeAttribute('hidden');
        summariesDiv.innerHTML = summary;
    }
}

async function generateQuestions() {
    const chatResponse = document.getElementById('chat_response').innerHTML;
    const questionsTopic = document.getElementById('questions_topic').value

    if (!chatResponse.trim()) {
        alert("Please enter some text.");
        return;
    }

    // Get the selected radio button value
    const selectedOption = document.querySelector('input[name="inlineRadioOptions2"]:checked').value;

    // Call backend API to generate questions
    let questions = await getQuestionsFromAPI(chatResponse, selectedOption, questionsTopic);

    // Number of version
    const version_number = sessionStorage.getItem('numButton');

    // Display the questions
    displayQuestions(questions);

    job_ad_questions = document.getElementById("questions_display").innerHTML;

    if (job_ad_questions.trim().length > 0) {
        // show container
        document.getElementById('questions_display').removeAttribute("hidden");
        document.getElementById('copyButtonsContainer').classList.remove('hidden');
        // store job ad data to button
        sessionStorage.setItem('version-' + version_number + '-questions', job_ad_questions);
    }
}

async function getQuestionsFromAPI(chatResponse, selectedOption, questionsTopic) {
    const response = await fetch('/generate_questions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
            chat_response: chatResponse, 
            inlineRadioOptions2: selectedOption,  // Include the selected radio button value
            questions_topic: questionsTopic
        })
    });

    if (!response.ok) {
        const errorData = await response.json();
        alert(`Error: ${errorData.error}`);
        return '';
    }

    const data = await response.json();
    return data.questions;
}

function displayQuestions(questions) {
    const questionsDiv = document.getElementById('questions_display');
    questionsDiv.innerHTML = ''; // Clear previous content
    if (questions.trim() != '') {
        questionsDiv.removeAttribute('hidden');
        const questionsParagraph = document.createElement('p');
        questionsParagraph.innerHTML = questions; // Use innerHTML to set HTML content
        questionsDiv.appendChild(questionsParagraph);
    }
}


