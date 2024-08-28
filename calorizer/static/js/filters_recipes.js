document.addEventListener('DOMContentLoaded', function() {
    const checkboxes = document.querySelectorAll('.type-checkbox');
    const selectedContainer = document.getElementById('selected-types');

    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            const label = this.closest('label').textContent.trim();

            if (this.checked) {
                // Check if the span already exists before adding
                if (!selectedContainer.querySelector(`span[data-value="${this.value}"]`)) {
                    const span = document.createElement('span');
                    span.classList.add('badge', 'bg-primary', 'me-1');
                    span.textContent = label;
                    span.setAttribute('data-value', this.value);
                    selectedContainer.appendChild(span);
                }
            } else {
                // Remove unselected checkbox label
                const spanToRemove = selectedContainer.querySelector(`span[data-value="${this.value}"]`);
                if (spanToRemove) {
                    selectedContainer.removeChild(spanToRemove);
                }
            }
        });
    });
});