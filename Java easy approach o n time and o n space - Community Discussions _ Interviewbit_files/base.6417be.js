!function(e){function t(t){for(var r,o,s=t[0],c=t[1],u=t[2],f=0,d=[];f<s.length;f++)o=s[f],Object.prototype.hasOwnProperty.call(i,o)&&i[o]&&d.push(i[o][0]),i[o]=0;for(r in c)Object.prototype.hasOwnProperty.call(c,r)&&(e[r]=c[r]);for(l&&l(t);d.length;)d.shift()();return a.push.apply(a,u||[]),n()}function n(){for(var e,t=0;t<a.length;t++){for(var n=a[t],r=!0,s=1;s<n.length;s++){var c=n[s];0!==i[c]&&(r=!1)}r&&(a.splice(t--,1),e=o(o.s=n[0]))}return e}var r={},i={80:0},a=[];function o(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,o),n.l=!0,n.exports}o.m=e,o.c=r,o.d=function(e,t,n){o.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},o.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},o.t=function(e,t){if(1&t&&(e=o(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(o.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)o.d(n,r,function(t){return e[t]}.bind(null,r));return n},o.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return o.d(t,"a",t),t},o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},o.p="https://assets.interviewbit.com/packs/";var s=window.webpackJsonp=window.webpackJsonp||[],c=s.push.bind(s);s.push=t,s=s.slice();for(var u=0;u<s.length;u++)t(s[u]);var l=c;a.push(["AMIh",0,2,186,1,3]),n()}({"7zL1":function(e,t,n){"use strict";var r=n("2bPg"),i=n("BRlI"),a=function(){function e(t){var n=this;if(Object(r.a)(this,e),this.sync=function(){n._data=n._loadLocalStorage()},!e.initializing)throw new Error("Use LocalStorage.getInstance instead");this._key=t,this.sync(),e.initializing=!1}return Object(i.a)(e,[{key:"addItem",value:function(e,t){this._data[e]=t,this._saveLocalStorage()}},{key:"removeItem",value:function(e){delete this._data[e],this._saveLocalStorage()}},{key:"_loadLocalStorage",value:function(){var e=window.localStorage.getItem(this._key);return e?JSON.parse(e):{}}},{key:"_saveLocalStorage",value:function(){window.localStorage.setItem(this._key,JSON.stringify(this._data))}}],[{key:"getInstance",value:function(t){if(!this.instance[t]){this.initializing=!0;try{this.instance[t]=new Proxy(new e(t),{get:function(e,t){return t.startsWith("$_")?e[t.substring("$_".length)]:e._data[t]},set:function(e,t,n){return e.addItem(t,n),!0},deleteProperty:function(e,t){return e.removeItem(t),!0}})}catch(e){}}return this.instance[t]}}]),e}();a.instance={},a.initializing=!1,t.a=a},"8BTH":function(e,t,n){"use strict";function r(){document.documentElement.classList.add("cannot-touch"),document.addEventListener("touchstart",(function e(){window.__CAN_TOUCH__=!0,document.documentElement.classList.remove("cannot-touch"),document.documentElement.classList.add("can-touch"),document.removeEventListener("touchstart",e,!1)}),!1)}n.d(t,"a",(function(){return r}))},AMIh:function(e,t,n){"use strict";n.r(t);var r=n("8BTH"),i=n("xyMv"),a=n("GTbB"),o=n("Q1SX"),s=(n("bkXJ"),n("L0im"));Object(r.a)(),Object(i.b)(),Object(o.c)()&&a.i.initialize(),window.addEventListener("load",(function(){s.a.syncAllEvents()}))},EsI2:function(e,t,n){"use strict";n.d(t,"k",(function(){return r})),n.d(t,"m",(function(){return i})),n.d(t,"i",(function(){return a})),n.d(t,"j",(function(){return o})),n.d(t,"l",(function(){return s})),n.d(t,"e",(function(){return c})),n.d(t,"c",(function(){return u})),n.d(t,"g",(function(){return l})),n.d(t,"f",(function(){return f})),n.d(t,"h",(function(){return d})),n.d(t,"a",(function(){return p})),n.d(t,"b",(function(){return v})),n.d(t,"d",(function(){return h}));var r=480,i=768,a=1024,o=1200,s="https://i.imgur.com/URiqMtc.png",c="create-diagram-tab",u="data:image/svg+xml;base64,",l={promoter:"promoter",detractor:"detractor",neutral:"neutral"},f="desktop-playstore",d="header__playstore-popup-container",p="app-playstore-link",v="app-playstore-strip-link",h="contact-us-top-nav"},L0im:function(e,t,n){"use strict";var r=n("upjz"),i=n("g4DW"),a=n("DjBF"),o=n("butC"),s=n("2bPg"),c=n("BRlI"),u=n("MkmS"),l=n.n(u),f=n("Vyyf"),d=n.n(f),p=n("Q1SX"),v=n("iB1e"),h=n("Pkhr"),b=n("TQpo");function _(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function y(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?_(Object(n),!0).forEach((function(t){Object(i.a)(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):_(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}var g=n("7zL1").a.getInstance("__vp_tracker__"),O="play",m="pause";function j(){return g.$_sync(),g.events||[]}var w=function(){var e,t;function n(e,t){Object(s.a)(this,n),this.trackingSessionId=Object(p.b)(),this.syncedIntervals={},this.allIntervals={},this._type=e,this._extraParams=t}return Object(c.a)(n,null,[{key:"syncAllEvents",value:(e=Object(o.a)(l.a.mark((function e(){var t,n,r;return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(0!==(t=j()).length){e.next=3;break}return e.abrupt("return");case 3:return e.next=5,b.a.send(t);case 5:n=e.sent,r=j().filter((function(e){return!n.includes(e.unique_id)})),g.events=r;case 8:case"end":return e.stop()}}),e)}))),function(){return e.apply(this,arguments)})}]),Object(c.a)(n,[{key:"update",value:function(e,t){if(t){var n=Object(h.b)(t),o=this._calculateAllAndUnSyncedIntervals(e,n),s=Object(a.a)(o,2),c=s[0],u=s[1],l=this._intervalsToEvents(e,u),f=this._calculateUniqueVideoId(e);this.allIntervals=y(y({},this.allIntervals),{},Object(i.a)({},f,c));var d=this._findOtherVideoEvents(e);g.events=[].concat(Object(r.a)(d),Object(r.a)(l))}}},{key:"sync",value:(t=Object(o.a)(l.a.mark((function e(){var t,n,i,a,o=this;return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(0!==(t=this.allEvents.filter((function(e){return e.session_id===o.trackingSessionId}))).length){e.next=3;break}return e.abrupt("return");case 3:return e.prev=3,e.next=6,b.a.send(t,{session_id:this.trackingSessionId});case 6:n=e.sent,i=Object(r.a)(this.allEvents),a=i.filter((function(e){return!n.includes(e.unique_id)})),g.events=a,this.syncedIntervals=d()(this.allIntervals);case 11:return e.prev=11,this.trackingSessionId=Object(p.b)(),e.finish(11);case 14:case"end":return e.stop()}}),e,this,[[3,,11,14]])}))),function(){return t.apply(this,arguments)})},{key:"_calculateAllAndUnSyncedIntervals",value:function(e,t){var n=this._findSyncedIntervals(e),i=this._findPreviousIntervals(e),a=Object(v.b)([].concat(Object(r.a)(i),Object(r.a)(t),Object(r.a)(n)));return[a,Object(v.a)(a,n)]}},{key:"_calculateUniqueVideoId",value:function(e){return"".concat(this._type,"-").concat(e)}},{key:"_findOtherVideoEvents",value:function(e){var t=this;return this.allEvents.filter((function(n){return n.session_id!==t.trackingSessionId||n.resource_type!==t._type||n.resource_id!==e}))}},{key:"_findPreviousIntervals",value:function(e){var t=this._calculateUniqueVideoId(e),n=this.allIntervals[t]||[];return Object(r.a)(n)}},{key:"_findSyncedIntervals",value:function(e){var t=this._calculateUniqueVideoId(e),n=this.syncedIntervals[t]||[];return Object(r.a)(n)}},{key:"_intervalsToEvents",value:function(e,t){var n=this._calculateUniqueVideoId(e),r=y({session_id:this.trackingSessionId,resource_type:this._type,resource_id:e},this._extraParams),i=[];return t.forEach((function(e,t){i.push(y(y({},r),{},{unique_id:"".concat(n,"_").concat(Date.now(),"_start_").concat(t),event_type:O,time:e[0]})),i.push(y(y({},r),{unique_id:"".concat(n,"_").concat(Date.now(),"_end_").concat(t),event_type:m,time:e[1]}))})),i}},{key:"allEvents",get:function(){return j()}}]),n}();t.a=w},Pkhr:function(e,t,n){"use strict";function r(e){for(var t=[],n=0;n<e.length;n+=1)t.push({start:e.start(n),end:e.end(n)});return t}function i(e){for(var t=[],n=e.length,r=0;r<n;r+=1)t.push([e.start(r),e.end(r)]);return t}n.d(t,"a",(function(){return r})),n.d(t,"b",(function(){return i}))},TQpo:function(e,t,n){"use strict";var r=n("g4DW"),i=n("butC"),a=n("MkmS"),o=n.n(a),s=n("upII");function c(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function u(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?c(Object(n),!0).forEach((function(t){Object(r.a)(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):c(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function l(){return(l=Object(i.a)(o.a.mark((function e(t){var n,r,i,a=arguments;return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(n=a.length>1&&void 0!==a[1]?a[1]:{},0!==t.length){e.next=3;break}return e.abrupt("return",[]);case 3:return e.next=5,Object(s.b)("POST","/recordings/events",u({events:t},n),{keepalive:!0});case 5:return r=e.sent,i=r.processed_events,e.abrupt("return",i);case 8:case"end":return e.stop()}}),e)})))).apply(this,arguments)}t.a={send:function(e){return l.apply(this,arguments)}}},bkXJ:function(e,t,n){},iB1e:function(e,t,n){"use strict";n.d(t,"b",(function(){return i})),n.d(t,"a",(function(){return s}));var r=n("upjz");function i(e){return e.sort((function(e,t){return e[0]-t[0]})).reduce((function(e,t){return!e.length||e[e.length-1][1]<t[0]?e.push(t):e[e.length-1][1]=Math.max(e[e.length-1][1],t[1]),e}),[])}function a(e){var t={},n=[];return e.forEach((function(e){var r=e.toString();t[r]||(t[r]=1,n.push(e))})),n}function o(e,t){var n=[];return e.forEach((function(e){var i=function(e,t){if(e[1]<t[0])return[e];if(e[0]>t[1])return[e];var n=[],r=[e[0],Math.min(e[1],t[0])];r[0]<r[1]&&n.push(r);var i=[t[1],e[1]];return i[0]<i[1]&&n.push(i),n}(e,t);n.push.apply(n,Object(r.a)(i))})),n}function s(e,t){var n=[];return e.forEach((function(e){var i,s=function(e,t){var n=[e];return t.forEach((function(e){n=o(n,e)})),a(n)}(e,t);(i=n).push.apply(i,Object(r.a)(s))})),n=a(n)}},xyMv:function(e,t,n){"use strict";n.d(t,"b",(function(){return f}));var r=n("butC"),i=n("2bPg"),a=n("BRlI"),o=n("MkmS"),s=n.n(o),c=n("EsI2"),u=!1,l=function(){function e(t){Object(i.a)(this,e),this._assetUrl=t,this._size=0}return Object(a.a)(e,null,[{key:"isEnabled",value:function(){return window.storeEsEvent&&window.ENV_VARS&&window.ENV_VARS.config&&window.ENV_VARS.config.speed_test_enabled}}]),Object(a.a)(e,[{key:"measureDownlink",value:function(){var e=this,t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:5e3;return new Promise((function(n){e._request=new XMLHttpRequest,e._request.responseType="blob",e._timeout=setTimeout((function(){e._request.abort(),n({speed:e.speed,completed:!1})}),t),e._request.onload=function(){200===e._request.status&&(clearTimeout(e._timeout),e._createHeadersMap(),e._endTime=Date.now(),e._size=e._responseHeaders["content-length"],n({speed:e.speed,completed:!0}))},e._request.onprogress=function(t){e._endTime=Date.now(),e._size=t.loaded},e._startTime=Date.now(),e._request.open("GET","".concat(e._assetUrl,"?v=").concat(Date.now()),!0),e._request.send()}))}},{key:"_createHeadersMap",value:function(){var e=this._request.getAllResponseHeaders().trim().split(/[\r\n]+/),t={};e.forEach((function(e){var n=e.split(": "),r=n.shift(),i=n.join(": ");t[r.toLowerCase()]=i})),this._responseHeaders=t}},{key:"speed",get:function(){return 0===this._size?0:8*this._size/1024/((this._endTime-this._startTime)/1e3)}}],[{key:"checkLastSpeedTest",value:function(){if("undefined"!=typeof Storage){var e=Date.now()-parseInt(localStorage.getItem("speedtest-time"),10);return Math.floor(e/1e3/60)<=10}return!1}}]),e}();function f(){u||l.checkLastSpeedTest()||(u=!0,window.addEventListener("load",Object(r.a)(s.a.mark((function e(){var t,n;return s.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(!l.isEnabled()){e.next=8;break}return t=new l(c.l),e.next=4,t.measureDownlink();case 4:if(n=e.sent,console.info("Download speed:",n.speed.toFixed(2),"kbps"),window.storeEsEvent("download-speed","log",n.speed),n.completed&&"undefined"!=typeof Storage)try{localStorage.setItem("speedtest-time",Date.now())}catch(e){}case 8:case"end":return e.stop()}}),e)})))))}t.a=l}});