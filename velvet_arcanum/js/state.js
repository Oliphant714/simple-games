window.VA = window.VA || {};
var VA = window.VA;
VA.SAVE_KEY = 'velvet_arcanum_save_v1';
VA.state = null;
VA.defaultState = function () {
  return { v: 1, started: false, day: 1, timeBlock: 'morning', mc: { name: '', gender: '', collegeId: '', track: '', spells: [] }, energy: 70, flags: {}, relationships: { alex: 15, love: 0, clark: 0 }, job: null, mysteryAwareness: 0 };
};
VA.save = function () { try { localStorage.setItem(VA.SAVE_KEY, JSON.stringify(VA.state)); } catch (e) {} };
VA.loadSave = function () { try { const raw = localStorage.getItem(VA.SAVE_KEY); return raw ? JSON.parse(raw) : null; } catch (e) { return null; } };
VA.clearSave = function () { try { localStorage.removeItem(VA.SAVE_KEY); } catch (e) {} };
VA.setFlag = function (key, value) { VA.state.flags[key] = value; };
VA.getFlag = function (key) { return VA.state.flags[key]; };
VA.adjustEnergy = function (delta) { VA.state.energy = Math.max(0, Math.min(100, VA.state.energy + delta)); };
VA.adjustRel = function (id, delta) { VA.state.relationships[id] = (VA.state.relationships[id] || 0) + delta; };
VA.bumpMystery = function (delta) { VA.state.mysteryAwareness = Math.max(0, VA.state.mysteryAwareness + delta); };
VA.currentCollege = function () { return VA.COLLEGES[VA.state.mc.collegeId]; };
VA.loveInterest = function () { return VA.state.mc.gender === 'female' ? VA.NPCS.darian : VA.NPCS.lily; };
