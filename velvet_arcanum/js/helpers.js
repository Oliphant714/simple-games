window.VA = window.VA || {};
var VA = window.VA;
VA.esc = function (value) { return String(value).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c])); };
VA.normalize = function (value) { return (value || '').trim().toLowerCase(); };
VA.ordinal = function (number) { const suffixes = ['th', 'st', 'nd', 'rd']; const value = number % 100; return number + (suffixes[(value - 20) % 10] || suffixes[value] || suffixes[0]); };
VA.dateLabel = function (day) { if (day === 3) return 'Thursday, the 9th'; if (day === 4) return 'Wednesday, the 22nd'; return ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][(day - 1) % 7] + ', the ' + VA.ordinal(day); };
VA.sigil = function (size, extraClass) { return '<svg class="sigil' + (extraClass ? ' ' + extraClass : '') + '" width="' + size + '" height="' + size + '" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="42" fill="none" stroke="currentColor" stroke-width="1.4"/><circle cx="50" cy="50" r="29" fill="none" stroke="currentColor" stroke-width="1"/><circle cx="50" cy="50" r="2.6" fill="currentColor"/><g stroke="currentColor" stroke-width="1.4"><line x1="50" y1="3" x2="50" y2="12"/><line x1="50" y1="88" x2="50" y2="97"/><line x1="3" y1="50" x2="12" y2="50"/><line x1="88" y1="50" x2="97" y2="50"/></g><circle cx="74" cy="27" r="1.6" fill="currentColor"/><circle cx="24" cy="73" r="1.4" fill="currentColor"/></svg>'; };
VA.capitalize = function (value) { return value.charAt(0).toUpperCase() + value.slice(1); };
