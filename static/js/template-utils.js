// function to display and persist template inputs and template input options
document.addEventListener('DOMContentLoaded', function() {
    var selectElement = document.getElementById('template-name');
    var textareaElement = document.getElementById('template-structure');

    // Array of valid option values
    var validOptions = ['email_short', 'email_long', 'multiposting', 
                        'linkedin_short', 'linkedin_long', 'personalizado'];

    selectElement.addEventListener('change', function() {
        // Check if the selected value is included in the validOptions array
        if (validOptions.includes(selectElement.value)) {
            textareaElement.value = selectElement.options[selectElement.selectedIndex].getAttribute('data-values');
            textareaElement.style.display = 'block'; // Show the textarea for detailed template
        } else {
            textareaElement.style.display = 'none'; // Hide the textarea for other templates
            textareaElement.value = ''; // Clear the textarea when other options are selected
        }

        // Save content to localStorage
        saveContentToLocalStorage();
    });

    // Function to save content to localStorage
    function saveContentToLocalStorage() {
        localStorage.setItem('templateContent', textareaElement.value);
    }

    // Function to load content from localStorage
    function loadContentFromLocalStorage() {
		var savedContent = localStorage.getItem('templateContent');
		if (savedContent && selectElement.value && validOptions.includes(selectElement.value)) {
			textareaElement.value = savedContent;
			textareaElement.style.display = 'block';
		} else {
			textareaElement.style.display = 'none';
			textareaElement.value = '';
		}
	}

    // Load content from localStorage when page loads
    loadContentFromLocalStorage();

    // Save content to localStorage when textarea content changes
    textareaElement.addEventListener('input', function() {
        saveContentToLocalStorage();
    });
});


