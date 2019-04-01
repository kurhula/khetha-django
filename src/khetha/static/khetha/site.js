/* Site-wide initialisation for Khetha. */

(function () {
    // https://material.io/develop/web/components/cards/#javascript
    const selector = '.mdc-button, .mdc-icon-button, .mdc-card__primary-action';
    const ripples = [].map.call(document.querySelectorAll(selector), function (el) {
        return new window.mdc.ripple.MDCRipple(el);
    });
})();