(window.webpackJsonp=window.webpackJsonp||[]).push([[34],{"+Toe":function(e,t,a){"use strict";var n=a("2bPg"),r=a("BRlI"),c=a("PK3Q"),i=a("Q5Ww"),o=a("00an"),s=a("VDzl");var l=function(e){function t(e){var a;return Object(n.a)(this,t),(a=Object(c.a)(this,Object(i.a)(t).call(this,function(e){return"The method `".concat(e,"` is not implemented")}(e))))._methodName=e,a}return Object(o.a)(t,e),Object(r.a)(t,[{key:"methodName",get:function(){return this._methodName}}]),t}(Object(s.a)(Error));t.a=l},"0qOM":function(e,t,a){"use strict";var n=a("gbB/"),r=a.n(n),c=a("boeR"),i=a("i5Br"),o=a.n(i),s=a("zXLR");function l(e){var t=e.isFit,a=e.isTransparent,n=e.message,i=e.redirectLabel,l=e.redirectTo,u=e.replace;return r.a.createElement("div",{className:"layout"},r.a.createElement("div",{className:o()("layout__content layout__content--centered p-10",{"layout__content--fit":t},{"layout__content--transparent":a})},r.a.createElement("p",{className:"text-c"},n),i&&l&&r.a.createElement(s.a,{className:"btn btn-primary",component:c.Link,to:l,replace:u},i)))}l.defaultProps={replace:!1}},"2Hh2":function(e,t,a){"use strict";var n=a("g4DW"),r=a("DjBF"),c=a("7cf5"),i=a("gbB/"),o=a.n(i),s=a("i5Br"),l=a.n(s),u=a("ldfh"),d=a("tjC1");t.a=function(e){var t=e.className,a=e.items,s=e.hasSidebarHeader,b=e.hasHeaderToggleBtn,f=e.gaCategory,m=e.headerContent,O=e.footerContent,p=e.isAlwaysOpen,g=void 0!==p&&p,v=Object(c.a)(e,["className","items","hasSidebarHeader","hasHeaderToggleBtn","gaCategory","headerContent","footerContent","isAlwaysOpen"]),E=Object(u.k)().tablet;Object(i.useEffect)((function(){N()}),[]);var y=Object(i.useState)(!1),h=Object(r.a)(y,2),j=h[0],_=h[1],N=function(){_(!(!g&&E))};return o.a.createElement(d.a,Object.assign({className:l()(Object(n.a)({},t,t),"sidebar__".concat(j?"open":"close")),arrowClasses:l()(Object(n.a)({},"icon-arrow-".concat(E?"down":"left"),!0)),items:a,toggle:function(){_(!j)},hasHeaderToggleBtn:b,gaCategory:f||void 0,headerContent:m,footerContent:O,hasSidebarHeader:s},v))}},"6xkA":function(e,t,a){"use strict";a.d(t,"b",(function(){return m}));var n=a("g4DW"),r=a("butC"),c=a("dOmW"),i=a.n(c),o=a("NNZK"),s=a("T+CM");function l(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function u(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?l(Object(a),!0).forEach((function(t){Object(n.a)(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):l(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}var d="".concat(s.w,"/SEARCH_QUERY_INIT"),b="".concat(s.w,"/SEARCH_QUERY_DONE"),f="".concat(s.w,"/SEARCH_QUERY_ERROR");function m(e){return function(){var t=Object(r.a)(i.a.mark((function t(a,n){var r;return i.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(!n().header.search.isLoading){t.next=3;break}return t.abrupt("return");case 3:return a({type:d}),t.prev=4,t.next=7,o.a.searchKeyword(e);case 7:r=t.sent,a({type:b,payload:r}),t.next=14;break;case 11:t.prev=11,t.t0=t.catch(4),a({type:f,payload:t.t0});case 14:case"end":return t.stop()}}),t,null,[[4,11]])})));return function(e,a){return t.apply(this,arguments)}}()}var O={isLoading:!1,data:null,error:null};t.a=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:O,t=arguments.length>1?arguments[1]:void 0,a=t.type,n=t.payload;switch(a){case d:return u(u({},e),{},{error:null,isLoading:!0});case b:return u(u({},e),{},{isLoading:!1,data:n,error:null});case f:return u(u({},e),{},{isLoading:!1,error:n});default:return e}}},IJNI:function(e,t,a){"use strict";var n=a("g4DW"),r=a("7cf5"),c=a("gbB/"),i=a.n(c),o=a("i5Br"),s=a.n(o),l=a("q7zV"),u=a("y1EJ"),d=a("+tDs");function b(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}t.a=Object(d.c)((function(e){var t=e.className,a=e.component,c=e.iconName,o=e.item,d=e.isNew,f=e.withBadge,m=(e.isVisible,Object(r.a)(e,["className","component","iconName","item","isNew","withBadge","isVisible"])),O=s()("sidebar__item-text",{"sidebar__item-text--new":d||!1});return i.a.createElement(a,function(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?b(Object(a),!0).forEach((function(t){Object(n.a)(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):b(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}({className:s()("sidebar__item",Object(n.a)({},t,t))},m),[c?i.a.createElement(l.a,{key:"icon",name:c,className:"sidebar__item-icon"},f&&i.a.createElement(u.a,{position:{top:"1rem",right:"1rem"},style:{minWidth:"0.5rem",minHeight:"0.5rem",borderRadius:"50%"},type:"info"})):null,i.a.createElement("span",{key:"label",className:s()("sidebar__item--text",Object(n.a)({},O,O))},o)])}))},LO7R:function(e,t,a){"use strict";var n,r,c=a("UM7G"),i=a("2TJN"),o=a("aJYY"),s=[i.a,o.a.middleware],l=[c.a.apply(void 0,s)],u="object"==typeof window&&["development","staging"].includes(null===(n=window)||void 0===n?void 0:null===(r=n.ENV_VARS)||void 0===r?void 0:r.mode)&&window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__?window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__({}):c.d;t.a=function(e){var t=u.apply(void 0,l),a=Object(c.e)(e(),t);return a.asyncReducers={},a.injectReducer=function(t,n){return a.asyncReducers[t]=n,a.replaceReducer(e(a.asyncReducers)),a},a}},NNZK:function(e,t,a){"use strict";var n=a("upII");t.a={searchKeyword:function(e){return Object(n.b)("GET","/search_index/",{q:e})}}},RRQN:function(e,t,a){"use strict";var n=a("7cf5"),r=a("gbB/"),c=a.n(r),i=a("tKK5"),o=a("nz4c");t.a=function(e){var t=e.children,a=e.renderSingletons,r=void 0!==a&&a,s=e.namespace,l=e.alertProps,u=void 0===l?{}:l,d=e.dialogProps,b=void 0===d?{}:d,f=Object(n.a)(e,["children","renderSingletons","namespace","alertProps","dialogProps"]);return c.a.createElement(i.U,f,c.a.createElement(i.v,null,t,r&&c.a.createElement(c.a.Fragment,null,c.a.createElement(i.b,Object.assign({name:s},u)),c.a.createElement(i.p,Object.assign({name:s},b)),c.a.createElement(i.eb,null),c.a.createElement(i.T,null)),c.a.createElement(o.a,null)))}},UcDd:function(e,t,a){"use strict";a("tryK");var n=a("W+XG");a.d(t,"a",(function(){return n.a}));var r=a("2u0L");a.d(t,"b",(function(){return r.a}));var c=a("3bhF");a.d(t,"c",(function(){return c.a}));a("0qOM");var i=a("dv5D");a.d(t,"d",(function(){return i.a}))},"W+XG":function(e,t,a){"use strict";var n=a("gbB/"),r=a.n(n);t.a=function(e){var t=e.type,a=e.height;switch(t){case"block":return r.a.createElement("div",{style:{height:"100%"}});case"flex-fill":return r.a.createElement("div",{style:{flex:"1 0 0"}});case"flex-auto":return r.a.createElement("div",{style:{flex:"1 0 auto"}});default:return r.a.createElement("div",{style:{height:a}})}}},WXUJ:function(e,t,a){"use strict";var n=a("2bPg"),r=a("BRlI"),c=a("PK3Q"),i=a("Q5Ww"),o=a("00an"),s=a("VDzl"),l=function(e){function t(e,a){var r;return Object(n.a)(this,t),(r=Object(c.a)(this,Object(i.a)(t).call(this,e)))._underlyingError=a,r}return Object(o.a)(t,e),Object(r.a)(t,[{key:"isValid",get:function(){return this.underlying.isFromServer}},{key:"status",get:function(){return this.isValid?this.underlying.response.status:-1}},{key:"underlying",get:function(){return this._underlyingError}}]),t}(Object(s.a)(Error));t.a=l},XxnZ:function(e,t,a){"use strict";var n=a("2bPg"),r=a("PK3Q"),c=a("Q5Ww"),i=a("00an"),o=a("VDzl"),s=function(e){return"S3Error::".concat(e)},l=function(e){function t(e){var a;return Object(n.a)(this,t),(a=Object(r.a)(this,Object(c.a)(t).call(this,s(e)))).message=s(e),a.errorCode=e,a}return Object(i.a)(t,e),t}(Object(o.a)(Error));l.ATTACHMENT_INITIALIZATION_FAILED="ATTACHMENT_INITIALIZATION_FAILED",l.PAPERCLIP_POSTPOLICY_FAILED="PAPERCLIP_POSTPOLICY_FAILED",l.S3_UPLOAD_FAILED="S3_UPLOAD_FAILED",l.FILE_UPDATION_FAILED="FILE_UPDATION_FAILED",l.NETWORK_PROBLEM_DETECTED="NETWORK_PROBLEM_DETECTED",t.a=l},fUVL:function(e,t,a){"use strict";var n=a("UM7G"),r=a("ztZk"),c=a("6xkA");t.a=Object(n.c)({user:r.b,search:c.a})},h2tT:function(e,t,a){},nz4c:function(e,t,a){"use strict";a.d(t,"a",(function(){return o}));var n=a("DjBF"),r=a("gbB/"),c=a.n(r),i=a("8bDF");function o(){var e=Object(r.useState)(null),t=Object(n.a)(e,2),a=t[0],o=t[1],s=function(e){var t=e.data,a=JSON.parse(t),n=a.type,r=a.data,c=(r=void 0===r?{}:r).percent;"invalid"!==n?"progress-update"===n&&o(100===c?null:c):o(20)};return Object(r.useEffect)((function(){Object(i.b)()&&(new WebSocket("ws://localhost:8080/sockjs-node").onmessage=s)}),[]),Object(i.b)()&&a>0?c.a.createElement(c.a.Fragment,null,a&&c.a.createElement("div",{className:"hmr"},c.a.createElement("div",{className:"hmr__progress",style:{width:"".concat(a,"%")}}))):null}},sluu:function(e,t,a){"use strict";var n=a("WXUJ");a.d(t,"a",(function(){return n.a}));var r=a("+Toe");a.d(t,"b",(function(){return r.a}));var c=a("XxnZ");a.d(t,"c",(function(){return c.a}));a("SBIh")},tjC1:function(e,t,a){"use strict";var n=a("7cf5"),r=a("gbB/"),c=a.n(r),i=a("i5Br"),o=a.n(i),s=a("IJNI"),l=a("tKK5"),u=a("ldfh");t.a=function(e){var t=e.className,a=(e.sidebarClasses,e.arrowClasses),i=e.items,d=(e.device,e.toggle),b=e.hasHeaderToggleBtn,f=e.gaCategory,m=void 0===f?"":f,O=e.headerContent,p=e.footerContent,g=e.hasSidebarHeader,v=void 0===g||g,E=Object(n.a)(e,["className","sidebarClasses","arrowClasses","items","device","toggle","hasHeaderToggleBtn","gaCategory","headerContent","footerContent","hasSidebarHeader"]),y=Object(u.k)().mobile,h=Object(r.useCallback)((function(e){window.trackGaEvent("Academy-Sidebar","Navigation",e)}),[]);return c.a.createElement(c.a.Fragment,null,b&&c.a.createElement("div",{className:"sidebar__open-btn"},c.a.createElement(l.bb,{className:"btn btn-icon btn-inverted",onClick:d},c.a.createElement(l.D,{name:"hamburger"}))),c.a.createElement("div",Object.assign({"data-testid":"sidebar",className:o()("sidebar",t)},E),v&&c.a.createElement("div",{className:"sidebar__header",onClick:d},c.a.createElement("span",{className:"sidebar__header-text"},"Scaler"),c.a.createElement("span",{className:o()("sidebar__arrow",a)})),y&&b&&c.a.createElement("div",{className:"sidebar__close-btn","data-testid":"sidebar-close-icon"},c.a.createElement(l.bb,{className:"btn btn-icon btn-inverted",onClick:d},c.a.createElement(l.D,{name:"close"}))),O,c.a.createElement("div",{className:"sidebar__content scroll-bar-hidden",onClick:y?d:null},i.map((function(e,t){return function(e){return void 0===e.isVisible||e.isVisible}(e)&&c.a.createElement(s.a,Object.assign({key:t,onClick:function(){return h("".concat(m).concat(e.item))},gtmEventType:"side_nav",gtmEventAction:"click",gtmEventResult:e.item,gtmEventLink:e.to},e))}))),p))}},tryK:function(e,t,a){"use strict";var n=a("g4DW"),r=a("7cf5"),c=a("gbB/"),i=a.n(c),o=a("i5Br"),s=a.n(o),l=a("2Hh2");function u(e){var t=e.children,a=e.className,c=e.isSidebarDisabled,o=e.sidebarItems,u=e.sidebarClassName,d=e.product,b=e.onlySidebar,f=e.hasHeaderToggleBtn,m=e.sidebarGaCategory,O=void 0===m?"":m,p=e.sidebarHeaderContent,g=e.sidebarFooterContent,v=Object(r.a)(e,["children","className","isSidebarDisabled","sidebarItems","sidebarClassName","product","onlySidebar","hasHeaderToggleBtn","sidebarGaCategory","sidebarHeaderContent","sidebarFooterContent"]);return i.a.createElement("div",Object.assign({className:s()("dashboard",Object(n.a)({},a,a))},v),!c&&i.a.createElement(l.a,{className:u,items:o,product:d,hasHeaderToggleBtn:f,gaCategory:O||void 0,headerContent:p,footerContent:g}),b?"":i.a.createElement("div",{className:s()("dashboard__content",{"dashboard__content--sidebar-disabled":c})},t))}u.defaultProps={isSidebarDisabled:!1,sidebarClassName:"",onlySidebar:!1}},ztZk:function(e,t,a){"use strict";a.d(t,"d",(function(){return O})),a.d(t,"a",(function(){return p})),a.d(t,"c",(function(){return g})),a.d(t,"e",(function(){return v}));var n=a("g4DW"),r=a("upjz"),c=a("T+CM"),i=a("JqKp");function o(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function s(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?o(Object(a),!0).forEach((function(t){Object(n.a)(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):o(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}var l="interviewbit/header",u="".concat(l,"/CHANGE_COINS"),d="".concat(l,"/FINISH_NUX_TOUR"),b="".concat(l,"/UPDATE_SCORE"),f="".concat(l,"/UPDATE/USER_DATA"),m="".concat(l,"/UPDATE/SCALER_HUB_DATA"),O=function(e){return function(t){return t({type:f,payload:e})}},p=function(e){return function(t){return t({type:u,payload:e})}},g=function(e,t){return function(a){a({type:d,payload:{NuxKey:e,NuxValue:t}})}},v=function(e,t){var a=e.hasSolved,n=e.submissionResult,r=e.achievedScore,c=t.obtainedScore;return function(e){a&&"correct_answer"===n&&e({type:b,payload:c||r})}},E={data:i.w,loggedIn:Boolean(null===i.w||void 0===i.w?void 0:i.w.userId),Options:[{href:"/profile/".concat(null===i.w||void 0===i.w?void 0:i.w.username),label:"Profile"}].concat(Object(r.a)(c.A))};t.b=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:E,t=arguments.length>1?arguments[1]:void 0,a=t.type,r=t.payload;switch(a){case u:return s(s({},e),{},{data:s(s({},e.data),{},{coins:r})});case d:return s(s({},e),{},{data:s(s({},e.data),{},Object(n.a)({},r.NuxKey,r.NuxValue))});case b:return s(s({},e),{},{data:s(s({},e.data),{},{score:e.data.score+r})});case f:return s(s({},e),{},{data:s(s({},e.data),r),loggedIn:!0});case m:return s(s({},e),{},{data:s(s({},e.data),r)});default:return e}}}}]);