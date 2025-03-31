function toggleSection(id) {
    document.querySelectorAll('.section').forEach(section => {
        if (section.id === id) {
            section.classList.remove('collapsed');
        } else {
            section.classList.add('collapsed');
        }
    });
}