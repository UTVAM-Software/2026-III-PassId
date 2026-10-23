(function () {
    /* Hamburger toggle para móvil */
    const toggle = document.getElementById('navToggle');
    const links  = document.getElementById('navLinks');
    if (toggle && links) {
        toggle.addEventListener('click', () => {
            const open = links.classList.toggle('is-open');
            toggle.setAttribute('aria-expanded', String(open));
        });
    }

    /* Cierra un dropdown al abrir otro */
    document.querySelectorAll('.nav-trigger').forEach(btn => {
        btn.addEventListener('click', e => {
            e.stopPropagation();
            const parent = btn.closest('.nav-dropdown');
            const isOpen = parent.classList.contains('is-open');
            document.querySelectorAll('.nav-dropdown.is-open').forEach(d => d.classList.remove('is-open'));
            if (!isOpen) {
                parent.classList.add('is-open');
            } else {
                btn.blur(); // libera el foco para que :focus-within no interfiera
            }
            btn.setAttribute('aria-expanded', String(!isOpen));
        });
    });

    /* Cierra al hacer clic fuera */
    document.addEventListener('click', () => {
        document.querySelectorAll('.nav-dropdown.is-open').forEach(d => {
            d.classList.remove('is-open');
            d.querySelector('.nav-trigger')?.setAttribute('aria-expanded', 'false');
        });
    });
})();
