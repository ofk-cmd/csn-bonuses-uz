(function () {
  var cards = document.querySelectorAll('.casino-card');
  var buttons = document.querySelectorAll('.rating-filter__btn');
  var search = document.querySelector('.rating-search');
  var countEl = document.querySelector('[data-rating-visible]');
  if (!cards.length) return;

  function applyFilter() {
    var type = document.querySelector('.rating-filter__btn.is-active');
    var filter = type ? type.getAttribute('data-filter') : 'all';
    var q = search ? search.value.trim().toLowerCase() : '';
    var visible = 0;
    cards.forEach(function (card) {
      var cardType = card.getAttribute('data-type') || 'both';
      var name = (card.getAttribute('data-name') || '').toLowerCase();
      var matchType = filter === 'all' || cardType === filter || cardType === 'both';
      var matchSearch = !q || name.indexOf(q) !== -1;
      var show = matchType && matchSearch;
      card.classList.toggle('is-hidden', !show);
      if (show) visible++;
    });
    if (countEl) countEl.textContent = String(visible);
  }

  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      buttons.forEach(function (b) { b.classList.remove('is-active'); });
      btn.classList.add('is-active');
      applyFilter();
    });
  });
  if (search) search.addEventListener('input', applyFilter);
  applyFilter();
})();
