// Event handler to select all tabs with the same label
// e.g. select all LaTeX representations
document.addEventListener("DOMContentLoaded", function () {
    const tabs = document.querySelectorAll(".sphinx-tabs-tab");

    function handler () {
        const selectedTabLabel = this.textContent;

        // Find all tabs with the same label
        const matchingTabs = Array.from(document.querySelectorAll('.sphinx-tabs-tab')).filter(
          tab => (tab.textContent.trim() === selectedTabLabel && tab !== this)
        );

        // Click all matching tabs
        //console.log(matchingTabs);
        matchingTabs.forEach((matchingTab) => {
            matchingTab.removeEventListener("click", handler);
            matchingTab.click();
            matchingTab.addEventListener("click", handler);
        });
      }

    tabs.forEach((tab) => {
      tab.addEventListener("click", handler);
    });
  });
