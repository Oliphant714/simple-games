window.VA = window.VA || {};
var VA = window.VA;
const existingSave = VA.loadSave();
VA.state = existingSave || VA.defaultState();
VA.render(VA.sceneTitle);
