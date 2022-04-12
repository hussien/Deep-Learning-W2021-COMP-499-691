(function(){/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
'use strict';var m;function aa(a){var b=0;return function(){return b<a.length?{done:!1,value:a[b++]}:{done:!0}}}
var ca="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){if(a==Array.prototype||a==Object.prototype)return a;a[b]=c.value;return a};
function da(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("Cannot find global object");}
var ea=da(this);function t(a,b){if(b)a:{var c=ea;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&null!=b&&ca(c,a,{configurable:!0,writable:!0,value:b})}}
t("Symbol",function(a){function b(e){if(this instanceof b)throw new TypeError("Symbol is not a constructor");return new c("jscomp_symbol_"+(e||"")+"_"+d++,e)}
function c(e,f){this.h=e;ca(this,"description",{configurable:!0,writable:!0,value:f})}
if(a)return a;c.prototype.toString=function(){return this.h};
var d=0;return b});
t("Symbol.iterator",function(a){if(a)return a;a=Symbol("Symbol.iterator");for(var b="Array Int8Array Uint8Array Uint8ClampedArray Int16Array Uint16Array Int32Array Uint32Array Float32Array Float64Array".split(" "),c=0;c<b.length;c++){var d=ea[b[c]];"function"===typeof d&&"function"!=typeof d.prototype[a]&&ca(d.prototype,a,{configurable:!0,writable:!0,value:function(){return fa(aa(this))}})}return a});
function fa(a){a={next:a};a[Symbol.iterator]=function(){return this};
return a}
function u(a){var b="undefined"!=typeof Symbol&&Symbol.iterator&&a[Symbol.iterator];return b?b.call(a):{next:aa(a)}}
function ha(a){for(var b,c=[];!(b=a.next()).done;)c.push(b.value);return c}
var ia="function"==typeof Object.create?Object.create:function(a){function b(){}
b.prototype=a;return new b},ja=function(){function a(){function c(){}
new c;Reflect.construct(c,[],function(){});
return new c instanceof c}
if("undefined"!=typeof Reflect&&Reflect.construct){if(a())return Reflect.construct;var b=Reflect.construct;return function(c,d,e){c=b(c,d);e&&Reflect.setPrototypeOf(c,e.prototype);return c}}return function(c,d,e){void 0===e&&(e=c);
e=ia(e.prototype||Object.prototype);return Function.prototype.apply.call(c,e,d)||e}}(),ka;
if("function"==typeof Object.setPrototypeOf)ka=Object.setPrototypeOf;else{var la;a:{var ma={a:!0},oa={};try{oa.__proto__=ma;la=oa.a;break a}catch(a){}la=!1}ka=la?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError(a+" is not extensible");return a}:null}var pa=ka;
function v(a,b){a.prototype=ia(b.prototype);a.prototype.constructor=a;if(pa)pa(a,b);else for(var c in b)if("prototype"!=c)if(Object.defineProperties){var d=Object.getOwnPropertyDescriptor(b,c);d&&Object.defineProperty(a,c,d)}else a[c]=b[c];a.L=b.prototype}
function qa(){this.o=!1;this.l=null;this.i=void 0;this.h=1;this.u=this.m=0;this.C=this.j=null}
function ra(a){if(a.o)throw new TypeError("Generator is already running");a.o=!0}
qa.prototype.A=function(a){this.i=a};
function sa(a,b){a.j={xa:b,ya:!0};a.h=a.m||a.u}
qa.prototype.return=function(a){this.j={return:a};this.h=this.u};
function w(a,b,c){a.h=c;return{value:b}}
qa.prototype.B=function(a){this.h=a};
function ta(a,b,c){a.m=b;void 0!=c&&(a.u=c)}
function ua(a){a.m=0;var b=a.j.xa;a.j=null;return b}
function va(a){a.C=[a.j];a.m=0;a.u=0}
function wa(a){var b=a.C.splice(0)[0];(b=a.j=a.j||b)?b.ya?a.h=a.m||a.u:void 0!=b.B&&a.u<b.B?(a.h=b.B,a.j=null):a.h=a.u:a.h=0}
function xa(a){this.h=new qa;this.i=a}
function ya(a,b){ra(a.h);var c=a.h.l;if(c)return za(a,"return"in c?c["return"]:function(d){return{value:d,done:!0}},b,a.h.return);
a.h.return(b);return Aa(a)}
function za(a,b,c,d){try{var e=b.call(a.h.l,c);if(!(e instanceof Object))throw new TypeError("Iterator result "+e+" is not an object");if(!e.done)return a.h.o=!1,e;var f=e.value}catch(g){return a.h.l=null,sa(a.h,g),Aa(a)}a.h.l=null;d.call(a.h,f);return Aa(a)}
function Aa(a){for(;a.h.h;)try{var b=a.i(a.h);if(b)return a.h.o=!1,{value:b.value,done:!1}}catch(c){a.h.i=void 0,sa(a.h,c)}a.h.o=!1;if(a.h.j){b=a.h.j;a.h.j=null;if(b.ya)throw b.xa;return{value:b.return,done:!0}}return{value:void 0,done:!0}}
function Ba(a){this.next=function(b){ra(a.h);a.h.l?b=za(a,a.h.l.next,b,a.h.A):(a.h.A(b),b=Aa(a));return b};
this.throw=function(b){ra(a.h);a.h.l?b=za(a,a.h.l["throw"],b,a.h.A):(sa(a.h,b),b=Aa(a));return b};
this.return=function(b){return ya(a,b)};
this[Symbol.iterator]=function(){return this}}
function x(a,b){b=new Ba(new xa(b));pa&&a.prototype&&pa(b,a.prototype);return b}
t("Reflect",function(a){return a?a:{}});
t("Reflect.construct",function(){return ja});
t("Reflect.setPrototypeOf",function(a){return a?a:pa?function(b,c){try{return pa(b,c),!0}catch(d){return!1}}:null});
function Ca(a,b,c){if(null==a)throw new TypeError("The 'this' value for String.prototype."+c+" must not be null or undefined");if(b instanceof RegExp)throw new TypeError("First argument to String.prototype."+c+" must not be a regular expression");return a+""}
t("String.prototype.endsWith",function(a){return a?a:function(b,c){var d=Ca(this,b,"endsWith");b+="";void 0===c&&(c=d.length);c=Math.max(0,Math.min(c|0,d.length));for(var e=b.length;0<e&&0<c;)if(d[--c]!=b[--e])return!1;return 0>=e}});
t("String.prototype.startsWith",function(a){return a?a:function(b,c){var d=Ca(this,b,"startsWith");b+="";var e=d.length,f=b.length;c=Math.max(0,Math.min(c|0,d.length));for(var g=0;g<f&&c<e;)if(d[c++]!=b[g++])return!1;return g>=f}});
t("Object.setPrototypeOf",function(a){return a||pa});
function Da(a,b){return Object.prototype.hasOwnProperty.call(a,b)}
var Ea="function"==typeof Object.assign?Object.assign:function(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(d)for(var e in d)Da(d,e)&&(a[e]=d[e])}return a};
t("Object.assign",function(a){return a||Ea});
t("Promise",function(a){function b(g){this.h=0;this.j=void 0;this.i=[];this.o=!1;var h=this.l();try{g(h.resolve,h.reject)}catch(k){h.reject(k)}}
function c(){this.h=null}
function d(g){return g instanceof b?g:new b(function(h){h(g)})}
if(a)return a;c.prototype.i=function(g){if(null==this.h){this.h=[];var h=this;this.j(function(){h.u()})}this.h.push(g)};
var e=ea.setTimeout;c.prototype.j=function(g){e(g,0)};
c.prototype.u=function(){for(;this.h&&this.h.length;){var g=this.h;this.h=[];for(var h=0;h<g.length;++h){var k=g[h];g[h]=null;try{k()}catch(l){this.l(l)}}}this.h=null};
c.prototype.l=function(g){this.j(function(){throw g;})};
b.prototype.l=function(){function g(l){return function(p){k||(k=!0,l.call(h,p))}}
var h=this,k=!1;return{resolve:g(this.K),reject:g(this.u)}};
b.prototype.K=function(g){if(g===this)this.u(new TypeError("A Promise cannot resolve to itself"));else if(g instanceof b)this.U(g);else{a:switch(typeof g){case "object":var h=null!=g;break a;case "function":h=!0;break a;default:h=!1}h?this.J(g):this.m(g)}};
b.prototype.J=function(g){var h=void 0;try{h=g.then}catch(k){this.u(k);return}"function"==typeof h?this.V(h,g):this.m(g)};
b.prototype.u=function(g){this.A(2,g)};
b.prototype.m=function(g){this.A(1,g)};
b.prototype.A=function(g,h){if(0!=this.h)throw Error("Cannot settle("+g+", "+h+"): Promise already settled in state"+this.h);this.h=g;this.j=h;2===this.h&&this.M();this.C()};
b.prototype.M=function(){var g=this;e(function(){if(g.G()){var h=ea.console;"undefined"!==typeof h&&h.error(g.j)}},1)};
b.prototype.G=function(){if(this.o)return!1;var g=ea.CustomEvent,h=ea.Event,k=ea.dispatchEvent;if("undefined"===typeof k)return!0;"function"===typeof g?g=new g("unhandledrejection",{cancelable:!0}):"function"===typeof h?g=new h("unhandledrejection",{cancelable:!0}):(g=ea.document.createEvent("CustomEvent"),g.initCustomEvent("unhandledrejection",!1,!0,g));g.promise=this;g.reason=this.j;return k(g)};
b.prototype.C=function(){if(null!=this.i){for(var g=0;g<this.i.length;++g)f.i(this.i[g]);this.i=null}};
var f=new c;b.prototype.U=function(g){var h=this.l();g.da(h.resolve,h.reject)};
b.prototype.V=function(g,h){var k=this.l();try{g.call(h,k.resolve,k.reject)}catch(l){k.reject(l)}};
b.prototype.then=function(g,h){function k(r,q){return"function"==typeof r?function(B){try{l(r(B))}catch(I){p(I)}}:q}
var l,p,n=new b(function(r,q){l=r;p=q});
this.da(k(g,l),k(h,p));return n};
b.prototype.catch=function(g){return this.then(void 0,g)};
b.prototype.da=function(g,h){function k(){switch(l.h){case 1:g(l.j);break;case 2:h(l.j);break;default:throw Error("Unexpected state: "+l.h);}}
var l=this;null==this.i?f.i(k):this.i.push(k);this.o=!0};
b.resolve=d;b.reject=function(g){return new b(function(h,k){k(g)})};
b.race=function(g){return new b(function(h,k){for(var l=u(g),p=l.next();!p.done;p=l.next())d(p.value).da(h,k)})};
b.all=function(g){var h=u(g),k=h.next();return k.done?d([]):new b(function(l,p){function n(B){return function(I){r[B]=I;q--;0==q&&l(r)}}
var r=[],q=0;do r.push(void 0),q++,d(k.value).da(n(r.length-1),p),k=h.next();while(!k.done)})};
return b});
t("Object.is",function(a){return a?a:function(b,c){return b===c?0!==b||1/b===1/c:b!==b&&c!==c}});
t("Array.prototype.includes",function(a){return a?a:function(b,c){var d=this;d instanceof String&&(d=String(d));var e=d.length;c=c||0;for(0>c&&(c=Math.max(c+e,0));c<e;c++){var f=d[c];if(f===b||Object.is(f,b))return!0}return!1}});
t("String.prototype.includes",function(a){return a?a:function(b,c){return-1!==Ca(this,b,"includes").indexOf(b,c||0)}});
t("Object.entries",function(a){return a?a:function(b){var c=[],d;for(d in b)Da(b,d)&&c.push([d,b[d]]);return c}});
t("WeakMap",function(a){function b(k){this.h=(h+=Math.random()+1).toString();if(k){k=u(k);for(var l;!(l=k.next()).done;)l=l.value,this.set(l[0],l[1])}}
function c(){}
function d(k){var l=typeof k;return"object"===l&&null!==k||"function"===l}
function e(k){if(!Da(k,g)){var l=new c;ca(k,g,{value:l})}}
function f(k){var l=Object[k];l&&(Object[k]=function(p){if(p instanceof c)return p;Object.isExtensible(p)&&e(p);return l(p)})}
if(function(){if(!a||!Object.seal)return!1;try{var k=Object.seal({}),l=Object.seal({}),p=new a([[k,2],[l,3]]);if(2!=p.get(k)||3!=p.get(l))return!1;p.delete(k);p.set(l,4);return!p.has(k)&&4==p.get(l)}catch(n){return!1}}())return a;
var g="$jscomp_hidden_"+Math.random();f("freeze");f("preventExtensions");f("seal");var h=0;b.prototype.set=function(k,l){if(!d(k))throw Error("Invalid WeakMap key");e(k);if(!Da(k,g))throw Error("WeakMap key fail: "+k);k[g][this.h]=l;return this};
b.prototype.get=function(k){return d(k)&&Da(k,g)?k[g][this.h]:void 0};
b.prototype.has=function(k){return d(k)&&Da(k,g)&&Da(k[g],this.h)};
b.prototype.delete=function(k){return d(k)&&Da(k,g)&&Da(k[g],this.h)?delete k[g][this.h]:!1};
return b});
t("Map",function(a){function b(){var h={};return h.previous=h.next=h.head=h}
function c(h,k){var l=h.h;return fa(function(){if(l){for(;l.head!=h.h;)l=l.previous;for(;l.next!=l.head;)return l=l.next,{done:!1,value:k(l)};l=null}return{done:!0,value:void 0}})}
function d(h,k){var l=k&&typeof k;"object"==l||"function"==l?f.has(k)?l=f.get(k):(l=""+ ++g,f.set(k,l)):l="p_"+k;var p=h.i[l];if(p&&Da(h.i,l))for(h=0;h<p.length;h++){var n=p[h];if(k!==k&&n.key!==n.key||k===n.key)return{id:l,list:p,index:h,H:n}}return{id:l,list:p,index:-1,H:void 0}}
function e(h){this.i={};this.h=b();this.size=0;if(h){h=u(h);for(var k;!(k=h.next()).done;)k=k.value,this.set(k[0],k[1])}}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var h=Object.seal({x:4}),k=new a(u([[h,"s"]]));if("s"!=k.get(h)||1!=k.size||k.get({x:4})||k.set({x:4},"t")!=k||2!=k.size)return!1;var l=k.entries(),p=l.next();if(p.done||p.value[0]!=h||"s"!=p.value[1])return!1;p=l.next();return p.done||4!=p.value[0].x||"t"!=p.value[1]||!l.next().done?!1:!0}catch(n){return!1}}())return a;
var f=new WeakMap;e.prototype.set=function(h,k){h=0===h?0:h;var l=d(this,h);l.list||(l.list=this.i[l.id]=[]);l.H?l.H.value=k:(l.H={next:this.h,previous:this.h.previous,head:this.h,key:h,value:k},l.list.push(l.H),this.h.previous.next=l.H,this.h.previous=l.H,this.size++);return this};
e.prototype.delete=function(h){h=d(this,h);return h.H&&h.list?(h.list.splice(h.index,1),h.list.length||delete this.i[h.id],h.H.previous.next=h.H.next,h.H.next.previous=h.H.previous,h.H.head=null,this.size--,!0):!1};
e.prototype.clear=function(){this.i={};this.h=this.h.previous=b();this.size=0};
e.prototype.has=function(h){return!!d(this,h).H};
e.prototype.get=function(h){return(h=d(this,h).H)&&h.value};
e.prototype.entries=function(){return c(this,function(h){return[h.key,h.value]})};
e.prototype.keys=function(){return c(this,function(h){return h.key})};
e.prototype.values=function(){return c(this,function(h){return h.value})};
e.prototype.forEach=function(h,k){for(var l=this.entries(),p;!(p=l.next()).done;)p=p.value,h.call(k,p[1],p[0],this)};
e.prototype[Symbol.iterator]=e.prototype.entries;var g=0;return e});
t("Set",function(a){function b(c){this.h=new Map;if(c){c=u(c);for(var d;!(d=c.next()).done;)this.add(d.value)}this.size=this.h.size}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var c=Object.seal({x:4}),d=new a(u([c]));if(!d.has(c)||1!=d.size||d.add(c)!=d||1!=d.size||d.add({x:4})!=d||2!=d.size)return!1;var e=d.entries(),f=e.next();if(f.done||f.value[0]!=c||f.value[1]!=c)return!1;f=e.next();return f.done||f.value[0]==c||4!=f.value[0].x||f.value[1]!=f.value[0]?!1:e.next().done}catch(g){return!1}}())return a;
b.prototype.add=function(c){c=0===c?0:c;this.h.set(c,c);this.size=this.h.size;return this};
b.prototype.delete=function(c){c=this.h.delete(c);this.size=this.h.size;return c};
b.prototype.clear=function(){this.h.clear();this.size=0};
b.prototype.has=function(c){return this.h.has(c)};
b.prototype.entries=function(){return this.h.entries()};
b.prototype.values=function(){return this.h.values()};
b.prototype.keys=b.prototype.values;b.prototype[Symbol.iterator]=b.prototype.values;b.prototype.forEach=function(c,d){var e=this;this.h.forEach(function(f){return c.call(d,f,f,e)})};
return b});
function Fa(a,b){a instanceof String&&(a+="");var c=0,d=!1,e={next:function(){if(!d&&c<a.length){var f=c++;return{value:b(f,a[f]),done:!1}}d=!0;return{done:!0,value:void 0}}};
e[Symbol.iterator]=function(){return e};
return e}
t("Array.prototype.entries",function(a){return a?a:function(){return Fa(this,function(b,c){return[b,c]})}});
t("Array.prototype.keys",function(a){return a?a:function(){return Fa(this,function(b){return b})}});
t("Array.prototype.values",function(a){return a?a:function(){return Fa(this,function(b,c){return c})}});
t("Number.isNaN",function(a){return a?a:function(b){return"number"===typeof b&&isNaN(b)}});
t("Number.MAX_SAFE_INTEGER",function(){return 9007199254740991});
t("Object.values",function(a){return a?a:function(b){var c=[],d;for(d in b)Da(b,d)&&c.push(b[d]);return c}});
var y=this||self;function z(a,b,c){a=a.split(".");c=c||y;a[0]in c||"undefined"==typeof c.execScript||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)a.length||void 0===b?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b}
function Ga(a){if(a&&a!=y)return Ha(a.document);null===Ia&&(Ia=Ha(y.document));return Ia}
var Ja=/^[\w+/_-]+[=]{0,2}$/,Ia=null;function Ha(a){return(a=a.querySelector&&a.querySelector("script[nonce]"))&&(a=a.nonce||a.getAttribute("nonce"))&&Ja.test(a)?a:""}
function A(a,b){a=a.split(".");b=b||y;for(var c=0;c<a.length;c++)if(b=b[a[c]],null==b)return null;return b}
function Ka(){}
function La(a){a.na=void 0;a.getInstance=function(){return a.na?a.na:a.na=new a}}
function Ma(a){var b=typeof a;return"object"!=b?b:a?Array.isArray(a)?"array":b:"null"}
function Na(a){var b=Ma(a);return"array"==b||"object"==b&&"number"==typeof a.length}
function Oa(a){var b=typeof a;return"object"==b&&null!=a||"function"==b}
function Pa(a){return Object.prototype.hasOwnProperty.call(a,Qa)&&a[Qa]||(a[Qa]=++Ra)}
var Qa="closure_uid_"+(1E9*Math.random()>>>0),Ra=0;function Sa(a,b,c){return a.call.apply(a.bind,arguments)}
function Ta(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var e=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(e,d);return a.apply(b,e)}}return function(){return a.apply(b,arguments)}}
function C(a,b,c){Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?C=Sa:C=Ta;return C.apply(null,arguments)}
function Ua(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}}
function Va(a,b){z(a,b,void 0)}
function D(a,b){function c(){}
c.prototype=b.prototype;a.L=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.Hk=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}}
function Wa(a){return a}
;function Xa(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,Xa);else{var c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));b&&(this.Ja=b)}
D(Xa,Error);Xa.prototype.name="CustomError";function Ya(a){a=a.url;var b=/[?&]dsh=1(&|$)/.test(a);this.j=!b&&/[?&]ae=1(&|$)/.test(a);this.l=!b&&/[?&]ae=2(&|$)/.test(a);if((this.h=/[?&]adurl=([^&]*)/.exec(a))&&this.h[1]){try{var c=decodeURIComponent(this.h[1])}catch(d){c=null}this.i=c}}
;function Za(a){var b=!1,c;return function(){b||(c=a(),b=!0);return c}}
;var $a=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if("string"===typeof a)return"string"!==typeof b||1!=b.length?-1:a.indexOf(b,0);
for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},E=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e="string"===typeof a?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)},ab=Array.prototype.filter?function(a,b){return Array.prototype.filter.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=[],e=0,f="string"===typeof a?a.split(""):a,g=0;g<c;g++)if(g in f){var h=f[g];
b.call(void 0,h,g,a)&&(d[e++]=h)}return d},bb=Array.prototype.map?function(a,b){return Array.prototype.map.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=Array(c),e="string"===typeof a?a.split(""):a,f=0;f<c;f++)f in e&&(d[f]=b.call(void 0,e[f],f,a));
return d},cb=Array.prototype.reduce?function(a,b,c){return Array.prototype.reduce.call(a,b,c)}:function(a,b,c){var d=c;
E(a,function(e,f){d=b.call(void 0,d,e,f,a)});
return d};
function db(a,b){a:{for(var c=a.length,d="string"===typeof a?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a)){b=e;break a}b=-1}return 0>b?null:"string"===typeof a?a.charAt(b):a[b]}
function eb(a,b){b=$a(a,b);var c;(c=0<=b)&&Array.prototype.splice.call(a,b,1);return c}
function fb(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]}
function gb(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(Na(d)){var e=a.length||0,f=d.length||0;a.length=e+f;for(var g=0;g<f;g++)a[e+g]=d[g]}else a.push(d)}}
;function hb(a,b){for(var c in a)b.call(void 0,a[c],c,a)}
function ib(a){var b=jb,c;for(c in b)if(a.call(void 0,b[c],c,b))return c}
function kb(a){for(var b in a)return!1;return!0}
function lb(a,b){if(null!==a&&b in a)throw Error('The object already contains the key "'+b+'"');a[b]=!0}
function nb(){var a=F("PLAYER_VARS",{});return null!==a&&"privembed"in a?a.privembed:!1}
function ob(a,b){for(var c in a)if(!(c in b)||a[c]!==b[c])return!1;for(var d in b)if(!(d in a))return!1;return!0}
function pb(a){var b={},c;for(c in a)b[c]=a[c];return b}
function qb(a){if(!a||"object"!==typeof a)return a;if("function"===typeof a.clone)return a.clone();var b=Array.isArray(a)?[]:"function"!==typeof ArrayBuffer||"function"!==typeof ArrayBuffer.isView||!ArrayBuffer.isView(a)||a instanceof DataView?{}:new a.constructor(a.length),c;for(c in a)b[c]=qb(a[c]);return b}
var rb="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");function sb(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<rb.length;f++)c=rb[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}}
;var tb;function ub(){if(void 0===tb){var a=null,b=y.trustedTypes;if(b&&b.createPolicy){try{a=b.createPolicy("goog#html",{createHTML:Wa,createScript:Wa,createScriptURL:Wa})}catch(c){y.console&&y.console.error(c.message)}tb=a}else tb=a}return tb}
;function vb(a,b){this.h=b===wb?a:""}
m=vb.prototype;m.X=!0;m.W=function(){return this.h.toString()};
m.ma=!0;m.ja=function(){return 1};
m.toString=function(){return this.h+""};
function xb(a){if(a instanceof vb&&a.constructor===vb)return a.h;Ma(a);return"type_error:TrustedResourceUrl"}
var wb={};var yb=String.prototype.trim?function(a){return a.trim()}:function(a){return/^[\s\xa0]*([\s\S]*?)[\s\xa0]*$/.exec(a)[1]};
function zb(a,b){if(b)a=a.replace(Ab,"&amp;").replace(Bb,"&lt;").replace(Cb,"&gt;").replace(Db,"&quot;").replace(Eb,"&#39;").replace(Fb,"&#0;");else{if(!Gb.test(a))return a;-1!=a.indexOf("&")&&(a=a.replace(Ab,"&amp;"));-1!=a.indexOf("<")&&(a=a.replace(Bb,"&lt;"));-1!=a.indexOf(">")&&(a=a.replace(Cb,"&gt;"));-1!=a.indexOf('"')&&(a=a.replace(Db,"&quot;"));-1!=a.indexOf("'")&&(a=a.replace(Eb,"&#39;"));-1!=a.indexOf("\x00")&&(a=a.replace(Fb,"&#0;"))}return a}
var Ab=/&/g,Bb=/</g,Cb=/>/g,Db=/"/g,Eb=/'/g,Fb=/\x00/g,Gb=/[\x00&<>"']/;function Hb(a,b){this.h=b===Ib?a:""}
m=Hb.prototype;m.X=!0;m.W=function(){return this.h.toString()};
m.ma=!0;m.ja=function(){return 1};
m.toString=function(){return this.h.toString()};
function Jb(a){if(a instanceof Hb&&a.constructor===Hb)return a.h;Ma(a);return"type_error:SafeUrl"}
var Kb=/^(?:audio\/(?:3gpp2|3gpp|aac|L16|midi|mp3|mp4|mpeg|oga|ogg|opus|x-m4a|x-matroska|x-wav|wav|webm)|font\/\w+|image\/(?:bmp|gif|jpeg|jpg|png|tiff|webp|x-icon)|video\/(?:mpeg|mp4|ogg|webm|quicktime|x-matroska))(?:;\w+=(?:\w+|"[\w;,= ]+"))*$/i,Lb=/^data:(.*);base64,[a-z0-9+\/]+=*$/i,Mb=/^(?:(?:https?|mailto|ftp):|[^:/?#]*(?:[/?#]|$))/i;function Nb(a){if(a instanceof Hb)return a;a="object"==typeof a&&a.X?a.W():String(a);Mb.test(a)||(a="about:invalid#zClosurez");return new Hb(a,Ib)}
var Ib={},Ob=new Hb("about:invalid#zClosurez",Ib);var Pb;a:{var Qb=y.navigator;if(Qb){var Rb=Qb.userAgent;if(Rb){Pb=Rb;break a}}Pb=""}function G(a){return-1!=Pb.indexOf(a)}
;function Sb(a,b,c){this.h=c===Tb?a:"";this.i=b}
m=Sb.prototype;m.ma=!0;m.ja=function(){return this.i};
m.X=!0;m.W=function(){return this.h.toString()};
m.toString=function(){return this.h.toString()};
var Tb={};function Ub(a,b){var c=ub();a=c?c.createHTML(a):a;return new Sb(a,b,Tb)}
;function Vb(a,b){b=b instanceof Hb?b:Nb(b);a.href=Jb(b)}
function Wb(a,b){a.rel="stylesheet";a.href=xb(b).toString();(b=a.ownerDocument&&a.ownerDocument.defaultView)&&b!=y?b=Xb(b.document):(null===Yb&&(Yb=Xb(y.document)),b=Yb);b&&a.setAttribute("nonce",b)}
function Zb(a,b){a.src=xb(b);(b=Ga(a.ownerDocument&&a.ownerDocument.defaultView))&&a.setAttribute("nonce",b)}
var Yb=null,$b=/^[\w+/_-]+[=]{0,2}$/;function Xb(a){if(!a.querySelector)return"";var b=a.querySelector("style[nonce]");b||(b=a.querySelector('link[rel="stylesheet"][nonce]'));return b&&(a=b.nonce||b.getAttribute("nonce"))&&$b.test(a)?a:""}
;function ac(a){return a=zb(a,void 0)}
function bc(a){for(var b=0,c=0;c<a.length;++c)b=31*b+a.charCodeAt(c)>>>0;return b}
;var cc=/^(?:([^:/?#.]+):)?(?:\/\/(?:([^\\/?#]*)@)?([^\\/?#]*?)(?::([0-9]+))?(?=[\\/?#]|$))?([^?#]+)?(?:\?([^#]*))?(?:#([\s\S]*))?$/;function dc(a){return a?decodeURI(a):a}
function ec(a){return dc(a.match(cc)[3]||null)}
function fc(a,b,c){if(Array.isArray(b))for(var d=0;d<b.length;d++)fc(a,String(b[d]),c);else null!=b&&c.push(a+(""===b?"":"="+encodeURIComponent(String(b))))}
function gc(a){var b=[],c;for(c in a)fc(c,a[c],b);return b.join("&")}
function hc(a,b){b=gc(b);if(b){var c=a.indexOf("#");0>c&&(c=a.length);var d=a.indexOf("?");if(0>d||d>c){d=c;var e=""}else e=a.substring(d+1,c);a=[a.substr(0,d),e,a.substr(c)];c=a[1];a[1]=b?c?c+"&"+b:b:c;b=a[0]+(a[1]?"?"+a[1]:"")+a[2]}else b=a;return b}
var ic=/#|$/;function H(a,b){var c=void 0;return new (c||(c=Promise))(function(d,e){function f(k){try{h(b.next(k))}catch(l){e(l)}}
function g(k){try{h(b["throw"](k))}catch(l){e(l)}}
function h(k){k.done?d(k.value):(new c(function(l){l(k.value)})).then(f,g)}
h((b=b.apply(a,void 0)).next())})}
;function jc(){return G("iPhone")&&!G("iPod")&&!G("iPad")}
;function kc(a){kc[" "](a);return a}
kc[" "]=Ka;var lc=G("Opera"),mc=G("Trident")||G("MSIE"),nc=G("Edge"),oc=G("Gecko")&&!(-1!=Pb.toLowerCase().indexOf("webkit")&&!G("Edge"))&&!(G("Trident")||G("MSIE"))&&!G("Edge"),pc=-1!=Pb.toLowerCase().indexOf("webkit")&&!G("Edge");function qc(){var a=y.document;return a?a.documentMode:void 0}
var rc;a:{var sc="",tc=function(){var a=Pb;if(oc)return/rv:([^\);]+)(\)|;)/.exec(a);if(nc)return/Edge\/([\d\.]+)/.exec(a);if(mc)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(pc)return/WebKit\/(\S+)/.exec(a);if(lc)return/(?:Version)[ \/]?(\S+)/.exec(a)}();
tc&&(sc=tc?tc[1]:"");if(mc){var uc=qc();if(null!=uc&&uc>parseFloat(sc)){rc=String(uc);break a}}rc=sc}var vc=rc,wc;if(y.document&&mc){var xc=qc();wc=xc?xc:parseInt(vc,10)||void 0}else wc=void 0;var yc=wc;var zc=jc()||G("iPod"),Ac=G("iPad"),Bc=G("Safari")&&!((G("Chrome")||G("CriOS"))&&!G("Edge")||G("Coast")||G("Opera")||G("Edge")||G("Edg/")||G("OPR")||G("Firefox")||G("FxiOS")||G("Silk")||G("Android"))&&!(jc()||G("iPad")||G("iPod"));var Cc={},Dc=null;
function Ec(a){var b=3;Na(a);void 0===b&&(b=0);if(!Dc){Dc={};for(var c="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split(""),d=["+/=","+/","-_=","-_.","-_"],e=0;5>e;e++){var f=c.concat(d[e].split(""));Cc[e]=f;for(var g=0;g<f.length;g++){var h=f[g];void 0===Dc[h]&&(Dc[h]=g)}}}b=Cc[b];c=[];for(d=0;d<a.length;d+=3){var k=a[d],l=(e=d+1<a.length)?a[d+1]:0;h=(f=d+2<a.length)?a[d+2]:0;g=k>>2;k=(k&3)<<4|l>>4;l=(l&15)<<2|h>>6;h&=63;f||(h=64,e||(l=64));c.push(b[g],b[k],b[l]||"",b[h]||"")}return c.join("")}
;var K=window;var Fc=!mc||9<=Number(yc);function Gc(a,b){this.x=void 0!==a?a:0;this.y=void 0!==b?b:0}
m=Gc.prototype;m.clone=function(){return new Gc(this.x,this.y)};
m.equals=function(a){return a instanceof Gc&&(this==a?!0:this&&a?this.x==a.x&&this.y==a.y:!1)};
m.ceil=function(){this.x=Math.ceil(this.x);this.y=Math.ceil(this.y);return this};
m.floor=function(){this.x=Math.floor(this.x);this.y=Math.floor(this.y);return this};
m.round=function(){this.x=Math.round(this.x);this.y=Math.round(this.y);return this};function Hc(a,b){this.width=a;this.height=b}
m=Hc.prototype;m.clone=function(){return new Hc(this.width,this.height)};
m.aspectRatio=function(){return this.width/this.height};
m.isEmpty=function(){return!(this.width*this.height)};
m.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
m.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
m.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};function Ic(a){var b=document;return"string"===typeof a?b.getElementById(a):a}
function Jc(a,b){hb(b,function(c,d){c&&"object"==typeof c&&c.X&&(c=c.W());"style"==d?a.style.cssText=c:"class"==d?a.className=c:"for"==d?a.htmlFor=c:Kc.hasOwnProperty(d)?a.setAttribute(Kc[d],c):0==d.lastIndexOf("aria-",0)||0==d.lastIndexOf("data-",0)?a.setAttribute(d,c):a[d]=c})}
var Kc={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
function Lc(a,b,c){var d=arguments,e=document,f=String(d[0]),g=d[1];if(!Fc&&g&&(g.name||g.type)){f=["<",f];g.name&&f.push(' name="',ac(g.name),'"');if(g.type){f.push(' type="',ac(g.type),'"');var h={};sb(h,g);delete h.type;g=h}f.push(">");f=f.join("")}f=Mc(e,f);g&&("string"===typeof g?f.className=g:Array.isArray(g)?f.className=g.join(" "):Jc(f,g));2<d.length&&Nc(e,f,d);return f}
function Nc(a,b,c){function d(h){h&&b.appendChild("string"===typeof h?a.createTextNode(h):h)}
for(var e=2;e<c.length;e++){var f=c[e];if(!Na(f)||Oa(f)&&0<f.nodeType)d(f);else{a:{if(f&&"number"==typeof f.length){if(Oa(f)){var g="function"==typeof f.item||"string"==typeof f.item;break a}if("function"===typeof f){g="function"==typeof f.item;break a}}g=!1}E(g?fb(f):f,d)}}}
function Mc(a,b){b=String(b);"application/xhtml+xml"===a.contentType&&(b=b.toLowerCase());return a.createElement(b)}
function Oc(a,b){for(var c=0;a;){if(b(a))return a;a=a.parentNode;c++}return null}
;function Pc(a){var b=Qc;if(b)for(var c in b)Object.prototype.hasOwnProperty.call(b,c)&&a.call(void 0,b[c],c,b)}
function Rc(){var a=[];Pc(function(b){a.push(b)});
return a}
var Qc={zb:"allow-forms",Ab:"allow-modals",Bb:"allow-orientation-lock",Cb:"allow-pointer-lock",Db:"allow-popups",Eb:"allow-popups-to-escape-sandbox",Fb:"allow-presentation",Gb:"allow-same-origin",Hb:"allow-scripts",Ib:"allow-top-navigation",Jb:"allow-top-navigation-by-user-activation"},Sc=Za(function(){return Rc()});
function Tc(){var a=Mc(document,"IFRAME"),b={};E(Sc(),function(c){a.sandbox&&a.sandbox.supports&&a.sandbox.supports(c)&&(b[c]=!0)});
return b}
;function Uc(a){Vc();var b=ub();a=b?b.createScriptURL(a):a;return new vb(a,wb)}
var Vc=Ka;function Wc(a){"number"==typeof a&&(a=Math.round(a)+"px");return a}
;var Xc=(new Date).getTime();function Yc(a){if(!a)return"";a=a.split("#")[0].split("?")[0];a=a.toLowerCase();0==a.indexOf("//")&&(a=window.location.protocol+a);/^[\w\-]*:\/\//.test(a)||(a=window.location.href);var b=a.substring(a.indexOf("://")+3),c=b.indexOf("/");-1!=c&&(b=b.substring(0,c));c=a.substring(0,a.indexOf("://"));if(!c)throw Error("URI is missing protocol: "+a);if("http"!==c&&"https"!==c&&"chrome-extension"!==c&&"moz-extension"!==c&&"file"!==c&&"android-app"!==c&&"chrome-search"!==c&&"chrome-untrusted"!==c&&"chrome"!==
c&&"app"!==c&&"devtools"!==c)throw Error("Invalid URI scheme in origin: "+c);a="";var d=b.indexOf(":");if(-1!=d){var e=b.substring(d+1);b=b.substring(0,d);if("http"===c&&"80"!==e||"https"===c&&"443"!==e)a=":"+e}return c+"://"+b+a}
;function Zc(){function a(){e[0]=1732584193;e[1]=4023233417;e[2]=2562383102;e[3]=271733878;e[4]=3285377520;p=l=0}
function b(n){for(var r=g,q=0;64>q;q+=4)r[q/4]=n[q]<<24|n[q+1]<<16|n[q+2]<<8|n[q+3];for(q=16;80>q;q++)n=r[q-3]^r[q-8]^r[q-14]^r[q-16],r[q]=(n<<1|n>>>31)&4294967295;n=e[0];var B=e[1],I=e[2],J=e[3],ba=e[4];for(q=0;80>q;q++){if(40>q)if(20>q){var U=J^B&(I^J);var O=1518500249}else U=B^I^J,O=1859775393;else 60>q?(U=B&I|J&(B|I),O=2400959708):(U=B^I^J,O=3395469782);U=((n<<5|n>>>27)&4294967295)+U+ba+O+r[q]&4294967295;ba=J;J=I;I=(B<<30|B>>>2)&4294967295;B=n;n=U}e[0]=e[0]+n&4294967295;e[1]=e[1]+B&4294967295;
e[2]=e[2]+I&4294967295;e[3]=e[3]+J&4294967295;e[4]=e[4]+ba&4294967295}
function c(n,r){if("string"===typeof n){n=unescape(encodeURIComponent(n));for(var q=[],B=0,I=n.length;B<I;++B)q.push(n.charCodeAt(B));n=q}r||(r=n.length);q=0;if(0==l)for(;q+64<r;)b(n.slice(q,q+64)),q+=64,p+=64;for(;q<r;)if(f[l++]=n[q++],p++,64==l)for(l=0,b(f);q+64<r;)b(n.slice(q,q+64)),q+=64,p+=64}
function d(){var n=[],r=8*p;56>l?c(h,56-l):c(h,64-(l-56));for(var q=63;56<=q;q--)f[q]=r&255,r>>>=8;b(f);for(q=r=0;5>q;q++)for(var B=24;0<=B;B-=8)n[r++]=e[q]>>B&255;return n}
for(var e=[],f=[],g=[],h=[128],k=1;64>k;++k)h[k]=0;var l,p;a();return{reset:a,update:c,digest:d,Ka:function(){for(var n=d(),r="",q=0;q<n.length;q++)r+="0123456789ABCDEF".charAt(Math.floor(n[q]/16))+"0123456789ABCDEF".charAt(n[q]%16);return r}}}
;function $c(a,b,c){var d=String(y.location.href);return d&&a&&b?[b,ad(Yc(d),a,c||null)].join(" "):null}
function ad(a,b,c){var d=[],e=[];if(1==(Array.isArray(c)?2:1))return e=[b,a],E(d,function(h){e.push(h)}),bd(e.join(" "));
var f=[],g=[];E(c,function(h){g.push(h.key);f.push(h.value)});
c=Math.floor((new Date).getTime()/1E3);e=0==f.length?[c,b,a]:[f.join(":"),c,b,a];E(d,function(h){e.push(h)});
a=bd(e.join(" "));a=[c,a];0==g.length||a.push(g.join(""));return a.join("_")}
function bd(a){var b=Zc();b.update(a);return b.Ka().toLowerCase()}
;var cd={};function dd(a){this.h=a||{cookie:""}}
m=dd.prototype;m.isEnabled=function(){if(!y.navigator.cookieEnabled)return!1;if(!this.isEmpty())return!0;this.set("TESTCOOKIESENABLED","1",{oa:60});if("1"!==this.get("TESTCOOKIESENABLED"))return!1;this.remove("TESTCOOKIESENABLED");return!0};
m.set=function(a,b,c){var d=!1;if("object"===typeof c){var e=c.Ok;d=c.secure||!1;var f=c.domain||void 0;var g=c.path||void 0;var h=c.oa}if(/[;=\s]/.test(a))throw Error('Invalid cookie name "'+a+'"');if(/[;\r\n]/.test(b))throw Error('Invalid cookie value "'+b+'"');void 0===h&&(h=-1);this.h.cookie=a+"="+b+(f?";domain="+f:"")+(g?";path="+g:"")+(0>h?"":0==h?";expires="+(new Date(1970,1,1)).toUTCString():";expires="+(new Date(Date.now()+1E3*h)).toUTCString())+(d?";secure":"")+(null!=e?";samesite="+e:"")};
m.get=function(a,b){for(var c=a+"=",d=(this.h.cookie||"").split(";"),e=0,f;e<d.length;e++){f=yb(d[e]);if(0==f.lastIndexOf(c,0))return f.substr(c.length);if(f==a)return""}return b};
m.remove=function(a,b,c){var d=void 0!==this.get(a);this.set(a,"",{oa:0,path:b,domain:c});return d};
m.isEmpty=function(){return!this.h.cookie};
m.clear=function(){for(var a=(this.h.cookie||"").split(";"),b=[],c=[],d,e,f=0;f<a.length;f++)e=yb(a[f]),d=e.indexOf("="),-1==d?(b.push(""),c.push(e)):(b.push(e.substring(0,d)),c.push(e.substring(d+1)));for(a=b.length-1;0<=a;a--)this.remove(b[a])};
var ed=new dd("undefined"==typeof document?null:document);function fd(a){return!!cd.FPA_SAMESITE_PHASE2_MOD||!(void 0===a||!a)}
function gd(a,b,c,d){(a=y[a])||(a=(new dd(document)).get(b));return a?$c(a,c,d):null}
function hd(a){var b=void 0===b?!1:b;var c=Yc(String(y.location.href)),d=[];var e=b;e=void 0===e?!1:e;var f=y.__SAPISID||y.__APISID||y.__3PSAPISID||y.__OVERRIDE_SID;fd(e)&&(f=f||y.__1PSAPISID);if(f)e=!0;else{var g=new dd(document);f=g.get("SAPISID")||g.get("APISID")||g.get("__Secure-3PAPISID")||g.get("SID");fd(e)&&(f=f||g.get("__Secure-1PAPISID"));e=!!f}e&&(e=(c=0==c.indexOf("https:")||0==c.indexOf("chrome-extension:")||0==c.indexOf("moz-extension:"))?y.__SAPISID:y.__APISID,e||(e=new dd(document),
e=e.get(c?"SAPISID":"APISID")||e.get("__Secure-3PAPISID")),(e=e?$c(e,c?"SAPISIDHASH":"APISIDHASH",a):null)&&d.push(e),c&&fd(b)&&((b=gd("__1PSAPISID","__Secure-1PAPISID","SAPISID1PHASH",a))&&d.push(b),(a=gd("__3PSAPISID","__Secure-3PAPISID","SAPISID3PHASH",a))&&d.push(a)));return 0==d.length?null:d.join(" ")}
;function id(){this.h=[];this.i=-1}
id.prototype.set=function(a,b){b=void 0===b?!0:b;0<=a&&52>a&&0===a%1&&this.h[a]!=b&&(this.h[a]=b,this.i=-1)};
id.prototype.get=function(a){return!!this.h[a]};
function jd(a){-1==a.i&&(a.i=cb(a.h,function(b,c,d){return c?b+Math.pow(2,d):b},0));
return a.i}
;function kd(a,b){this.j=a;this.l=b;this.i=0;this.h=null}
kd.prototype.get=function(){if(0<this.i){this.i--;var a=this.h;this.h=a.next;a.next=null}else a=this.j();return a};
function ld(a,b){a.l(b);100>a.i&&(a.i++,b.next=a.h,a.h=b)}
;var md;
function nd(){var a=y.MessageChannel;"undefined"===typeof a&&"undefined"!==typeof window&&window.postMessage&&window.addEventListener&&!G("Presto")&&(a=function(){var e=Mc(document,"IFRAME");e.style.display="none";document.documentElement.appendChild(e);var f=e.contentWindow;e=f.document;e.open();e.close();var g="callImmediate"+Math.random(),h="file:"==f.location.protocol?"*":f.location.protocol+"//"+f.location.host;e=C(function(k){if(("*"==h||k.origin==h)&&k.data==g)this.port1.onmessage()},this);
f.addEventListener("message",e,!1);this.port1={};this.port2={postMessage:function(){f.postMessage(g,h)}}});
if("undefined"!==typeof a&&!G("Trident")&&!G("MSIE")){var b=new a,c={},d=c;b.port1.onmessage=function(){if(void 0!==c.next){c=c.next;var e=c.ta;c.ta=null;e()}};
return function(e){d.next={ta:e};d=d.next;b.port2.postMessage(0)}}return function(e){y.setTimeout(e,0)}}
;function od(a){y.setTimeout(function(){throw a;},0)}
;function pd(){this.i=this.h=null}
pd.prototype.add=function(a,b){var c=qd.get();c.set(a,b);this.i?this.i.next=c:this.h=c;this.i=c};
pd.prototype.remove=function(){var a=null;this.h&&(a=this.h,this.h=this.h.next,this.h||(this.i=null),a.next=null);return a};
var qd=new kd(function(){return new rd},function(a){return a.reset()});
function rd(){this.next=this.scope=this.h=null}
rd.prototype.set=function(a,b){this.h=a;this.scope=b;this.next=null};
rd.prototype.reset=function(){this.next=this.scope=this.h=null};function sd(a,b){td||ud();vd||(td(),vd=!0);wd.add(a,b)}
var td;function ud(){if(y.Promise&&y.Promise.resolve){var a=y.Promise.resolve(void 0);td=function(){a.then(xd)}}else td=function(){var b=xd;
"function"!==typeof y.setImmediate||y.Window&&y.Window.prototype&&!G("Edge")&&y.Window.prototype.setImmediate==y.setImmediate?(md||(md=nd()),md(b)):y.setImmediate(b)}}
var vd=!1,wd=new pd;function xd(){for(var a;a=wd.remove();){try{a.h.call(a.scope)}catch(b){od(b)}ld(qd,a)}vd=!1}
;function yd(){this.i=-1}
;function zd(){this.i=64;this.h=[];this.m=[];this.o=[];this.l=[];this.l[0]=128;for(var a=1;a<this.i;++a)this.l[a]=0;this.u=this.j=0;this.reset()}
D(zd,yd);zd.prototype.reset=function(){this.h[0]=1732584193;this.h[1]=4023233417;this.h[2]=2562383102;this.h[3]=271733878;this.h[4]=3285377520;this.u=this.j=0};
function Ad(a,b,c){c||(c=0);var d=a.o;if("string"===typeof b)for(var e=0;16>e;e++)d[e]=b.charCodeAt(c)<<24|b.charCodeAt(c+1)<<16|b.charCodeAt(c+2)<<8|b.charCodeAt(c+3),c+=4;else for(e=0;16>e;e++)d[e]=b[c]<<24|b[c+1]<<16|b[c+2]<<8|b[c+3],c+=4;for(e=16;80>e;e++){var f=d[e-3]^d[e-8]^d[e-14]^d[e-16];d[e]=(f<<1|f>>>31)&4294967295}b=a.h[0];c=a.h[1];var g=a.h[2],h=a.h[3],k=a.h[4];for(e=0;80>e;e++){if(40>e)if(20>e){f=h^c&(g^h);var l=1518500249}else f=c^g^h,l=1859775393;else 60>e?(f=c&g|h&(c|g),l=2400959708):
(f=c^g^h,l=3395469782);f=(b<<5|b>>>27)+f+k+l+d[e]&4294967295;k=h;h=g;g=(c<<30|c>>>2)&4294967295;c=b;b=f}a.h[0]=a.h[0]+b&4294967295;a.h[1]=a.h[1]+c&4294967295;a.h[2]=a.h[2]+g&4294967295;a.h[3]=a.h[3]+h&4294967295;a.h[4]=a.h[4]+k&4294967295}
zd.prototype.update=function(a,b){if(null!=a){void 0===b&&(b=a.length);for(var c=b-this.i,d=0,e=this.m,f=this.j;d<b;){if(0==f)for(;d<=c;)Ad(this,a,d),d+=this.i;if("string"===typeof a)for(;d<b;){if(e[f]=a.charCodeAt(d),++f,++d,f==this.i){Ad(this,e);f=0;break}}else for(;d<b;)if(e[f]=a[d],++f,++d,f==this.i){Ad(this,e);f=0;break}}this.j=f;this.u+=b}};
zd.prototype.digest=function(){var a=[],b=8*this.u;56>this.j?this.update(this.l,56-this.j):this.update(this.l,this.i-(this.j-56));for(var c=this.i-1;56<=c;c--)this.m[c]=b&255,b/=256;Ad(this,this.m);for(c=b=0;5>c;c++)for(var d=24;0<=d;d-=8)a[b]=this.h[c]>>d&255,++b;return a};function Bd(a){var b=A("window.location.href");null==a&&(a='Unknown Error of type "null/undefined"');if("string"===typeof a)return{message:a,name:"Unknown error",lineNumber:"Not available",fileName:b,stack:"Not available"};var c=!1;try{var d=a.lineNumber||a.line||"Not available"}catch(g){d="Not available",c=!0}try{var e=a.fileName||a.filename||a.sourceURL||y.$googDebugFname||b}catch(g){e="Not available",c=!0}b=Cd(a);if(!(!c&&a.lineNumber&&a.fileName&&a.stack&&a.message&&a.name)){c=a.message;if(null==
c){if(a.constructor&&a.constructor instanceof Function){if(a.constructor.name)c=a.constructor.name;else if(c=a.constructor,Dd[c])c=Dd[c];else{c=String(c);if(!Dd[c]){var f=/function\s+([^\(]+)/m.exec(c);Dd[c]=f?f[1]:"[Anonymous]"}c=Dd[c]}c='Unknown Error of type "'+c+'"'}else c="Unknown Error of unknown type";"function"===typeof a.toString&&Object.prototype.toString!==a.toString&&(c+=": "+a.toString())}return{message:c,name:a.name||"UnknownError",lineNumber:d,fileName:e,stack:b||"Not available"}}a.stack=
b;return{message:a.message,name:a.name,lineNumber:a.lineNumber,fileName:a.fileName,stack:a.stack}}
function Cd(a,b){b||(b={});b[Ed(a)]=!0;var c=a.stack||"";(a=a.Ja)&&!b[Ed(a)]&&(c+="\nCaused by: ",a.stack&&0==a.stack.indexOf(a.toString())||(c+="string"===typeof a?a:a.message+"\n"),c+=Cd(a,b));return c}
function Ed(a){var b="";"function"===typeof a.toString&&(b=""+a);return b+a.stack}
var Dd={};function Fd(a){a&&"function"==typeof a.dispose&&a.dispose()}
;function Gd(a){for(var b=0,c=arguments.length;b<c;++b){var d=arguments[b];Na(d)?Gd.apply(null,d):Fd(d)}}
;function L(){this.h=this.h;this.u=this.u}
L.prototype.h=!1;L.prototype.dispose=function(){this.h||(this.h=!0,this.D())};
function Hd(a,b){a.h?b():(a.u||(a.u=[]),a.u.push(b))}
L.prototype.D=function(){if(this.u)for(;this.u.length;)this.u.shift()()};function Id(a){return"string"==typeof a.className?a.className:a.getAttribute&&a.getAttribute("class")||""}
function Jd(a,b){"string"==typeof a.className?a.className=b:a.setAttribute&&a.setAttribute("class",b)}
function Kd(a,b){a.classList?b=a.classList.contains(b):(a=a.classList?a.classList:Id(a).match(/\S+/g)||[],b=0<=$a(a,b));return b}
function Ld(){var a=document.body;a.classList?a.classList.remove("inverted-hdpi"):Kd(a,"inverted-hdpi")&&Jd(a,ab(a.classList?a.classList:Id(a).match(/\S+/g)||[],function(b){return"inverted-hdpi"!=b}).join(" "))}
;var Md="StopIteration"in y?y.StopIteration:{message:"StopIteration",stack:""};function Nd(){}
Nd.prototype.next=function(){throw Md;};
Nd.prototype.N=function(){return this};
function Od(a){if(a instanceof Nd)return a;if("function"==typeof a.N)return a.N(!1);if(Na(a)){var b=0,c=new Nd;c.next=function(){for(;;){if(b>=a.length)throw Md;if(b in a)return a[b++];b++}};
return c}throw Error("Not implemented");}
function Pd(a,b){if(Na(a))try{E(a,b,void 0)}catch(c){if(c!==Md)throw c;}else{a=Od(a);try{for(;;)b.call(void 0,a.next(),void 0,a)}catch(c){if(c!==Md)throw c;}}}
function Qd(a){if(Na(a))return fb(a);a=Od(a);var b=[];Pd(a,function(c){b.push(c)});
return b}
;function Rd(a,b){this.i={};this.h=[];this.P=this.j=0;var c=arguments.length;if(1<c){if(c%2)throw Error("Uneven number of arguments");for(var d=0;d<c;d+=2)this.set(arguments[d],arguments[d+1])}else if(a)if(a instanceof Rd)for(c=Sd(a),d=0;d<c.length;d++)this.set(c[d],a.get(c[d]));else for(d in a)this.set(d,a[d])}
function Sd(a){Td(a);return a.h.concat()}
m=Rd.prototype;m.equals=function(a,b){if(this===a)return!0;if(this.j!=a.j)return!1;b=b||Ud;Td(this);for(var c,d=0;c=this.h[d];d++)if(!b(this.get(c),a.get(c)))return!1;return!0};
function Ud(a,b){return a===b}
m.isEmpty=function(){return 0==this.j};
m.clear=function(){this.i={};this.P=this.j=this.h.length=0};
m.remove=function(a){return Object.prototype.hasOwnProperty.call(this.i,a)?(delete this.i[a],this.j--,this.P++,this.h.length>2*this.j&&Td(this),!0):!1};
function Td(a){if(a.j!=a.h.length){for(var b=0,c=0;b<a.h.length;){var d=a.h[b];Object.prototype.hasOwnProperty.call(a.i,d)&&(a.h[c++]=d);b++}a.h.length=c}if(a.j!=a.h.length){var e={};for(c=b=0;b<a.h.length;)d=a.h[b],Object.prototype.hasOwnProperty.call(e,d)||(a.h[c++]=d,e[d]=1),b++;a.h.length=c}}
m.get=function(a,b){return Object.prototype.hasOwnProperty.call(this.i,a)?this.i[a]:b};
m.set=function(a,b){Object.prototype.hasOwnProperty.call(this.i,a)||(this.j++,this.h.push(a),this.P++);this.i[a]=b};
m.forEach=function(a,b){for(var c=Sd(this),d=0;d<c.length;d++){var e=c[d],f=this.get(e);a.call(b,f,e,this)}};
m.clone=function(){return new Rd(this)};
m.N=function(a){Td(this);var b=0,c=this.P,d=this,e=new Nd;e.next=function(){if(c!=d.P)throw Error("The map has changed since the iterator was created");if(b>=d.h.length)throw Md;var f=d.h[b++];return a?f:d.i[f]};
return e};var Vd=function(){if(!y.addEventListener||!Object.defineProperty)return!1;var a=!1,b=Object.defineProperty({},"passive",{get:function(){a=!0}});
try{y.addEventListener("test",Ka,b),y.removeEventListener("test",Ka,b)}catch(c){}return a}();function Wd(a,b){this.type=a;this.h=this.target=b;this.defaultPrevented=this.j=!1}
Wd.prototype.stopPropagation=function(){this.j=!0};
Wd.prototype.preventDefault=function(){this.defaultPrevented=!0};function Xd(a,b){Wd.call(this,a?a.type:"");this.relatedTarget=this.h=this.target=null;this.button=this.screenY=this.screenX=this.clientY=this.clientX=0;this.key="";this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.altKey=this.ctrlKey=!1;this.state=null;this.pointerId=0;this.pointerType="";this.i=null;a&&this.init(a,b)}
D(Xd,Wd);var Yd={2:"touch",3:"pen",4:"mouse"};
Xd.prototype.init=function(a,b){var c=this.type=a.type,d=a.changedTouches&&a.changedTouches.length?a.changedTouches[0]:null;this.target=a.target||a.srcElement;this.h=b;if(b=a.relatedTarget){if(oc){a:{try{kc(b.nodeName);var e=!0;break a}catch(f){}e=!1}e||(b=null)}}else"mouseover"==c?b=a.fromElement:"mouseout"==c&&(b=a.toElement);this.relatedTarget=b;d?(this.clientX=void 0!==d.clientX?d.clientX:d.pageX,this.clientY=void 0!==d.clientY?d.clientY:d.pageY,this.screenX=d.screenX||0,this.screenY=d.screenY||
0):(this.clientX=void 0!==a.clientX?a.clientX:a.pageX,this.clientY=void 0!==a.clientY?a.clientY:a.pageY,this.screenX=a.screenX||0,this.screenY=a.screenY||0);this.button=a.button;this.keyCode=a.keyCode||0;this.key=a.key||"";this.charCode=a.charCode||("keypress"==c?a.keyCode:0);this.ctrlKey=a.ctrlKey;this.altKey=a.altKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.pointerId=a.pointerId||0;this.pointerType="string"===typeof a.pointerType?a.pointerType:Yd[a.pointerType]||"";this.state=a.state;
this.i=a;a.defaultPrevented&&Xd.L.preventDefault.call(this)};
Xd.prototype.stopPropagation=function(){Xd.L.stopPropagation.call(this);this.i.stopPropagation?this.i.stopPropagation():this.i.cancelBubble=!0};
Xd.prototype.preventDefault=function(){Xd.L.preventDefault.call(this);var a=this.i;a.preventDefault?a.preventDefault():a.returnValue=!1};var Zd="closure_listenable_"+(1E6*Math.random()|0);var $d=0;function ae(a,b,c,d,e){this.listener=a;this.h=null;this.src=b;this.type=c;this.capture=!!d;this.fa=e;this.key=++$d;this.Z=this.ca=!1}
function be(a){a.Z=!0;a.listener=null;a.h=null;a.src=null;a.fa=null}
;function ce(a){this.src=a;this.listeners={};this.h=0}
ce.prototype.add=function(a,b,c,d,e){var f=a.toString();a=this.listeners[f];a||(a=this.listeners[f]=[],this.h++);var g=de(a,b,d,e);-1<g?(b=a[g],c||(b.ca=!1)):(b=new ae(b,this.src,f,!!d,e),b.ca=c,a.push(b));return b};
ce.prototype.remove=function(a,b,c,d){a=a.toString();if(!(a in this.listeners))return!1;var e=this.listeners[a];b=de(e,b,c,d);return-1<b?(be(e[b]),Array.prototype.splice.call(e,b,1),0==e.length&&(delete this.listeners[a],this.h--),!0):!1};
function ee(a,b){var c=b.type;c in a.listeners&&eb(a.listeners[c],b)&&(be(b),0==a.listeners[c].length&&(delete a.listeners[c],a.h--))}
function de(a,b,c,d){for(var e=0;e<a.length;++e){var f=a[e];if(!f.Z&&f.listener==b&&f.capture==!!c&&f.fa==d)return e}return-1}
;var fe="closure_lm_"+(1E6*Math.random()|0),ge={},he=0;function ie(a,b,c,d,e){if(d&&d.once)je(a,b,c,d,e);else if(Array.isArray(b))for(var f=0;f<b.length;f++)ie(a,b[f],c,d,e);else c=ke(c),a&&a[Zd]?le(a,b,c,Oa(d)?!!d.capture:!!d,e):me(a,b,c,!1,d,e)}
function me(a,b,c,d,e,f){if(!b)throw Error("Invalid event type");var g=Oa(e)?!!e.capture:!!e,h=ne(a);h||(a[fe]=h=new ce(a));c=h.add(b,c,d,g,f);if(!c.h){d=oe();c.h=d;d.src=a;d.listener=c;if(a.addEventListener)Vd||(e=g),void 0===e&&(e=!1),a.addEventListener(b.toString(),d,e);else if(a.attachEvent)a.attachEvent(pe(b.toString()),d);else if(a.addListener&&a.removeListener)a.addListener(d);else throw Error("addEventListener and attachEvent are unavailable.");he++}}
function oe(){function a(c){return b.call(a.src,a.listener,c)}
var b=qe;return a}
function je(a,b,c,d,e){if(Array.isArray(b))for(var f=0;f<b.length;f++)je(a,b[f],c,d,e);else c=ke(c),a&&a[Zd]?a.i.add(String(b),c,!0,Oa(d)?!!d.capture:!!d,e):me(a,b,c,!0,d,e)}
function re(a,b,c,d,e){if(Array.isArray(b))for(var f=0;f<b.length;f++)re(a,b[f],c,d,e);else(d=Oa(d)?!!d.capture:!!d,c=ke(c),a&&a[Zd])?a.i.remove(String(b),c,d,e):a&&(a=ne(a))&&(b=a.listeners[b.toString()],a=-1,b&&(a=de(b,c,d,e)),(c=-1<a?b[a]:null)&&se(c))}
function se(a){if("number"!==typeof a&&a&&!a.Z){var b=a.src;if(b&&b[Zd])ee(b.i,a);else{var c=a.type,d=a.h;b.removeEventListener?b.removeEventListener(c,d,a.capture):b.detachEvent?b.detachEvent(pe(c),d):b.addListener&&b.removeListener&&b.removeListener(d);he--;(c=ne(b))?(ee(c,a),0==c.h&&(c.src=null,b[fe]=null)):be(a)}}}
function pe(a){return a in ge?ge[a]:ge[a]="on"+a}
function qe(a,b){if(a.Z)a=!0;else{b=new Xd(b,this);var c=a.listener,d=a.fa||a.src;a.ca&&se(a);a=c.call(d,b)}return a}
function ne(a){a=a[fe];return a instanceof ce?a:null}
var te="__closure_events_fn_"+(1E9*Math.random()>>>0);function ke(a){if("function"===typeof a)return a;a[te]||(a[te]=function(b){return a.handleEvent(b)});
return a[te]}
;function ue(){L.call(this);this.i=new ce(this);this.K=this;this.A=null}
D(ue,L);ue.prototype[Zd]=!0;ue.prototype.addEventListener=function(a,b,c,d){ie(this,a,b,c,d)};
ue.prototype.removeEventListener=function(a,b,c,d){re(this,a,b,c,d)};
function ve(a,b){var c=a.A;if(c){var d=[];for(var e=1;c;c=c.A)d.push(c),++e}a=a.K;c=b.type||b;"string"===typeof b?b=new Wd(b,a):b instanceof Wd?b.target=b.target||a:(e=b,b=new Wd(c,a),sb(b,e));e=!0;if(d)for(var f=d.length-1;!b.j&&0<=f;f--){var g=b.h=d[f];e=we(g,c,!0,b)&&e}b.j||(g=b.h=a,e=we(g,c,!0,b)&&e,b.j||(e=we(g,c,!1,b)&&e));if(d)for(f=0;!b.j&&f<d.length;f++)g=b.h=d[f],e=we(g,c,!1,b)&&e}
ue.prototype.D=function(){ue.L.D.call(this);if(this.i){var a=this.i,b=0,c;for(c in a.listeners){for(var d=a.listeners[c],e=0;e<d.length;e++)++b,be(d[e]);delete a.listeners[c];a.h--}}this.A=null};
function le(a,b,c,d,e){a.i.add(String(b),c,!1,d,e)}
function we(a,b,c,d){b=a.i.listeners[String(b)];if(!b)return!0;b=b.concat();for(var e=!0,f=0;f<b.length;++f){var g=b[f];if(g&&!g.Z&&g.capture==c){var h=g.listener,k=g.fa||g.src;g.ca&&ee(a.i,g);e=!1!==h.call(k,d)&&e}}return e&&!d.defaultPrevented}
;function xe(a){var b=[];ye(new ze,a,b);return b.join("")}
function ze(){}
function ye(a,b,c){if(null==b)c.push("null");else{if("object"==typeof b){if(Array.isArray(b)){var d=b;b=d.length;c.push("[");for(var e="",f=0;f<b;f++)c.push(e),ye(a,d[f],c),e=",";c.push("]");return}if(b instanceof String||b instanceof Number||b instanceof Boolean)b=b.valueOf();else{c.push("{");e="";for(d in b)Object.prototype.hasOwnProperty.call(b,d)&&(f=b[d],"function"!=typeof f&&(c.push(e),Ae(d,c),c.push(":"),ye(a,f,c),e=","));c.push("}");return}}switch(typeof b){case "string":Ae(b,c);break;case "number":c.push(isFinite(b)&&
!isNaN(b)?String(b):"null");break;case "boolean":c.push(String(b));break;case "function":c.push("null");break;default:throw Error("Unknown type: "+typeof b);}}}
var Be={'"':'\\"',"\\":"\\\\","/":"\\/","\b":"\\b","\f":"\\f","\n":"\\n","\r":"\\r","\t":"\\t","\x0B":"\\u000b"},Ce=/\uffff/.test("\uffff")?/[\\"\x00-\x1f\x7f-\uffff]/g:/[\\"\x00-\x1f\x7f-\xff]/g;function Ae(a,b){b.push('"',a.replace(Ce,function(c){var d=Be[c];d||(d="\\u"+(c.charCodeAt(0)|65536).toString(16).substr(1),Be[c]=d);return d}),'"')}
;function De(a){if(!a)return!1;try{return!!a.$goog_Thenable}catch(b){return!1}}
;function Ee(a){this.h=0;this.o=void 0;this.l=this.i=this.j=null;this.u=this.m=!1;if(a!=Ka)try{var b=this;a.call(void 0,function(c){Fe(b,2,c)},function(c){Fe(b,3,c)})}catch(c){Fe(this,3,c)}}
function Ge(){this.next=this.context=this.onRejected=this.i=this.h=null;this.j=!1}
Ge.prototype.reset=function(){this.context=this.onRejected=this.i=this.h=null;this.j=!1};
var He=new kd(function(){return new Ge},function(a){a.reset()});
function Ie(a,b,c){var d=He.get();d.i=a;d.onRejected=b;d.context=c;return d}
function Je(a){return new Ee(function(b,c){c(a)})}
Ee.prototype.then=function(a,b,c){return Ke(this,"function"===typeof a?a:null,"function"===typeof b?b:null,c)};
Ee.prototype.$goog_Thenable=!0;function Le(a,b){return Ke(a,null,b,void 0)}
Ee.prototype.cancel=function(a){if(0==this.h){var b=new Me(a);sd(function(){Ne(this,b)},this)}};
function Ne(a,b){if(0==a.h)if(a.j){var c=a.j;if(c.i){for(var d=0,e=null,f=null,g=c.i;g&&(g.j||(d++,g.h==a&&(e=g),!(e&&1<d)));g=g.next)e||(f=g);e&&(0==c.h&&1==d?Ne(c,b):(f?(d=f,d.next==c.l&&(c.l=d),d.next=d.next.next):Oe(c),Pe(c,e,3,b)))}a.j=null}else Fe(a,3,b)}
function Qe(a,b){a.i||2!=a.h&&3!=a.h||Re(a);a.l?a.l.next=b:a.i=b;a.l=b}
function Ke(a,b,c,d){var e=Ie(null,null,null);e.h=new Ee(function(f,g){e.i=b?function(h){try{var k=b.call(d,h);f(k)}catch(l){g(l)}}:f;
e.onRejected=c?function(h){try{var k=c.call(d,h);void 0===k&&h instanceof Me?g(h):f(k)}catch(l){g(l)}}:g});
e.h.j=a;Qe(a,e);return e.h}
Ee.prototype.C=function(a){this.h=0;Fe(this,2,a)};
Ee.prototype.G=function(a){this.h=0;Fe(this,3,a)};
function Fe(a,b,c){if(0==a.h){a===c&&(b=3,c=new TypeError("Promise cannot resolve to itself"));a.h=1;a:{var d=c,e=a.C,f=a.G;if(d instanceof Ee){Qe(d,Ie(e||Ka,f||null,a));var g=!0}else if(De(d))d.then(e,f,a),g=!0;else{if(Oa(d))try{var h=d.then;if("function"===typeof h){Se(d,h,e,f,a);g=!0;break a}}catch(k){f.call(a,k);g=!0;break a}g=!1}}g||(a.o=c,a.h=b,a.j=null,Re(a),3!=b||c instanceof Me||Te(a,c))}}
function Se(a,b,c,d,e){function f(k){h||(h=!0,d.call(e,k))}
function g(k){h||(h=!0,c.call(e,k))}
var h=!1;try{b.call(a,g,f)}catch(k){f(k)}}
function Re(a){a.m||(a.m=!0,sd(a.A,a))}
function Oe(a){var b=null;a.i&&(b=a.i,a.i=b.next,b.next=null);a.i||(a.l=null);return b}
Ee.prototype.A=function(){for(var a;a=Oe(this);)Pe(this,a,this.h,this.o);this.m=!1};
function Pe(a,b,c,d){if(3==c&&b.onRejected&&!b.j)for(;a&&a.u;a=a.j)a.u=!1;if(b.h)b.h.j=null,Ue(b,c,d);else try{b.j?b.i.call(b.context):Ue(b,c,d)}catch(e){Ve.call(null,e)}ld(He,b)}
function Ue(a,b,c){2==b?a.i.call(a.context,c):a.onRejected&&a.onRejected.call(a.context,c)}
function Te(a,b){a.u=!0;sd(function(){a.u&&Ve.call(null,b)})}
var Ve=od;function Me(a){Xa.call(this,a)}
D(Me,Xa);Me.prototype.name="cancel";function M(a){L.call(this);this.o=1;this.l=[];this.m=0;this.i=[];this.j={};this.A=!!a}
D(M,L);m=M.prototype;m.subscribe=function(a,b,c){var d=this.j[a];d||(d=this.j[a]=[]);var e=this.o;this.i[e]=a;this.i[e+1]=b;this.i[e+2]=c;this.o=e+3;d.push(e);return e};
function We(a,b,c,d){if(b=a.j[b]){var e=a.i;(b=db(b,function(f){return e[f+1]==c&&e[f+2]==d}))&&a.Y(b)}}
m.Y=function(a){var b=this.i[a];if(b){var c=this.j[b];0!=this.m?(this.l.push(a),this.i[a+1]=Ka):(c&&eb(c,a),delete this.i[a],delete this.i[a+1],delete this.i[a+2])}return!!b};
m.R=function(a,b){var c=this.j[a];if(c){for(var d=Array(arguments.length-1),e=1,f=arguments.length;e<f;e++)d[e-1]=arguments[e];if(this.A)for(e=0;e<c.length;e++){var g=c[e];Xe(this.i[g+1],this.i[g+2],d)}else{this.m++;try{for(e=0,f=c.length;e<f;e++)g=c[e],this.i[g+1].apply(this.i[g+2],d)}finally{if(this.m--,0<this.l.length&&0==this.m)for(;c=this.l.pop();)this.Y(c)}}return 0!=e}return!1};
function Xe(a,b,c){sd(function(){a.apply(b,c)})}
m.clear=function(a){if(a){var b=this.j[a];b&&(E(b,this.Y,this),delete this.j[a])}else this.i.length=0,this.j={}};
m.D=function(){M.L.D.call(this);this.clear();this.l.length=0};function Ye(a){this.h=a}
Ye.prototype.set=function(a,b){void 0===b?this.h.remove(a):this.h.set(a,xe(b))};
Ye.prototype.get=function(a){try{var b=this.h.get(a)}catch(c){return}if(null!==b)try{return JSON.parse(b)}catch(c){throw"Storage: Invalid value was encountered";}};
Ye.prototype.remove=function(a){this.h.remove(a)};function Ze(a){this.h=a}
D(Ze,Ye);function $e(a){this.data=a}
function af(a){return void 0===a||a instanceof $e?a:new $e(a)}
Ze.prototype.set=function(a,b){Ze.L.set.call(this,a,af(b))};
Ze.prototype.i=function(a){a=Ze.L.get.call(this,a);if(void 0===a||a instanceof Object)return a;throw"Storage: Invalid value was encountered";};
Ze.prototype.get=function(a){if(a=this.i(a)){if(a=a.data,void 0===a)throw"Storage: Invalid value was encountered";}else a=void 0;return a};function bf(a){this.h=a}
D(bf,Ze);bf.prototype.set=function(a,b,c){if(b=af(b)){if(c){if(c<Date.now()){bf.prototype.remove.call(this,a);return}b.expiration=c}b.creation=Date.now()}bf.L.set.call(this,a,b)};
bf.prototype.i=function(a){var b=bf.L.i.call(this,a);if(b){var c=b.creation,d=b.expiration;if(d&&d<Date.now()||c&&c>Date.now())bf.prototype.remove.call(this,a);else return b}};function cf(){}
;function df(){}
D(df,cf);df.prototype.clear=function(){var a=Qd(this.N(!0)),b=this;E(a,function(c){b.remove(c)})};function ef(a){this.h=a}
D(ef,df);m=ef.prototype;m.isAvailable=function(){if(!this.h)return!1;try{return this.h.setItem("__sak","1"),this.h.removeItem("__sak"),!0}catch(a){return!1}};
m.set=function(a,b){try{this.h.setItem(a,b)}catch(c){if(0==this.h.length)throw"Storage mechanism: Storage disabled";throw"Storage mechanism: Quota exceeded";}};
m.get=function(a){a=this.h.getItem(a);if("string"!==typeof a&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
m.remove=function(a){this.h.removeItem(a)};
m.N=function(a){var b=0,c=this.h,d=new Nd;d.next=function(){if(b>=c.length)throw Md;var e=c.key(b++);if(a)return e;e=c.getItem(e);if("string"!==typeof e)throw"Storage mechanism: Invalid value was encountered";return e};
return d};
m.clear=function(){this.h.clear()};
m.key=function(a){return this.h.key(a)};function ff(){var a=null;try{a=window.localStorage||null}catch(b){}this.h=a}
D(ff,ef);function gf(a,b){this.i=a;this.h=null;if(mc&&!(9<=Number(yc))){hf||(hf=new Rd);this.h=hf.get(a);this.h||(b?this.h=document.getElementById(b):(this.h=document.createElement("userdata"),this.h.addBehavior("#default#userData"),document.body.appendChild(this.h)),hf.set(a,this.h));try{this.h.load(this.i)}catch(c){this.h=null}}}
D(gf,df);var jf={".":".2E","!":".21","~":".7E","*":".2A","'":".27","(":".28",")":".29","%":"."},hf=null;function kf(a){return"_"+encodeURIComponent(a).replace(/[.!~*'()%]/g,function(b){return jf[b]})}
m=gf.prototype;m.isAvailable=function(){return!!this.h};
m.set=function(a,b){this.h.setAttribute(kf(a),b);lf(this)};
m.get=function(a){a=this.h.getAttribute(kf(a));if("string"!==typeof a&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
m.remove=function(a){this.h.removeAttribute(kf(a));lf(this)};
m.N=function(a){var b=0,c=this.h.XMLDocument.documentElement.attributes,d=new Nd;d.next=function(){if(b>=c.length)throw Md;var e=c[b++];if(a)return decodeURIComponent(e.nodeName.replace(/\./g,"%")).substr(1);e=e.nodeValue;if("string"!==typeof e)throw"Storage mechanism: Invalid value was encountered";return e};
return d};
m.clear=function(){for(var a=this.h.XMLDocument.documentElement,b=a.attributes.length;0<b;b--)a.removeAttribute(a.attributes[b-1].nodeName);lf(this)};
function lf(a){try{a.h.save(a.i)}catch(b){throw"Storage mechanism: Quota exceeded";}}
;function mf(a,b){this.i=a;this.h=b+"::"}
D(mf,df);mf.prototype.set=function(a,b){this.i.set(this.h+a,b)};
mf.prototype.get=function(a){return this.i.get(this.h+a)};
mf.prototype.remove=function(a){this.i.remove(this.h+a)};
mf.prototype.N=function(a){var b=this.i.N(!0),c=this,d=new Nd;d.next=function(){for(var e=b.next();e.substr(0,c.h.length)!=c.h;)e=b.next();return a?e.substr(c.h.length):c.i.get(e)};
return d};function nf(a,b){1<b.length?a[b[0]]=b[1]:1===b.length&&Object.assign(a,b[0])}
;var of=window.yt&&window.yt.config_||window.ytcfg&&window.ytcfg.data_||{};z("yt.config_",of,void 0);function N(a){nf(of,arguments)}
function F(a,b){return a in of?of[a]:b}
;var pf=[];function qf(a){pf.forEach(function(b){return b(a)})}
function rf(a){return a&&window.yterr?function(){try{return a.apply(this,arguments)}catch(b){sf(b)}}:a}
function sf(a){var b=A("yt.logging.errors.log");b?b(a,"ERROR",void 0,void 0,void 0):(b=F("ERRORS",[]),b.push([a,"ERROR",void 0,void 0,void 0]),N("ERRORS",b));qf(a)}
function tf(a){var b=A("yt.logging.errors.log");b?b(a,"WARNING",void 0,void 0,void 0):(b=F("ERRORS",[]),b.push([a,"WARNING",void 0,void 0,void 0]),N("ERRORS",b))}
;var uf=window.yt&&window.yt.msgs_||window.ytcfg&&window.ytcfg.msgs||{};z("yt.msgs_",uf,void 0);function vf(a){nf(uf,arguments)}
;function Q(a){a=wf(a);return"string"===typeof a&&"false"===a?!1:!!a}
function xf(a,b){a=wf(a);return void 0===a&&void 0!==b?b:Number(a||0)}
function wf(a){var b=F("EXPERIMENTS_FORCED_FLAGS",{});return void 0!==b[a]?b[a]:F("EXPERIMENT_FLAGS",{})[a]}
;var yf=0,zf=pc?"webkit":oc?"moz":mc?"ms":lc?"o":"";z("ytDomDomGetNextId",A("ytDomDomGetNextId")||function(){return++yf},void 0);var Af={stopImmediatePropagation:1,stopPropagation:1,preventMouseEvent:1,preventManipulation:1,preventDefault:1,layerX:1,layerY:1,screenX:1,screenY:1,scale:1,rotation:1,webkitMovementX:1,webkitMovementY:1};
function Bf(a){this.type="";this.state=this.source=this.data=this.currentTarget=this.relatedTarget=this.target=null;this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.ctrlKey=this.altKey=!1;this.clientY=this.clientX=0;this.changedTouches=this.touches=null;try{if(a=a||window.event){this.event=a;for(var b in a)b in Af||(this[b]=a[b]);var c=a.target||a.srcElement;c&&3==c.nodeType&&(c=c.parentNode);this.target=c;var d=a.relatedTarget;if(d)try{d=d.nodeName?d:null}catch(e){d=null}else"mouseover"==
this.type?d=a.fromElement:"mouseout"==this.type&&(d=a.toElement);this.relatedTarget=d;this.clientX=void 0!=a.clientX?a.clientX:a.pageX;this.clientY=void 0!=a.clientY?a.clientY:a.pageY;this.keyCode=a.keyCode?a.keyCode:a.which;this.charCode=a.charCode||("keypress"==this.type?this.keyCode:0);this.altKey=a.altKey;this.ctrlKey=a.ctrlKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.h=a.pageX;this.i=a.pageY}}catch(e){}}
function Cf(a){if(document.body&&document.documentElement){var b=document.body.scrollTop+document.documentElement.scrollTop;a.h=a.clientX+(document.body.scrollLeft+document.documentElement.scrollLeft);a.i=a.clientY+b}}
Bf.prototype.preventDefault=function(){this.event&&(this.event.returnValue=!1,this.event.preventDefault&&this.event.preventDefault())};
Bf.prototype.stopPropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopPropagation&&this.event.stopPropagation())};
Bf.prototype.stopImmediatePropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopImmediatePropagation&&this.event.stopImmediatePropagation())};var jb=y.ytEventsEventsListeners||{};z("ytEventsEventsListeners",jb,void 0);var Df=y.ytEventsEventsCounter||{count:0};z("ytEventsEventsCounter",Df,void 0);
function Ef(a,b,c,d){d=void 0===d?{}:d;a.addEventListener&&("mouseenter"!=b||"onmouseenter"in document?"mouseleave"!=b||"onmouseenter"in document?"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"):b="mouseout":b="mouseover");return ib(function(e){var f="boolean"===typeof e[4]&&e[4]==!!d,g=Oa(e[4])&&Oa(d)&&ob(e[4],d);return!!e.length&&e[0]==a&&e[1]==b&&e[2]==c&&(f||g)})}
var Ff=Za(function(){var a=!1;try{var b=Object.defineProperty({},"capture",{get:function(){a=!0}});
window.addEventListener("test",null,b)}catch(c){}return a});
function Gf(a,b,c,d){d=void 0===d?{}:d;if(!a||!a.addEventListener&&!a.attachEvent)return"";var e=Ef(a,b,c,d);if(e)return e;e=++Df.count+"";var f=!("mouseenter"!=b&&"mouseleave"!=b||!a.addEventListener||"onmouseenter"in document);var g=f?function(h){h=new Bf(h);if(!Oc(h.relatedTarget,function(k){return k==a}))return h.currentTarget=a,h.type=b,c.call(a,h)}:function(h){h=new Bf(h);
h.currentTarget=a;return c.call(a,h)};
g=rf(g);a.addEventListener?("mouseenter"==b&&f?b="mouseover":"mouseleave"==b&&f?b="mouseout":"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"),Ff()||"boolean"===typeof d?a.addEventListener(b,g,d):a.addEventListener(b,g,!!d.capture)):a.attachEvent("on"+b,g);jb[e]=[a,b,c,g,d];return e}
function Hf(a){a&&("string"==typeof a&&(a=[a]),E(a,function(b){if(b in jb){var c=jb[b],d=c[0],e=c[1],f=c[3];c=c[4];d.removeEventListener?Ff()||"boolean"===typeof c?d.removeEventListener(e,f,c):d.removeEventListener(e,f,!!c.capture):d.detachEvent&&d.detachEvent("on"+e,f);delete jb[b]}}))}
;var If=window.ytcsi&&window.ytcsi.now?window.ytcsi.now:window.performance&&window.performance.timing&&window.performance.now&&window.performance.timing.navigationStart?function(){return window.performance.timing.navigationStart+window.performance.now()}:function(){return(new Date).getTime()};function Jf(a,b){"function"===typeof a&&(a=rf(a));return window.setTimeout(a,b)}
function Kf(a){window.clearTimeout(a)}
;function Lf(a){this.C=a;this.i=null;this.m=0;this.A=null;this.o=0;this.j=[];for(a=0;4>a;a++)this.j.push(0);this.l=0;this.J=Gf(window,"mousemove",C(this.K,this));a=C(this.G,this);"function"===typeof a&&(a=rf(a));this.M=window.setInterval(a,25)}
D(Lf,L);Lf.prototype.K=function(a){void 0===a.h&&Cf(a);var b=a.h;void 0===a.i&&Cf(a);this.i=new Gc(b,a.i)};
Lf.prototype.G=function(){if(this.i){var a=If();if(0!=this.m){var b=this.A,c=this.i,d=b.x-c.x;b=b.y-c.y;d=Math.sqrt(d*d+b*b)/(a-this.m);this.j[this.l]=.5<Math.abs((d-this.o)/this.o)?1:0;for(c=b=0;4>c;c++)b+=this.j[c]||0;3<=b&&this.C();this.o=d}this.m=a;this.A=this.i;this.l=(this.l+1)%4}};
Lf.prototype.D=function(){window.clearInterval(this.M);Hf(this.J)};function Mf(){}
function Nf(a,b){return Of(a,0,b)}
function Pf(a,b){return Of(a,1,b)}
function Qf(a,b){Of(a,2,b)}
;function Rf(){Mf.apply(this,arguments)}
var Sf;v(Rf,Mf);function Of(a,b,c){void 0!==c&&Number.isNaN(Number(c))&&(c=void 0);var d=A("yt.scheduler.instance.addJob");return d?d(a,b,c):void 0===c?(a(),NaN):Jf(a,c||0)}
function Tf(a){if(void 0===a||!Number.isNaN(Number(a))){var b=A("yt.scheduler.instance.cancelJob");b?b(a):Kf(a)}}
Rf.prototype.start=function(){var a=A("yt.scheduler.instance.start");a&&a()};
Rf.prototype.pause=function(){var a=A("yt.scheduler.instance.pause");a&&a()};Sf||(Sf=new Rf);var Uf={};
function Vf(a){var b=void 0===a?{}:a;a=void 0===b.Na?!0:b.Na;b=void 0===b.ab?!1:b.ab;if(null==A("_lact",window)){var c=parseInt(F("LACT"),10);c=isFinite(c)?Date.now()-Math.max(c,0):-1;z("_lact",c,window);z("_fact",c,window);-1==c&&Wf();Gf(document,"keydown",Wf);Gf(document,"keyup",Wf);Gf(document,"mousedown",Wf);Gf(document,"mouseup",Wf);a&&(b?Gf(window,"touchmove",function(){Xf("touchmove",200)},{passive:!0}):(Gf(window,"resize",function(){Xf("resize",200)}),Gf(window,"scroll",function(){Xf("scroll",200)})));
new Lf(function(){Xf("mouse",100)});
Gf(document,"touchstart",Wf,{passive:!0});Gf(document,"touchend",Wf,{passive:!0})}}
function Xf(a,b){Uf[a]||(Uf[a]=!0,Pf(function(){Wf();Uf[a]=!1},b))}
function Wf(){null==A("_lact",window)&&Vf();var a=Date.now();z("_lact",a,window);-1==A("_fact",window)&&z("_fact",a,window);(a=A("ytglobal.ytUtilActivityCallback_"))&&a()}
function Yf(){var a=A("_lact",window);return null==a?-1:Math.max(Date.now()-a,0)}
;function Zf(){var a=$f;A("yt.ads.biscotti.getId_")||z("yt.ads.biscotti.getId_",a,void 0)}
function ag(a){z("yt.ads.biscotti.lastId_",a,void 0)}
;var bg=/^[\w.]*$/,cg={q:!0,search_query:!0};function dg(a,b){b=a.split(b);for(var c={},d=0,e=b.length;d<e;d++){var f=b[d].split("=");if(1==f.length&&f[0]||2==f.length)try{var g=eg(f[0]||""),h=eg(f[1]||"");g in c?Array.isArray(c[g])?gb(c[g],h):c[g]=[c[g],h]:c[g]=h}catch(n){var k=n,l=f[0],p=String(dg);k.args=[{key:l,value:f[1],query:a,method:fg==p?"unchanged":p}];cg.hasOwnProperty(l)||tf(k)}}return c}
var fg=String(dg);function gg(a){var b=[];hb(a,function(c,d){var e=encodeURIComponent(String(d)),f;Array.isArray(c)?f=c:f=[c];E(f,function(g){""==g?b.push(e):b.push(e+"="+encodeURIComponent(String(g)))})});
return b.join("&")}
function hg(a){"?"==a.charAt(0)&&(a=a.substr(1));return dg(a,"&")}
function ig(){var a=window.location.href;return-1!=a.indexOf("?")?(a=(a||"").split("#")[0],a=a.split("?",2),hg(1<a.length?a[1]:a[0])):{}}
function jg(a,b,c){var d=a.split("#",2);a=d[0];d=1<d.length?"#"+d[1]:"";var e=a.split("?",2);a=e[0];e=hg(e[1]||"");for(var f in b)!c&&null!==e&&f in e||(e[f]=b[f]);return hc(a,e)+d}
function kg(a){if(!b)var b=window.location.href;var c=a.match(cc)[1]||null,d=ec(a);c&&d?(a=a.match(cc),b=b.match(cc),a=a[3]==b[3]&&a[1]==b[1]&&a[4]==b[4]):a=d?ec(b)==d&&(Number(b.match(cc)[4]||null)||null)==(Number(a.match(cc)[4]||null)||null):!0;return a}
function eg(a){return a&&a.match(bg)?a:decodeURIComponent(a.replace(/\+/g," "))}
;function lg(a){var b=mg;a=void 0===a?A("yt.ads.biscotti.lastId_")||"":a;var c=Object,d=c.assign,e={};e.dt=Xc;e.flash="0";a:{try{var f=b.h.top.location.href}catch(P){f=2;break a}f=f?f===b.i.location.href?0:1:2}e=(e.frm=f,e);e.u_tz=-(new Date).getTimezoneOffset();var g=void 0===g?K:g;try{var h=g.history.length}catch(P){h=0}e.u_his=h;e.u_java=!!K.navigator&&"unknown"!==typeof K.navigator.javaEnabled&&!!K.navigator.javaEnabled&&K.navigator.javaEnabled();K.screen&&(e.u_h=K.screen.height,e.u_w=K.screen.width,
e.u_ah=K.screen.availHeight,e.u_aw=K.screen.availWidth,e.u_cd=K.screen.colorDepth);K.navigator&&K.navigator.plugins&&(e.u_nplug=K.navigator.plugins.length);K.navigator&&K.navigator.mimeTypes&&(e.u_nmime=K.navigator.mimeTypes.length);h=b.h;try{var k=h.screenX;var l=h.screenY}catch(P){}try{var p=h.outerWidth;var n=h.outerHeight}catch(P){}try{var r=h.innerWidth;var q=h.innerHeight}catch(P){}try{var B=h.screenLeft;var I=h.screenTop}catch(P){}try{r=h.innerWidth,q=h.innerHeight}catch(P){}try{var J=h.screen.availWidth;
var ba=h.screen.availTop}catch(P){}k=[B,I,k,l,J,ba,p,n,r,q];l=b.h.top;try{var U=(l||window).document,O="CSS1Compat"==U.compatMode?U.documentElement:U.body;var na=(new Hc(O.clientWidth,O.clientHeight)).round()}catch(P){na=new Hc(-12245933,-12245933)}U=na;na={};O=new id;y.SVGElement&&y.document.createElementNS&&O.set(0);l=Tc();l["allow-top-navigation-by-user-activation"]&&O.set(1);l["allow-popups-to-escape-sandbox"]&&O.set(2);y.crypto&&y.crypto.subtle&&O.set(3);y.TextDecoder&&y.TextEncoder&&O.set(4);
O=jd(O);na.bc=O;na.bih=U.height;na.biw=U.width;na.brdim=k.join();b=b.i;b=(na.vis={visible:1,hidden:2,prerender:3,preview:4,unloaded:5}[b.visibilityState||b.webkitVisibilityState||b.mozVisibilityState||""]||0,na.wgl=!!K.WebGLRenderingContext,na);c=d.call(c,e,b);c.ca_type="image";a&&(c.bid=a);return c}
var mg=new function(){var a=window.document;this.h=window;this.i=a};
z("yt.ads_.signals_.getAdSignalsString",function(a){return gg(lg(a))},void 0);var ng="XMLHttpRequest"in y?function(){return new XMLHttpRequest}:null;
function og(){if(!ng)return null;var a=ng();return"open"in a?a:null}
function pg(a){switch(a&&"status"in a?a.status:-1){case 200:case 201:case 202:case 203:case 204:case 205:case 206:case 304:return!0;default:return!1}}
;var qg={Authorization:"AUTHORIZATION","X-Goog-Visitor-Id":"SANDBOXED_VISITOR_ID","X-Youtube-Chrome-Connected":"CHROME_CONNECTED_HEADER","X-YouTube-Client-Name":"INNERTUBE_CONTEXT_CLIENT_NAME","X-YouTube-Client-Version":"INNERTUBE_CONTEXT_CLIENT_VERSION","X-YouTube-Delegation-Context":"INNERTUBE_CONTEXT_SERIALIZED_DELEGATION_CONTEXT","X-YouTube-Device":"DEVICE","X-Youtube-Identity-Token":"ID_TOKEN","X-YouTube-Page-CL":"PAGE_CL","X-YouTube-Page-Label":"PAGE_BUILD_LABEL","X-YouTube-Variants-Checksum":"VARIANTS_CHECKSUM"},
rg="app debugcss debugjs expflag force_ad_params force_ad_encrypted force_viral_ad_response_params forced_experiments innertube_snapshots innertube_goldens internalcountrycode internalipoverride absolute_experiments conditional_experiments sbb sr_bns_address client_dev_root_url".split(" "),sg=!1;
function tg(a,b){b=void 0===b?{}:b;var c=kg(a),d=Q("web_ajax_ignore_global_headers_if_set"),e;for(e in qg){var f=F(qg[e]);!f||!c&&ec(a)||d&&void 0!==b[e]||(b[e]=f)}if(c||!ec(a))b["X-YouTube-Utc-Offset"]=String(-(new Date).getTimezoneOffset());if(c||!ec(a)){try{var g=(new Intl.DateTimeFormat).resolvedOptions().timeZone}catch(h){}g&&(b["X-YouTube-Time-Zone"]=g)}if(c||!ec(a))b["X-YouTube-Ad-Signals"]=gg(lg(void 0));return b}
function ug(a){var b=window.location.search,c=ec(a);Q("debug_handle_relative_url_for_query_forward_killswitch")||c||!kg(a)||(c=document.location.hostname);var d=dc(a.match(cc)[5]||null);d=(c=c&&(c.endsWith("youtube.com")||c.endsWith("youtube-nocookie.com")))&&d&&d.startsWith("/api/");if(!c||d)return a;var e=hg(b),f={};E(rg,function(g){e[g]&&(f[g]=e[g])});
return jg(a,f||{},!1)}
function vg(a,b){var c=b.format||"JSON";a=wg(a,b);var d=xg(a,b),e=!1,f=yg(a,function(k){if(!e){e=!0;h&&Kf(h);var l=pg(k),p=null,n=400<=k.status&&500>k.status,r=500<=k.status&&600>k.status;if(l||n||r)p=zg(a,c,k,b.convertToSafeHtml);if(l)a:if(k&&204==k.status)l=!0;else{switch(c){case "XML":l=0==parseInt(p&&p.return_code,10);break a;case "RAW":l=!0;break a}l=!!p}p=p||{};n=b.context||y;l?b.onSuccess&&b.onSuccess.call(n,k,p):b.onError&&b.onError.call(n,k,p);b.onFinish&&b.onFinish.call(n,k,p)}},b.method,
d,b.headers,b.responseType,b.withCredentials);
if(b.onTimeout&&0<b.timeout){var g=b.onTimeout;var h=Jf(function(){e||(e=!0,f.abort(),Kf(h),g.call(b.context||y,f))},b.timeout)}return f}
function wg(a,b){b.includeDomain&&(a=document.location.protocol+"//"+document.location.hostname+(document.location.port?":"+document.location.port:"")+a);var c=F("XSRF_FIELD_NAME",void 0);if(b=b.urlParams)b[c]&&delete b[c],a=jg(a,b||{},!0);return a}
function xg(a,b){var c=F("XSRF_FIELD_NAME",void 0),d=F("XSRF_TOKEN",void 0),e=b.postBody||"",f=b.postParams,g=F("XSRF_FIELD_NAME",void 0),h;b.headers&&(h=b.headers["Content-Type"]);b.excludeXsrf||ec(a)&&!b.withCredentials&&ec(a)!=document.location.hostname||"POST"!=b.method||h&&"application/x-www-form-urlencoded"!=h||b.postParams&&b.postParams[g]||(f||(f={}),f[c]=d);f&&"string"===typeof e&&(e=hg(e),sb(e,f),e=b.postBodyFormat&&"JSON"==b.postBodyFormat?JSON.stringify(e):gc(e));f=e||f&&!kb(f);!sg&&f&&
"POST"!=b.method&&(sg=!0,sf(Error("AJAX request with postData should use POST")));return e}
function zg(a,b,c,d){var e=null;switch(b){case "JSON":try{var f=c.responseText}catch(g){throw d=Error("Error reading responseText"),d.params=a,tf(d),g;}a=c.getResponseHeader("Content-Type")||"";f&&0<=a.indexOf("json")&&(")]}'\n"===f.substring(0,5)&&(f=f.substring(5)),e=JSON.parse(f));break;case "XML":if(a=(a=c.responseXML)?Ag(a):null)e={},E(a.getElementsByTagName("*"),function(g){e[g.tagName]=Bg(g)})}d&&Cg(e);
return e}
function Cg(a){if(Oa(a))for(var b in a){var c;(c="html_content"==b)||(c=b.length-5,c=0<=c&&b.indexOf("_html",c)==c);if(c){c=b;var d=Ub(a[b],null);a[c]=d}else Cg(a[b])}}
function Ag(a){return a?(a=("responseXML"in a?a.responseXML:a).getElementsByTagName("root"))&&0<a.length?a[0]:null:null}
function Bg(a){var b="";E(a.childNodes,function(c){b+=c.nodeValue});
return b}
function yg(a,b,c,d,e,f,g){function h(){4==(k&&"readyState"in k?k.readyState:0)&&b&&rf(b)(k)}
c=void 0===c?"GET":c;d=void 0===d?"":d;var k=og();if(!k)return null;"onloadend"in k?k.addEventListener("loadend",h,!1):k.onreadystatechange=h;Q("debug_forward_web_query_parameters")&&(a=ug(a));k.open(c,a,!0);f&&(k.responseType=f);g&&(k.withCredentials=!0);c="POST"==c&&(void 0===window.FormData||!(d instanceof FormData));if(e=tg(a,e))for(var l in e)k.setRequestHeader(l,e[l]),"content-type"==l.toLowerCase()&&(c=!1);c&&k.setRequestHeader("Content-Type","application/x-www-form-urlencoded");k.send(d);
return k}
;var Dg=zc||Ac;function Eg(a){var b=Pb;return b?0<=b.toLowerCase().indexOf(a):!1}
;var Fg={},Gg=0;
function Hg(a,b,c,d,e){e=void 0===e?"":e;if(a)if(c&&!Eg("cobalt")){if(a){a instanceof Hb||(a="object"==typeof a&&a.X?a.W():String(a),Mb.test(a)?a=new Hb(a,Ib):(a=String(a),a=a.replace(/(%0A|%0D)/g,""),a=(b=a.match(Lb))&&Kb.test(b[1])?new Hb(a,Ib):null));a=Jb(a||Ob);if("about:invalid#zClosurez"===a||a.startsWith("data"))a="";else{if(!(a instanceof Sb)){b="object"==typeof a;var f=null;b&&a.ma&&(f=a.ja());a=Ub(zb(b&&a.X?a.W():String(a)),f)}a instanceof Sb&&a.constructor===Sb?a=a.h:(Ma(a),a="type_error:SafeHtml");
a=encodeURIComponent(String(xe(a.toString())))}/^[\s\xa0]*$/.test(a)||(a=Lc("IFRAME",{src:'javascript:"<body><img src=\\""+'+a+'+"\\"></body>"',style:"display:none"}),(9==a.nodeType?a:a.ownerDocument||a.document).body.appendChild(a))}}else if(e)yg(a,b,"POST",e,d);else if(F("USE_NET_AJAX_FOR_PING_TRANSPORT",!1)||d)yg(a,b,"GET","",d);else{b:{try{var g=new Ya({url:a});if(g.j&&g.i||g.l){var h=dc(a.match(cc)[5]||null),k;if(!(k=!h||!h.endsWith("/aclk"))){var l=a.search(ic);d:{for(c=0;0<=(c=a.indexOf("ri",
c))&&c<l;){var p=a.charCodeAt(c-1);if(38==p||63==p){var n=a.charCodeAt(c+2);if(!n||61==n||38==n||35==n){var r=c;break d}}c+=3}r=-1}if(0>r)var q=null;else{var B=a.indexOf("&",r);if(0>B||B>l)B=l;r+=3;q=decodeURIComponent(a.substr(r,B-r).replace(/\+/g," "))}k="1"!==q}f=!k;break b}}catch(I){}f=!1}f?Ig(a)?(b&&b(),f=!0):f=!1:f=!1;f||Jg(a,b)}}
function Kg(a){var b=void 0===b?"":b;Ig(a,b)||Hg(a,void 0,void 0,void 0,b)}
function Ig(a,b){try{if(window.navigator&&window.navigator.sendBeacon&&window.navigator.sendBeacon(a,void 0===b?"":b))return!0}catch(c){}return!1}
function Jg(a,b){var c=new Image,d=""+Gg++;Fg[d]=c;c.onload=c.onerror=function(){b&&Fg[d]&&b();delete Fg[d]};
c.src=a}
;var Lg=y.ytPubsubPubsubInstance||new M,Mg=y.ytPubsubPubsubSubscribedKeys||{},Ng=y.ytPubsubPubsubTopicToKeys||{},Og=y.ytPubsubPubsubIsSynchronous||{};function Pg(a,b){var c=Qg();if(c&&b){var d=c.subscribe(a,function(){var e=arguments;var f=function(){Mg[d]&&b.apply&&"function"==typeof b.apply&&b.apply(window,e)};
try{Og[a]?f():Jf(f,0)}catch(g){sf(g)}},void 0);
Mg[d]=!0;Ng[a]||(Ng[a]=[]);Ng[a].push(d);return d}return 0}
function Rg(a){var b=Qg();b&&("number"===typeof a?a=[a]:"string"===typeof a&&(a=[parseInt(a,10)]),E(a,function(c){b.unsubscribeByKey(c);delete Mg[c]}))}
function Sg(a,b){var c=Qg();c&&c.publish.apply(c,arguments)}
function Tg(a){var b=Qg();if(b)if(b.clear(a),a)Ug(a);else for(var c in Ng)Ug(c)}
function Qg(){return y.ytPubsubPubsubInstance}
function Ug(a){Ng[a]&&(a=Ng[a],E(a,function(b){Mg[b]&&delete Mg[b]}),a.length=0)}
M.prototype.subscribe=M.prototype.subscribe;M.prototype.unsubscribeByKey=M.prototype.Y;M.prototype.publish=M.prototype.R;M.prototype.clear=M.prototype.clear;z("ytPubsubPubsubInstance",Lg,void 0);z("ytPubsubPubsubTopicToKeys",Ng,void 0);z("ytPubsubPubsubIsSynchronous",Og,void 0);z("ytPubsubPubsubSubscribedKeys",Mg,void 0);var Vg=window,R=Vg.ytcsi&&Vg.ytcsi.now?Vg.ytcsi.now:Vg.performance&&Vg.performance.timing&&Vg.performance.now&&Vg.performance.timing.navigationStart?function(){return Vg.performance.timing.navigationStart+Vg.performance.now()}:function(){return(new Date).getTime()};var Wg=xf("initial_gel_batch_timeout",1E3),Xg=Math.pow(2,16)-1,Yg=null,Zg=0,$g=void 0,ah=0,bh=0,ch=0,dh=!0,eh=y.ytLoggingTransportGELQueue_||new Map;z("ytLoggingTransportGELQueue_",eh,void 0);var fh=y.ytLoggingTransportTokensToCttTargetIds_||{};z("ytLoggingTransportTokensToCttTargetIds_",fh,void 0);
function gh(a,b){if("log_event"===a.endpoint){var c="";a.ea?c="visitorOnlyApprovedKey":a.F&&(fh[a.F.token]=hh(a.F),c=a.F.token);var d=eh.get(c)||[];eh.set(c,d);d.push(a.payload);b&&($g=new b);a=xf("tvhtml5_logging_max_batch")||xf("web_logging_max_batch")||100;b=R();d.length>=a?ih({writeThenSend:!0}):10<=b-ch&&(jh(),ch=b)}}
function kh(a,b){if("log_event"===a.endpoint){var c="";a.ea?c="visitorOnlyApprovedKey":a.F&&(fh[a.F.token]=hh(a.F),c=a.F.token);var d=new Map;d.set(c,[a.payload]);b&&($g=new b);return new Ee(function(e){$g&&$g.isReady()?lh(d,e,{bypassNetworkless:!0}):e()})}}
function ih(a){a=void 0===a?{}:a;new Ee(function(b){Kf(ah);Kf(bh);bh=0;$g&&$g.isReady()?(lh(eh,b,a),eh.clear()):(jh(),b())})}
function jh(){Q("web_gel_timeout_cap")&&!bh&&(bh=Jf(function(){ih({writeThenSend:!0})},6E4));
Kf(ah);var a=F("LOGGING_BATCH_TIMEOUT",xf("web_gel_debounce_ms",1E4));Q("shorten_initial_gel_batch_timeout")&&dh&&(a=Wg);ah=Jf(function(){ih({writeThenSend:!0})},a)}
function lh(a,b,c){var d=$g;c=void 0===c?{}:c;var e=Math.round(R()),f=a.size;a=u(a);for(var g=a.next();!g.done;g=a.next()){var h=u(g.value);g=h.next().value;var k=h.next().value;h=qb({context:mh(d.h||nh())});h.events=k;(k=fh[g])&&oh(h,g,k);delete fh[g];g="visitorOnlyApprovedKey"===g;ph(h,e,g);Q("send_beacon_before_gel")&&window.navigator&&window.navigator.sendBeacon&&!c.writeThenSend&&Kg("/generate_204");qh(d,"log_event",h,{retry:!0,onSuccess:function(){f--;f||b();Zg=Math.round(R()-e)},
onError:function(){f--;f||b()},
Ba:c,ea:g});dh=!1}}
function ph(a,b,c){a.requestTimeMs=String(b);Q("unsplit_gel_payloads_in_logs")&&(a.unsplitGelPayloadsInLogs=!0);!c&&(b=F("EVENT_ID",void 0))&&((c=F("BATCH_CLIENT_COUNTER",void 0)||0)||(c=Math.floor(Math.random()*Xg/2)),c++,c>Xg&&(c=1),N("BATCH_CLIENT_COUNTER",c),b={serializedEventId:b,clientCounter:String(c)},a.serializedClientEventId=b,Yg&&Zg&&Q("log_gel_rtt_web")&&(a.previousBatchInfo={serializedClientEventId:Yg,roundtripMs:String(Zg)}),Yg=b,Zg=0)}
function oh(a,b,c){if(c.videoId)var d="VIDEO";else if(c.playlistId)d="PLAYLIST";else return;a.credentialTransferTokenTargetId=c;a.context=a.context||{};a.context.user=a.context.user||{};a.context.user.credentialTransferTokens=[{token:b,scope:d}]}
function hh(a){var b={};a.videoId?b.videoId=a.videoId:a.playlistId&&(b.playlistId=a.playlistId);return b}
;var rh=y.ytLoggingGelSequenceIdObj_||{};z("ytLoggingGelSequenceIdObj_",rh,void 0);function sh(a,b,c,d){d=void 0===d?{}:d;var e={},f=Math.round(d.timestamp||R());e.eventTimeMs=f<Number.MAX_SAFE_INTEGER?f:0;e[a]=b;a=Yf();e.context={lastActivityMs:String(d.timestamp||!isFinite(a)?-1:a)};Q("log_sequence_info_on_gel_web")&&d.O&&(a=e.context,b=d.O,rh[b]=b in rh?rh[b]+1:0,a.sequence={index:rh[b],groupKey:b},d.La&&delete rh[d.O]);(d.Pk?kh:gh)({endpoint:"log_event",payload:e,F:d.F,ea:d.ea},c)}
;function th(){if(!y.matchMedia)return"WEB_DISPLAY_MODE_UNKNOWN";try{return y.matchMedia("(display-mode: standalone)").matches?"WEB_DISPLAY_MODE_STANDALONE":y.matchMedia("(display-mode: minimal-ui)").matches?"WEB_DISPLAY_MODE_MINIMAL_UI":y.matchMedia("(display-mode: fullscreen)").matches?"WEB_DISPLAY_MODE_FULLSCREEN":y.matchMedia("(display-mode: browser)").matches?"WEB_DISPLAY_MODE_BROWSER":"WEB_DISPLAY_MODE_UNKNOWN"}catch(a){return"WEB_DISPLAY_MODE_UNKNOWN"}}
;function uh(a,b,c,d,e){ed.set(""+a,b,{oa:c,path:"/",domain:void 0===d?"youtube.com":d,secure:void 0===e?!1:e})}
;var vh=A("ytglobal.prefsUserPrefsPrefs_")||{};z("ytglobal.prefsUserPrefsPrefs_",vh,void 0);function wh(){this.h=F("ALT_PREF_COOKIE_NAME","PREF");this.i=F("ALT_PREF_COOKIE_DOMAIN","youtube.com");var a=ed.get(""+this.h,void 0);if(a){a=decodeURIComponent(a).split("&");for(var b=0;b<a.length;b++){var c=a[b].split("="),d=c[0];(c=c[1])&&(vh[d]=c.toString())}}}
wh.prototype.get=function(a,b){xh(a);yh(a);a=void 0!==vh[a]?vh[a].toString():null;return null!=a?a:b?b:""};
wh.prototype.set=function(a,b){xh(a);yh(a);if(null==b)throw Error("ExpectedNotNull");vh[a]=b.toString()};
wh.prototype.remove=function(a){xh(a);yh(a);delete vh[a]};
wh.prototype.clear=function(){for(var a in vh)delete vh[a]};
function yh(a){if(/^f([1-9][0-9]*)$/.test(a))throw Error("ExpectedRegexMatch: "+a);}
function xh(a){if(!/^\w+$/.test(a))throw Error("ExpectedRegexMismatch: "+a);}
function zh(a){a=void 0!==vh[a]?vh[a].toString():null;return null!=a&&/^[A-Fa-f0-9]+$/.test(a)?parseInt(a,16):null}
La(wh);var Ah={bluetooth:"CONN_DISCO",cellular:"CONN_CELLULAR_UNKNOWN",ethernet:"CONN_WIFI",none:"CONN_NONE",wifi:"CONN_WIFI",wimax:"CONN_CELLULAR_4G",other:"CONN_UNKNOWN",unknown:"CONN_UNKNOWN","slow-2g":"CONN_CELLULAR_2G","2g":"CONN_CELLULAR_2G","3g":"CONN_CELLULAR_3G","4g":"CONN_CELLULAR_4G"},Bh={"slow-2g":"EFFECTIVE_CONNECTION_TYPE_SLOW_2G","2g":"EFFECTIVE_CONNECTION_TYPE_2G","3g":"EFFECTIVE_CONNECTION_TYPE_3G","4g":"EFFECTIVE_CONNECTION_TYPE_4G"};
function Ch(){var a=y.navigator;return a?a.connection:void 0}
;function Dh(){return"INNERTUBE_API_KEY"in of&&"INNERTUBE_API_VERSION"in of}
function nh(){return{innertubeApiKey:F("INNERTUBE_API_KEY",void 0),innertubeApiVersion:F("INNERTUBE_API_VERSION",void 0),Oa:F("INNERTUBE_CONTEXT_CLIENT_CONFIG_INFO"),Pa:F("INNERTUBE_CONTEXT_CLIENT_NAME","WEB"),innertubeContextClientVersion:F("INNERTUBE_CONTEXT_CLIENT_VERSION",void 0),Ra:F("INNERTUBE_CONTEXT_HL",void 0),Qa:F("INNERTUBE_CONTEXT_GL",void 0),Sa:F("INNERTUBE_HOST_OVERRIDE",void 0)||"",Ua:!!F("INNERTUBE_USE_THIRD_PARTY_AUTH",!1),Ta:!!F("INNERTUBE_OMIT_API_KEY_WHEN_AUTH_HEADER_IS_PRESENT",
!1),appInstallData:F("SERIALIZED_CLIENT_CONFIG_DATA",void 0)}}
function mh(a){var b={client:{hl:a.Ra,gl:a.Qa,clientName:a.Pa,clientVersion:a.innertubeContextClientVersion,configInfo:a.Oa}},c=y.devicePixelRatio;c&&1!=c&&(b.client.screenDensityFloat=String(c));c=F("EXPERIMENTS_TOKEN","");""!==c&&(b.client.experimentsToken=c);c=[];var d=F("EXPERIMENTS_FORCED_FLAGS",{});for(e in d)c.push({key:e,value:String(d[e])});var e=F("EXPERIMENT_FLAGS",{});for(var f in e)f.startsWith("force_")&&void 0===d[f]&&c.push({key:f,value:String(e[f])});0<c.length&&(b.request={internalExperimentFlags:c});
f=b.client.clientName;if("WEB"===f||"MWEB"===f||1===f||2===f){if(!Q("web_include_display_mode_killswitch")){var g;b.client.mainAppWebInfo=null!=(g=b.client.mainAppWebInfo)?g:{};b.client.mainAppWebInfo.webDisplayMode=th()}}else if(g=b.client.clientName,("WEB_REMIX"===g||76===g)&&!Q("music_web_display_mode_killswitch")){var h;b.client.Aa=null!=(h=b.client.Aa)?h:{};b.client.Aa.webDisplayMode=th()}a.appInstallData&&(b.client.configInfo=b.client.configInfo||{},b.client.configInfo.appInstallData=a.appInstallData);
F("DELEGATED_SESSION_ID")&&!Q("pageid_as_header_web")&&(b.user={onBehalfOfUser:F("DELEGATED_SESSION_ID")});a:{if(h=Ch()){a=Ah[h.type||"unknown"]||"CONN_UNKNOWN";h=Ah[h.effectiveType||"unknown"]||"CONN_UNKNOWN";"CONN_CELLULAR_UNKNOWN"===a&&"CONN_UNKNOWN"!==h&&(a=h);if("CONN_UNKNOWN"!==a)break a;if("CONN_UNKNOWN"!==h){a=h;break a}}a=void 0}a&&(b.client.connectionType=a);Q("web_log_effective_connection_type")&&(a=Ch(),a=null!==a&&void 0!==a&&a.effectiveType?Bh.hasOwnProperty(a.effectiveType)?Bh[a.effectiveType]:
"EFFECTIVE_CONNECTION_TYPE_UNKNOWN":void 0,a&&(b.client.effectiveConnectionType=a));a=Object;h=a.assign;g=b.client;f={};e=u(Object.entries(hg(F("DEVICE",""))));for(c=e.next();!c.done;c=e.next())d=u(c.value),c=d.next().value,d=d.next().value,"cbrand"===c?f.deviceMake=d:"cmodel"===c?f.deviceModel=d:"cbr"===c?f.browserName=d:"cbrver"===c?f.browserVersion=d:"cos"===c?f.osName=d:"cosver"===c?f.osVersion=d:"cplatform"===c&&(f.platform=d);b.client=h.call(a,g,f);return b}
function Eh(a,b,c){c=void 0===c?{}:c;var d={"X-Goog-Visitor-Id":c.visitorData||F("VISITOR_DATA","")};if(b&&b.includes("www.youtube-nocookie.com"))return d;(b=c.Gk||F("AUTHORIZATION"))||(a?b="Bearer "+A("gapi.auth.getToken")().Fk:b=hd([]));b&&(d.Authorization=b,d["X-Goog-AuthUser"]=F("SESSION_INDEX",0),Q("pageid_as_header_web")&&(d["X-Goog-PageId"]=F("DELEGATED_SESSION_ID")));return d}
;function Fh(a){a=Object.assign({},a);delete a.Authorization;var b=hd();if(b){var c=new zd;c.update(F("INNERTUBE_API_KEY",void 0));c.update(b);a.hash=Ec(c.digest())}return a}
;function Gh(a){var b=new ff;(b=b.isAvailable()?a?new mf(b,a):b:null)||(a=new gf(a||"UserDataSharedStore"),b=a.isAvailable()?a:null);this.h=(a=b)?new bf(a):null;this.i=document.domain||window.location.hostname}
Gh.prototype.set=function(a,b,c,d){c=c||31104E3;this.remove(a);if(this.h)try{this.h.set(a,b,Date.now()+1E3*c);return}catch(f){}var e="";if(d)try{e=escape(xe(b))}catch(f){return}else e=escape(b);uh(a,e,c,this.i)};
Gh.prototype.get=function(a,b){var c=void 0,d=!this.h;if(!d)try{c=this.h.get(a)}catch(e){d=!0}if(d&&(c=ed.get(""+a,void 0))&&(c=unescape(c),b))try{c=JSON.parse(c)}catch(e){this.remove(a),c=void 0}return c};
Gh.prototype.remove=function(a){this.h&&this.h.remove(a);var b=this.i;ed.remove(""+a,"/",void 0===b?"youtube.com":b)};var Hh;function Ih(){Hh||(Hh=new Gh("yt.innertube"));return Hh}
function Jh(a,b,c,d){if(d)return null;d=Ih().get("nextId",!0)||1;var e=Ih().get("requests",!0)||{};e[d]={method:a,request:b,authState:Fh(c),requestTime:Math.round(R())};Ih().set("nextId",d+1,86400,!0);Ih().set("requests",e,86400,!0);return d}
function Kh(a){var b=Ih().get("requests",!0)||{};delete b[a];Ih().set("requests",b,86400,!0)}
function Lh(a){var b=Ih().get("requests",!0);if(b){for(var c in b){var d=b[c];if(!(6E4>Math.round(R())-d.requestTime)){var e=d.authState,f=Fh(Eh(!1));ob(e,f)&&(e=d.request,"requestTimeMs"in e&&(e.requestTimeMs=Math.round(R())),qh(a,d.method,e,{}));delete b[c]}}Ih().set("requests",b,86400,!0)}}
;function Mh(a,b){this.version=a;this.args=b}
;function Nh(a,b){this.topic=a;this.h=b}
Nh.prototype.toString=function(){return this.topic};var Oh=A("ytPubsub2Pubsub2Instance")||new M;M.prototype.subscribe=M.prototype.subscribe;M.prototype.unsubscribeByKey=M.prototype.Y;M.prototype.publish=M.prototype.R;M.prototype.clear=M.prototype.clear;z("ytPubsub2Pubsub2Instance",Oh,void 0);var Ph=A("ytPubsub2Pubsub2SubscribedKeys")||{};z("ytPubsub2Pubsub2SubscribedKeys",Ph,void 0);var Qh=A("ytPubsub2Pubsub2TopicToKeys")||{};z("ytPubsub2Pubsub2TopicToKeys",Qh,void 0);var Rh=A("ytPubsub2Pubsub2IsAsync")||{};z("ytPubsub2Pubsub2IsAsync",Rh,void 0);
z("ytPubsub2Pubsub2SkipSubKey",null,void 0);function Sh(a,b){var c=Th();c&&c.publish.call(c,a.toString(),a,b)}
function Uh(a){var b=Vh,c=Th();if(!c)return 0;var d=c.subscribe(b.toString(),function(e,f){var g=A("ytPubsub2Pubsub2SkipSubKey");g&&g==d||(g=function(){if(Ph[d])try{if(f&&b instanceof Nh&&b!=e)try{var h=b.h,k=f;if(!k.args||!k.version)throw Error("yt.pubsub2.Data.deserialize(): serializedData is incomplete.");try{if(!h.P){var l=new h;h.P=l.version}var p=h.P}catch(n){}if(!p||k.version!=p)throw Error("yt.pubsub2.Data.deserialize(): serializedData version is incompatible.");try{f=Reflect.construct(h,
fb(k.args))}catch(n){throw n.message="yt.pubsub2.Data.deserialize(): "+n.message,n;}}catch(n){throw n.message="yt.pubsub2.pubsub2 cross-binary conversion error for "+b.toString()+": "+n.message,n;}a.call(window,f)}catch(n){sf(n)}},Rh[b.toString()]?A("yt.scheduler.instance")?Pf(g):Jf(g,0):g())});
Ph[d]=!0;Qh[b.toString()]||(Qh[b.toString()]=[]);Qh[b.toString()].push(d);return d}
function Wh(){var a=Xh,b=Uh(function(c){a.apply(void 0,arguments);Yh(b)});
return b}
function Yh(a){var b=Th();b&&("number"===typeof a&&(a=[a]),E(a,function(c){b.unsubscribeByKey(c);delete Ph[c]}))}
function Th(){return A("ytPubsub2Pubsub2Instance")}
;function Zh(){}
;var $h=[],ai=!1;function bi(a){ai||($h.push({type:"ERROR",payload:a}),10<$h.length&&$h.shift())}
function ci(a,b){ai||($h.push({type:"EVENT",eventType:a,payload:b}),10<$h.length&&$h.shift())}
;var di=function(){var a;return function(){a||(a=new Gh("ytidb"));return a}}();
function ei(){var a;return null===(a=di())||void 0===a?void 0:a.get("LAST_RESULT_ENTRY_KEY",!0)}
function fi(a,b,c){this.h=void 0===a?!1:a;this.failureMessage=b;this.j=c;(a=ei())||(a={createdTimestampMs:R(),isSupported:this.h,resultCount:0,hasSucceededOnce:this.h});this.i=a;var d;if(gi()){var e;this.i.isSupported===this.h?e=Object.assign(Object.assign({},this.i),{resultCount:this.i.resultCount+1}):e={isSupported:this.h,resultCount:1,createdTimestampMs:R(),hasSucceededOnce:this.i.hasSucceededOnce||this.h};null===(d=di())||void 0===d?void 0:d.set("LAST_RESULT_ENTRY_KEY",e,2592E3,!0)}}
function hi(a,b){return new fi(!1,a instanceof Error?a.message:"",void 0===b?!1:b)}
fi.prototype.isSupported=function(){return this.h};
fi.prototype.log=function(){gi()&&ci("IS_SUPPORTED_COMPLETED",{isSupported:this.h,lastIsSupported:this.i.isSupported,failureMessage:this.failureMessage,sameResultCount:this.i.resultCount,sameResultDurationMs:Math.floor(R()-this.i.createdTimestampMs),canDetectDataOnFailure:this.j})};
function gi(){var a;return!!(Q("ytidb_analyze_is_supported")&&(null===(a=di())||void 0===a?0:a.h))}
;function ii(a,b){for(var c=[],d=1;d<arguments.length;++d)c[d-1]=arguments[d];d=Error.call(this,a);this.message=d.message;"stack"in d&&(this.stack=d.stack);this.args=[].concat(c instanceof Array?c:ha(u(c)))}
v(ii,Error);function ji(a){if(0<=a.indexOf(":"))throw Error("Database name cannot contain ':'");}
function ki(a){return a.substr(0,a.indexOf(":"))||a}
;var li={},mi=(li.AUTH_INVALID="No user identifier specified.",li.EXPLICIT_ABORT="Transaction was explicitly aborted.",li.IDB_NOT_SUPPORTED="IndexedDB is not supported.",li.MISSING_OBJECT_STORE="Object store not created.",li.UNKNOWN_ABORT="Transaction was aborted for unknown reasons.",li.QUOTA_EXCEEDED="The current transaction exceeded its quota limitations.",li.QUOTA_MAYBE_EXCEEDED="The current transaction may have failed because of exceeding quota limitations.",li.EXECUTE_TRANSACTION_ON_CLOSED_DB=
"Can't start a transaction on a closed database",li),ni={},oi=(ni.AUTH_INVALID="ERROR",ni.EXECUTE_TRANSACTION_ON_CLOSED_DB="WARNING",ni.EXPLICIT_ABORT="IGNORED",ni.IDB_NOT_SUPPORTED="ERROR",ni.MISSING_OBJECT_STORE="ERROR",ni.QUOTA_EXCEEDED="WARNING",ni.QUOTA_MAYBE_EXCEEDED="WARNING",ni.UNKNOWN_ABORT="WARNING",ni),pi={},qi=(pi.AUTH_INVALID=!1,pi.EXECUTE_TRANSACTION_ON_CLOSED_DB=!1,pi.EXPLICIT_ABORT=!1,pi.IDB_NOT_SUPPORTED=!1,pi.MISSING_OBJECT_STORE=!1,pi.QUOTA_EXCEEDED=!1,pi.QUOTA_MAYBE_EXCEEDED=!0,
pi.UNKNOWN_ABORT=!0,pi);function S(a,b,c,d,e){b=void 0===b?{}:b;c=void 0===c?mi[a]:c;d=void 0===d?oi[a]:d;e=void 0===e?qi[a]:e;ii.call(this,c,Object.assign({name:"YtIdbKnownError",isSw:void 0===self.document,isIframe:self!==self.top,type:a},b));this.type=a;this.message=c;this.level=d;this.h=e;Object.setPrototypeOf(this,S.prototype)}
v(S,ii);function ri(a){S.call(this,"MISSING_OBJECT_STORE",{Kk:a},mi.MISSING_OBJECT_STORE);Object.setPrototypeOf(this,ri.prototype)}
v(ri,S);var si=["The database connection is closing","Can't start a transaction on a closed database","A mutation operation was attempted on a database that did not allow mutations"];
function ti(a,b,c){b=ki(b);var d=a instanceof Error?a:Error("Unexpected error: "+a);if(d instanceof S)return d;if("QuotaExceededError"===d.name)return new S("QUOTA_EXCEEDED",{objectStoreNames:c,dbName:b});if(Bc&&"UnknownError"===d.name)return new S("QUOTA_MAYBE_EXCEEDED",{objectStoreNames:c,dbName:b});if("InvalidStateError"===d.name&&si.some(function(e){return d.message.includes(e)}))return new S("EXECUTE_TRANSACTION_ON_CLOSED_DB",{objectStoreNames:c,
dbName:b});if("AbortError"===d.name)return new S("UNKNOWN_ABORT",{objectStoreNames:c,dbName:b},d.message);d.args=[{name:"IdbError",Lk:d.name,dbName:b,objectStoreNames:c}];d.level="WARNING";return d}
;function ui(a){if(!a)throw Error();throw a;}
function vi(a){return a}
function T(a){function b(e){if("PENDING"===d.state.status){d.state={status:"REJECTED",reason:e};e=u(d.onRejected);for(var f=e.next();!f.done;f=e.next())f=f.value,f()}}
function c(e){if("PENDING"===d.state.status){d.state={status:"FULFILLED",value:e};e=u(d.h);for(var f=e.next();!f.done;f=e.next())f=f.value,f()}}
var d=this;this.i=a;this.state={status:"PENDING"};this.h=[];this.onRejected=[];try{this.i(c,b)}catch(e){b(e)}}
T.all=function(a){return new T(function(b,c){var d=[],e=a.length;0===e&&b(d);for(var f={T:0};f.T<a.length;f={T:f.T},++f.T)wi(T.resolve(a[f.T]).then(function(g){return function(h){d[g.T]=h;e--;0===e&&b(d)}}(f)),function(g){c(g)})})};
T.resolve=function(a){return new T(function(b,c){a instanceof T?a.then(b,c):b(a)})};
T.reject=function(a){return new T(function(b,c){c(a)})};
T.prototype.then=function(a,b){var c=this,d=null!==a&&void 0!==a?a:vi,e=null!==b&&void 0!==b?b:ui;return new T(function(f,g){"PENDING"===c.state.status?(c.h.push(function(){xi(c,c,d,f,g)}),c.onRejected.push(function(){yi(c,c,e,f,g)})):"FULFILLED"===c.state.status?xi(c,c,d,f,g):"REJECTED"===c.state.status&&yi(c,c,e,f,g)})};
function wi(a,b){a.then(void 0,b)}
function xi(a,b,c,d,e){try{if("FULFILLED"!==a.state.status)throw Error("calling handleResolve before the promise is fulfilled.");var f=c(a.state.value);f instanceof T?zi(a,b,f,d,e):d(f)}catch(g){e(g)}}
function yi(a,b,c,d,e){try{if("REJECTED"!==a.state.status)throw Error("calling handleReject before the promise is rejected.");var f=c(a.state.reason);f instanceof T?zi(a,b,f,d,e):d(f)}catch(g){e(g)}}
function zi(a,b,c,d,e){b===c?e(new TypeError("Circular promise chain detected.")):c.then(function(f){f instanceof T?zi(a,b,f,d,e):d(f)},function(f){e(f)})}
;function Ai(a,b,c){function d(){c(a.error);f()}
function e(){b(a.result);f()}
function f(){try{a.removeEventListener("success",e),a.removeEventListener("error",d)}catch(g){}}
a.addEventListener("success",e);a.addEventListener("error",d)}
function Bi(a){return new Promise(function(b,c){Ai(a,b,c)})}
function V(a){return new T(function(b,c){Ai(a,b,c)})}
;function Ci(a,b){return new T(function(c,d){function e(){var f=a?b(a):null;f?f.then(function(g){a=g;e()},d):c()}
e()})}
;function Di(a){return new Promise(function(b){Qf(function(){b()},a)})}
function Ei(a,b){this.h=a;this.options=b;this.transactionCount=0;this.j=Math.round(R());this.i=!1}
m=Ei.prototype;m.add=function(a,b,c){return Fi(this,[a],{mode:"readwrite",I:!0},function(d){return Gi(d,a).add(b,c)})};
m.clear=function(a){return Fi(this,[a],{mode:"readwrite",I:!0},function(b){return Gi(b,a).clear()})};
m.close=function(){var a;this.h.close();(null===(a=this.options)||void 0===a?0:a.closed)&&this.options.closed()};
m.count=function(a,b){return Fi(this,[a],{mode:"readonly",I:!0},function(c){return Gi(c,a).count(b)})};
function Hi(a,b,c){a=a.h.createObjectStore(b,c);return new Ii(a)}
m.delete=function(a,b){return Fi(this,[a],{mode:"readwrite",I:!0},function(c){return Gi(c,a).delete(b)})};
m.get=function(a,b){return Fi(this,[a],{mode:"readonly",I:!0},function(c){return Gi(c,a).get(b)})};
function Ji(a,b,c,d){return Fi(a,[b],{mode:"readwrite",I:!0},function(e){e=Gi(e,b);return V(e.h.put(c,d))})}
function Fi(a,b,c,d){return H(a,function f(){var g=this,h,k,l,p,n,r,q,B,I,J,ba,U,O,na;return x(f,function(P){switch(P.h){case 1:var mb={mode:"readonly",I:!1};"string"===typeof c?mb.mode=c:mb=c;h=mb;g.transactionCount++;k=Q("ytidb_transaction_exponential_backoff_retries");l=h.I?xf("ytidb_transaction_try_count",1):1;p=500;n=0;case 2:if(r){P.B(3);break}n++;q=Math.round(R());ta(P,4);B=g.h.transaction(b,h.mode);mb=new Ki(B);mb=Li(mb,d);return w(P,mb,6);case 6:return I=P.i,J=Math.round(R()),Mi(g,q,J,n,
void 0,b.join(),h),P.return(I);case 4:ba=ua(P);U=Math.round(R());O=ti(ba,g.h.name,b.join());if((na=O instanceof S&&!O.h)||n>=l){Mi(g,q,U,n,O,b.join(),h);r=O;P.B(2);break}if(!k){P.B(2);break}return w(P,Di(p),9);case 9:p*=2;P.B(2);break;case 3:return P.return(Promise.reject(r))}})})}
function Mi(a,b,c,d,e,f,g){b=c-b;e?(e instanceof S&&("QUOTA_EXCEEDED"===e.type||"QUOTA_MAYBE_EXCEEDED"===e.type)&&ci("QUOTA_EXCEEDED",{dbName:ki(a.h.name),objectStoreNames:f,transactionCount:a.transactionCount,transactionMode:g.mode}),e instanceof S&&"UNKNOWN_ABORT"===e.type&&(ci("TRANSACTION_UNEXPECTEDLY_ABORTED",{objectStoreNames:f,transactionDuration:b,transactionCount:a.transactionCount,dbDuration:c-a.j}),a.i=!0),Ni(a,!1,d,f,b),bi(e)):Ni(a,!0,d,f,b)}
function Ni(a,b,c,d,e){ci("TRANSACTION_ENDED",{objectStoreNames:d,connectionHasUnknownAbortedTransaction:a.i,duration:e,isSuccessful:b,tryCount:c})}
function Ii(a){this.h=a}
m=Ii.prototype;m.add=function(a,b){return V(this.h.add(a,b))};
m.clear=function(){return V(this.h.clear()).then(function(){})};
m.count=function(a){return V(this.h.count(a))};
function Oi(a,b){return Pi(a,{query:b},function(c){return c.delete().then(function(){return c.continue()})}).then(function(){})}
m.delete=function(a){return a instanceof IDBKeyRange?Oi(this,a):V(this.h.delete(a))};
m.get=function(a){return V(this.h.get(a))};
m.index=function(a){return new Qi(this.h.index(a))};
m.getName=function(){return this.h.name};
function Pi(a,b,c){a=a.h.openCursor(b.query,b.direction);return Ri(a).then(function(d){return Ci(d,c)})}
function Ki(a){var b=this;this.h=a;this.i=new Map;this.aborted=!1;this.done=new Promise(function(c,d){b.h.addEventListener("complete",function(){c()});
b.h.addEventListener("error",function(e){e.currentTarget===e.target&&d(b.h.error)});
b.h.addEventListener("abort",function(){var e=b.h.error;if(e)d(e);else if(!b.aborted){e=S;for(var f=b.h.objectStoreNames,g=[],h=0;h<f.length;h++){var k=f.item(h);if(null===k)throw Error("Invariant: item in DOMStringList is null");g.push(k)}e=new e("UNKNOWN_ABORT",{objectStoreNames:g.join(),dbName:b.h.db.name,mode:b.h.mode});d(e)}})})}
function Li(a,b){var c=new Promise(function(d,e){wi(b(a).then(function(f){a.commit();d(f)}),e)});
return Promise.all([c,a.done]).then(function(d){return u(d).next().value})}
Ki.prototype.abort=function(){this.h.abort();this.aborted=!0;throw new S("EXPLICIT_ABORT");};
Ki.prototype.commit=function(){var a=this.h;a.commit&&!this.aborted&&a.commit()};
function Gi(a,b){b=a.h.objectStore(b);var c=a.i.get(b);c||(c=new Ii(b),a.i.set(b,c));return c}
function Qi(a){this.h=a}
Qi.prototype.count=function(a){return V(this.h.count(a))};
Qi.prototype.delete=function(a){return Si(this,{query:a},function(b){return b.delete().then(function(){return b.continue()})})};
Qi.prototype.get=function(a){return V(this.h.get(a))};
Qi.prototype.getKey=function(a){return V(this.h.getKey(a))};
function Si(a,b,c){a=a.h.openCursor(void 0===b.query?null:b.query,void 0===b.direction?"next":b.direction);return Ri(a).then(function(d){return Ci(d,c)})}
function Ti(a,b){this.request=a;this.cursor=b}
function Ri(a){return V(a).then(function(b){return null===b?null:new Ti(a,b)})}
m=Ti.prototype;m.advance=function(a){this.cursor.advance(a);return Ri(this.request)};
m.continue=function(a){this.cursor.continue(a);return Ri(this.request)};
m.delete=function(){return V(this.cursor.delete()).then(function(){})};
m.getKey=function(){return this.cursor.key};
m.getValue=function(){return this.cursor.value};
m.update=function(a){return V(this.cursor.update(a))};function Ui(a,b,c){return H(this,function e(){var f,g,h,k,l,p,n,r,q,B;return x(e,function(I){if(1==I.h)return f=self.indexedDB.open(a,b),g=c,h=g.blocked,k=g.blocking,l=g.mb,p=g.upgrade,n=g.closed,q=function(){r||(r=new Ei(f.result,{closed:n}));return r},f.addEventListener("upgradeneeded",function(J){if(null===J.newVersion)throw Error("Invariant: newVersion on IDbVersionChangeEvent is null");
if(null===f.transaction)throw Error("Invariant: transaction on IDbOpenDbRequest is null");J.dataLoss&&"none"!==J.dataLoss&&ci("IDB_DATA_CORRUPTED",{reason:J.dataLossMessage||"unknown reason",dbName:ki(a)});var ba=q(),U=new Ki(f.transaction);p&&p(ba,J.oldVersion,J.newVersion,U)}),h&&f.addEventListener("blocked",function(){h()}),w(I,Bi(f),2);
B=I.i;k&&B.addEventListener("versionchange",function(){k(q())});
B.addEventListener("close",function(){ci("IDB_UNEXPECTEDLY_CLOSED",{dbName:ki(a),dbVersion:B.version});l&&l()});
return I.return(q())})})}
function Vi(a,b,c){c=void 0===c?{}:c;return Ui(a,b,c)}
function Wi(a,b){b=void 0===b?{}:b;return H(this,function d(){var e,f,g;return x(d,function(h){e=self.indexedDB.deleteDatabase(a);f=b;(g=f.blocked)&&e.addEventListener("blocked",function(){g()});
return w(h,Bi(e),0)})})}
;function Xi(a,b){this.name=a;this.options=b;this.j=!1}
Xi.prototype.i=function(a,b,c){c=void 0===c?{}:c;return Vi(a,b,c)};
Xi.prototype.delete=function(a){a=void 0===a?{}:a;return Wi(this.name,a)};
Xi.prototype.open=function(){var a=this;if(!this.h){var b,c=function(){a.h===b&&(a.h=void 0)},d={blocking:function(f){f.close()},
closed:c,mb:c,upgrade:this.options.upgrade},e=function(){return H(a,function g(){var h=this,k,l,p;return x(g,function(n){switch(n.h){case 1:return ta(n,2),w(n,h.i(h.name,h.options.version,d),4);case 4:k=n.i;a:{var r=u(Object.keys(h.options.Ca));for(var q=r.next();!q.done;q=r.next())if(q=q.value,!k.h.objectStoreNames.contains(q)){r=q;break a}r=void 0}l=r;if(void 0===l){n.B(5);break}if(h.j){n.B(6);break}h.j=!0;return w(n,h.delete(),7);case 7:return n.return(e());case 6:throw new ri(l);case 5:return n.return(k);
case 2:p=ua(n);if(p instanceof DOMException?"VersionError"===p.name:"DOMError"in self&&p instanceof DOMError?"VersionError"===p.name:p instanceof Object&&"message"in p&&"An attempt was made to open a database using a lower version than the existing version."===p.message)return n.return(h.i(h.name,void 0,Object.assign(Object.assign({},d),{upgrade:void 0})));c();throw p;}})})};
this.h=b=e()}return this.h};var Yi=new Xi("YtIdbMeta",{Ca:{databases:!0},upgrade:function(a,b){1>b&&Hi(a,"databases",{keyPath:"actualName"})}});
function Zi(a){return H(this,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,Yi.open(),2);d=e.i;return e.return(Fi(d,["databases"],{I:!0,mode:"readwrite"},function(f){var g=Gi(f,"databases");return g.get(a.actualName).then(function(h){if(h?a.actualName!==h.actualName||a.publicName!==h.publicName||a.userIdentifier!==h.userIdentifier||a.clearDataOnAuthChange!==h.clearDataOnAuthChange:1)return V(g.h.put(a,void 0)).then(function(){})})}))})})}
function $i(a){return H(this,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,Yi.open(),2);d=e.i;return e.return(d.delete("databases",a))})})}
function aj(){return H(this,function b(){var c,d;return x(b,function(e){if(1==e.h)return w(e,Yi.open(),2);if(3!=e.h)return c=e.i,w(e,c.count("databases"),3);d=e.i;return e.return(0<d)})})}
function bj(a){return H(this,function c(){var d,e;return x(c,function(f){return 1==f.h?(d=[],w(f,Yi.open(),2)):3!=f.h?(e=f.i,w(f,Fi(e,["databases"],{I:!0,mode:"readonly"},function(g){d.length=0;return Pi(Gi(g,"databases"),{},function(h){a(h.getValue())&&d.push(h.getValue());return h.continue()})}),3)):f.return(d)})})}
function cj(){return bj(function(a){return"LogsDatabaseV2"===a.publicName&&void 0!==a.userIdentifier})}
;var dj;
function ej(){return H(this,function b(){var c,d,e,f,g;return x(b,function(h){switch(h.h){case 1:if(Q("ytidb_is_supported_cache_success_result")&&(c=ei(),null===c||void 0===c?0:c.hasSucceededOnce))return h.return(new fi(!0));var k;if(k=Dg)k=/WebKit\/([0-9]+)/.exec(Pb),k=!!(k&&600<=parseInt(k[1],10));k&&(k=/WebKit\/([0-9]+)/.exec(Pb),k=!(k&&602<=parseInt(k[1],10)));if(k)return h.return(hi(Error("YtIdb is not supported on iOS 8 or 9")));if(nc)return h.return(hi(Error("YtIdb is not supported on Edge")));try{if(d=
self,!(d.indexedDB&&d.IDBIndex&&d.IDBKeyRange&&d.IDBObjectStore))return h.return(hi(Error("Non-prefixed indexedDB APIs are missing")))}catch(l){return h.return(hi(l))}if(!("IDBTransaction"in self&&"objectStoreNames"in IDBTransaction.prototype))return h.return(hi(Error("IDBTransaction.prototype.objectStoreNames is missing")));ta(h,2);e={actualName:"yt-idb-test-do-not-use",publicName:"yt-idb-test-do-not-use",userIdentifier:void 0};return w(h,Zi(e),4);case 4:return w(h,$i("yt-idb-test-do-not-use"),5);
case 5:return h.return(new fi(!0));case 2:f=ua(h);if(!gi()){h.B(6);break}ta(h,7);return w(h,aj(),9);case 9:return g=h.i,h.return(hi(f,g));case 7:return ua(h),h.return(hi(f));case 6:return h.return(hi(f))}})})}
function fj(){if(void 0!==dj)return dj;ai=!0;return dj=ej().then(function(a){ai=!1;a.log();return a.isSupported()})}
;function gj(){var a=new S("AUTH_INVALID");bi(a);throw a;throw Error("Datasync ID not set");}
function hj(a,b,c,d){var e;return H(this,function g(){var h,k;return x(g,function(l){switch(l.h){case 1:return w(l,ij({caller:"openDbImpl",publicName:a,version:b}),2);case 2:return ji(a),c?h={actualName:a,publicName:a,userIdentifier:void 0}:h=gj(),h.clearDataOnAuthChange=null!==(e=d.clearDataOnAuthChange)&&void 0!==e?e:!1,ta(l,3),w(l,Zi(h),5);case 5:return w(l,Vi(h.actualName,b,d),6);case 6:return l.return(l.i);case 3:return k=ua(l),ta(l,7),w(l,$i(h.actualName),9);case 9:l.h=8;l.m=0;break;case 7:ua(l);
case 8:throw k;}})})}
function ij(a){return H(this,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,fj(),2);if(!e.i)throw d=new S("IDB_NOT_SUPPORTED",{context:a}),bi(d),d;e.h=0})})}
function jj(a,b,c){c=void 0===c?{}:c;return hj(a,b,!1,c)}
function kj(a,b,c){c=void 0===c?{}:c;return hj(a,b,!0,c)}
function lj(a,b){b=void 0===b?{}:b;return H(this,function d(){var e;return x(d,function(f){if(1==f.h)return w(f,fj(),2);if(3!=f.h){if(!f.i)return f.return();ji(a);e=gj();return w(f,Wi(e.actualName,b),3)}return w(f,$i(e.actualName),0)})})}
function mj(a,b){var c=this;a=a.map(function(d){return H(c,function f(){return x(f,function(g){return 1==g.h?w(g,Wi(d.actualName,b),2):w(g,$i(d.actualName),0)})})});
return Promise.all(a).then(function(){})}
function nj(){var a=void 0===a?{}:a;return H(this,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,fj(),2);if(3!=e.h){if(!e.i)return e.return();ji("LogsDatabaseV2");return w(e,cj(),3)}d=e.i;return w(e,mj(d,a),0)})})}
function oj(a,b){b=void 0===b?{}:b;return H(this,function d(){return x(d,function(e){if(1==e.h)return w(e,fj(),2);if(3!=e.h){if(!e.i)return e.return();ji(a);return w(e,Wi(a,b),3)}return w(e,$i(a),0)})})}
;function pj(a,b){Xi.call(this,a,b);this.options=b;ji(a)}
v(pj,Xi);pj.prototype.i=function(a,b,c){c=void 0===c?{}:c;return(this.options.Fa?kj:jj)(a,b,Object.assign(Object.assign({},c),{clearDataOnAuthChange:this.options.clearDataOnAuthChange}))};
pj.prototype.delete=function(a){a=void 0===a?{}:a;return(this.options.Fa?oj:lj)(this.name,a)};
function qj(a){var b;return function(){b||(b=new pj("LogsDatabaseV2",a));return b}}
;function rj(){T.call(this,function(){});
throw Error("Not allowed to instantiate the thennable outside of the core library.");}
v(rj,T);rj.reject=T.reject;rj.resolve=T.resolve;rj.all=T.all;var sj;function tj(){if(!sj){var a={};sj=qj({Ca:(a.LogsRequestsStore=!0,a.sapisid=!0,a.SWHealthLog=!0,a),Fa:!Q("nwl_use_ytidb_partitioning"),upgrade:function(b,c){2>c&&(Hi(b,"LogsRequestsStore",{keyPath:"id",autoIncrement:!0}).h.createIndex("newRequest",["status","authHash","interface","timestamp"],{unique:!1}),Hi(b,"sapisid"));3>c&&Hi(b,"SWHealthLog",{keyPath:"id",autoIncrement:!0}).h.createIndex("swHealthNewRequest",["interface","timestamp"],{unique:!1})},
version:3})}return sj().open()}
function uj(a){return H(this,function c(){var d,e,f,g,h;return x(c,function(k){switch(k.h){case 1:return d={startTime:R(),transactionType:"YT_IDB_TRANSACTION_TYPE_WRITE"},w(k,vj(),2);case 2:return e=k.i,w(k,tj(),3);case 3:return f=k.i,g=Object.assign(Object.assign({},a),{options:JSON.parse(JSON.stringify(a.options)),authHash:e,interface:F("INNERTUBE_CONTEXT_CLIENT_NAME",0)}),w(k,Ji(f,"LogsRequestsStore",g),4);case 4:return h=k.i,d.nb=R(),wj(d),k.return(h)}})})}
function xj(a){return H(this,function c(){var d,e,f,g,h,k,l,p;return x(c,function(n){switch(n.h){case 1:return d={startTime:R(),transactionType:"YT_IDB_TRANSACTION_TYPE_READ"},w(n,vj(),2);case 2:return e=n.i,f=F("INNERTUBE_CONTEXT_CLIENT_NAME",0),g=[a,e,f,0],h=[a,e,f,R()],k=IDBKeyRange.bound(g,h),w(n,tj(),3);case 3:return l=n.i,p=void 0,w(n,Fi(l,["LogsRequestsStore"],{mode:"readwrite",I:!0},function(r){return Si(Gi(r,"LogsRequestsStore").index("newRequest"),{query:k,direction:"prev"},function(q){q.getValue()&&
(p=q.getValue(),"NEW"===a&&(p.status="QUEUED",q.update(p)))})}),4);
case 4:return d.nb=R(),wj(d),n.return(p)}})})}
function yj(a){return H(this,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,tj(),2);d=e.i;return e.return(Fi(d,["LogsRequestsStore"],{mode:"readwrite",I:!0},function(f){var g=Gi(f,"LogsRequestsStore");return g.get(a).then(function(h){if(h)return h.status="QUEUED",V(g.h.put(h,void 0)).then(function(){return h})})}))})})}
function zj(a){return H(this,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,tj(),2);d=e.i;return e.return(Fi(d,["LogsRequestsStore"],{mode:"readwrite",I:!0},function(f){var g=Gi(f,"LogsRequestsStore");return g.get(a).then(function(h){return h?(h.status="NEW",h.sendCount+=1,V(g.h.put(h,void 0)).then(function(){return h})):rj.resolve(void 0)})}))})})}
function Aj(a){return H(this,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,tj(),2);d=e.i;return e.return(d.delete("LogsRequestsStore",a))})})}
function Bj(){return H(this,function b(){var c;return x(b,function(d){if(1==d.h)return w(d,tj(),2);c=d.i;return d.return(c.clear("LogsRequestsStore"))})})}
function Cj(){return H(this,function b(){var c;return x(b,function(d){if(1==d.h)return w(d,tj(),2);c=d.i;return d.return(c.clear("SWHealthLog"))})})}
function Dj(){return H(this,function b(){var c,d;return x(b,function(e){return 1==e.h?w(e,tj(),2):3!=e.h?(c=e.i,d=R()-2592E6,w(e,Fi(c,["LogsRequestsStore"],{mode:"readwrite",I:!0},function(f){return Pi(Gi(f,"LogsRequestsStore"),{},function(g){if(g.getValue().timestamp<=d)return g.delete().then(function(){return g.continue()})})}),3)):Q("web_clean_sw_logs_store")?w(e,Fi(c,["SWHealthLog"],{mode:"readwrite",
I:!0},function(f){return Pi(Gi(f,"SWHealthLog"),{},function(g){if(g.getValue().timestamp<=d)return g.delete().then(function(){return g.continue()})})}),0):e.B(0)})})}
function Ej(){return H(this,function b(){return x(b,function(c){return 1==c.h?w(c,nj(),2):w(c,oj("LogsDatabaseV2"),0)})})}
function vj(){return H(this,function b(){var c;return x(b,function(d){if(1==d.h){Zh.h||(Zh.h=new Zh);var e={};var f=hd([]);f&&(e.Authorization=f,f=void 0,void 0===f&&(f=Number(F("SESSION_INDEX",0)),f=isNaN(f)?0:f),e["X-Goog-AuthUser"]=f,"INNERTUBE_HOST_OVERRIDE"in of||(e["X-Origin"]=window.location.origin),Q("pageid_as_header_web")&&"DELEGATED_SESSION_ID"in of&&(e["X-Goog-PageId"]=F("DELEGATED_SESSION_ID")));e instanceof Ee||(f=new Ee(Ka),Fe(f,2,e),e=f);return w(d,e,2)}c=d.i;e=d.return;f=Fh(c);var g=
new zd;g.update(JSON.stringify(f,Object.keys(f).sort()));f=g.digest();g="";for(var h=0;h<f.length;h++)g+="0123456789ABCDEF".charAt(Math.floor(f[h]/16))+"0123456789ABCDEF".charAt(f[h]%16);return e.call(d,g)})})}
function Fj(a){return H(this,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,tj(),2);d=e.i;return w(e,Ji(d,"sapisid",a,"sapisid"),0)})})}
function Gj(){return H(this,function b(){var c,d;return x(b,function(e){if(1==e.h)return w(e,tj(),2);if(3!=e.h)return c=e.i,w(e,c.get("sapisid","sapisid"),3);d=e.i;return e.return(d||"")})})}
function wj(a){var b=xf("nwl_latency_sampling_rate",.01);.02<b||Math.random()<=b&&Sh("nwl_transaction_latency_payload",a)}
;var Hj=["__Secure-1PAPISID","SAPISID","__Secure-3PAPISID"];function Ij(){for(var a=u(Hj),b=a.next();!b.done;b=a.next())if(b=ed.get(b.value))return b;return"LOGGED_OUT"}
function Jj(){ue.call(this);this.pollingInterval=3E3;this.j=[null,null,null];this.m=!1;Kj(this)}
v(Jj,ue);function Lj(){Jj.h||(Jj.h=new Jj);var a=Jj.h;a.m=!0;a.verifyUser();Mj(a)}
Jj.prototype.verifyUser=function(){var a=Kj(this),b=a.Wa;if(!a.lb)return Mj(this),!0;ve(this,"ytsessionchange");b&&ve(this,"ytuserinvalid");Mj(this);return!1};
function Kj(a){var b=Hj.map(function(e){var f;return null!==(f=ed.get(e))&&void 0!==f?f:""}),c=b.some(function(e,f){return a.j&&""!==a.j[f]&&""===e}),d=b.some(function(e,f){return a.j&&a.j[f]!==e});
a.j=b;return{Wa:c,lb:d}}
function Mj(a){a.m&&(Nj(a),a.l=Nf(function(){a.verifyUser()},a.pollingInterval))}
function Nj(a){a.l&&(Tf(a.l),a.l=void 0)}
;var Oj;function Pj(){Oj||(Oj=new Gh("yt.offline"));return Oj}
function Qj(a){if(Q("offline_error_handling")){var b=Pj().get("errors",!0)||{};b[a.message]={name:a.name,stack:a.stack};a.level&&(b[a.message].level=a.level);Pj().set("errors",b,2592E3,!0)}}
;function Rj(){ue.call(this);this.m=this.C=this.G=this.l=!1;this.j=Sj();this.m=Q("validate_network_status");Tj(this);Uj(this)}
v(Rj,ue);function Sj(){var a=window.navigator.onLine;return void 0===a?!0:a}
function Uj(a){window.addEventListener("online",function(){return H(a,function c(){var d=this;return x(c,function(e){if(1==e.h)return d.m?w(e,Vj(d),2):(d.j=!0,d.l&&ve(d,"ytnetworkstatus-online"),e.B(2));Wj(d);if(d.C&&Q("offline_error_handling")){var f=Pj().get("errors",!0);if(f){for(var g in f)if(f[g]){var h=new ii(g,"sent via offline_errors");h.name=f[g].name;h.stack=f[g].stack;h.level=f[g].level;sf(h)}Pj().set("errors",{},2592E3,!0)}}e.h=0})})})}
function Tj(a){window.addEventListener("offline",function(){return H(a,function c(){var d=this;return x(c,function(e){if(1==e.h)return d.m?w(e,Vj(d),2):(d.j=!1,d.l&&ve(d,"ytnetworkstatus-offline"),e.B(2));Wj(d);e.h=0})})})}
function Wj(a){a.G&&(tf(new ii("NetworkStatusManager state did not match poll",R()-0)),a.G=!1)}
function Vj(a){return a.o?a.o:a.o=new Promise(function(b){return H(a,function d(){var e,f,g,h=this;return x(d,function(k){switch(k.h){case 1:return e=new AbortController,f=e.signal,g=!1,ta(k,2,3),h.J=Pf(function(){e.abort()},2E4),w(k,fetch("/generate_204",{method:"HEAD",
signal:f}),5);case 5:g=!0;case 3:va(k);h.o=void 0;Tf(h.J);g!==h.j&&(h.j=g,h.j&&h.l?ve(h,"ytnetworkstatus-online"):h.l&&ve(h,"ytnetworkstatus-offline"));b(g);wa(k);break;case 2:ua(k),g=!1,k.B(3)}})})})}
;function Xj(a){a=void 0===a?{}:a;ue.call(this);var b=this;this.l=this.o=0;Rj.h||(Rj.h=new Rj);this.j=Rj.h;this.j.l=!0;a.Va&&(this.j.C=!0);a.ga?(this.ga=a.ga,le(this.j,"ytnetworkstatus-online",function(){Yj(b,"publicytnetworkstatus-online")}),le(this.j,"ytnetworkstatus-offline",function(){Yj(b,"publicytnetworkstatus-offline")})):(le(this.j,"ytnetworkstatus-online",function(){ve(b,"publicytnetworkstatus-online")}),le(this.j,"ytnetworkstatus-offline",function(){ve(b,"publicytnetworkstatus-offline")}))}
v(Xj,ue);function Zj(){var a=ak().j;a.m||a.j===Sj()||tf(new ii("NetworkStatusManager isOnline does not match window status"));return a.j}
function Yj(a,b){a.ga?a.l?(Tf(a.o),a.o=Pf(function(){a.m!==b&&(ve(a,b),a.m=b,a.l=R())},a.ga-(R()-a.l))):(ve(a,b),a.m=b,a.l=R()):ve(a,b)}
;var bk=!1,ck=!1,dk=0,ek;function fk(){H(this,function b(){var c,d,e,f;return x(b,function(g){switch(g.h){case 1:return w(g,fj(),2);case 2:(c=g.i)&&(ck=!0);d=Q("networkless_logging");if(c&&d)return Q("nwl_use_ytidb_partitioning")?w(g,oj("LogsDatabaseV2"),8):w(g,nj(),8);if(!c){g.B(0);break}return w(g,Ej(),0);case 8:return Lj(),document.addEventListener("ytsessionchange",function(){gk()}),w(g,Gj(),11);
case 11:e=g.i;f=Ij();if(e===f){g.B(12);break}gk();return w(g,Fj(f),12);case 12:if(!(Q("enable_nwl_cleaning_logic")&&Math.random()<=xf("nwl_cleaning_rate",.1))){g.B(14);break}return w(g,Dj(),14);case 14:bk=!0;hk();Zj()&&ik();le(ak(),"publicytnetworkstatus-online",ik);le(ak(),"publicytnetworkstatus-offline",jk);if(!Q("networkless_immediately_drop_sw_health_store")){g.B(16);break}return w(g,kk(),16);case 16:if(Q("networkless_immediately_drop_all_requests"))return w(g,Ej(),0);g.B(0)}})})}
function lk(a,b){function c(d){var e=Zj();if(!bk||!d||e&&Q("vss_networkless_bypass_write"))vg(a,b);else{var f={url:a,options:b,timestamp:R(),status:"NEW",sendCount:0};uj(f).then(function(g){f.id=g;(Zj()||Q("networkless_always_online"))&&mk(f)}).catch(function(g){mk(f);
Zj()?sf(g):Qj(g)})}}
b=void 0===b?{}:b;Q("skip_is_supported_killswitch")?fj().then(function(d){c(d)}):c(ck)}
function nk(a,b){function c(d){if(bk&&d){var e={url:a,options:b,timestamp:R(),status:"NEW",sendCount:0},f=!1,g=b.onSuccess?b.onSuccess:function(){};
e.options.onSuccess=function(h,k){void 0!==e.id?Aj(e.id):f=!0;g(h,k)};
vg(e.url,e.options);uj(e).then(function(h){e.id=h;f&&Aj(e.id)}).catch(function(h){Zj()?sf(h):Qj(h)})}else vg(a,b)}
b=void 0===b?{}:b;Q("skip_is_supported_killswitch")?fj().then(function(d){c(d)}):c(ck)}
function ik(){var a=this;dk||(dk=Pf(function(){return H(a,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,xj("NEW"),2);if(3!=e.h)return d=e.i,d?w(e,mk(d),3):(jk(),e.return());dk=0;ik();e.h=0})})},100))}
function jk(){Tf(dk);dk=0}
function mk(a){return H(this,function c(){var d;return x(c,function(e){switch(e.h){case 1:if(void 0===a.id){e.B(2);break}return w(e,yj(a.id),3);case 3:(d=e.i)?a=d:tf(Error("The request cannot be found in the database."));case 2:if(ok(a,2592E6)){e.B(4);break}tf(Error("Networkless Logging: Stored logs request expired age limit"));if(void 0===a.id){e.B(5);break}return w(e,Aj(a.id),5);case 5:return e.return();case 4:var f=a=pk(a),g,h;if(null===(h=null===(g=null===f||void 0===f?void 0:f.options)||void 0===
g?void 0:g.postParams)||void 0===h?0:h.requestTimeMs)f.options.postParams.requestTimeMs=Math.round(R());(a=f)&&vg(a.url,a.options);e.h=0}})})}
function pk(a){var b=this,c=a.options.onError?a.options.onError:function(){};
a.options.onError=function(e,f){return H(b,function h(){return x(h,function(k){if(1==k.h)return void 0===(null===a||void 0===a?void 0:a.id)?k.B(2):1>a.sendCount?w(k,zj(a.id),6):w(k,Aj(a.id),2);2!=k.h&&Pf(function(){Zj()&&ik()},5E3);
c(e,f);k.h=0})})};
var d=a.options.onSuccess?a.options.onSuccess:function(){};
a.options.onSuccess=function(e,f){return H(b,function h(){return x(h,function(k){if(1==k.h)return void 0===(null===a||void 0===a?void 0:a.id)?k.B(2):w(k,Aj(a.id),2);d(e,f);k.h=0})})};
return a}
function ok(a,b){a=a.timestamp;return R()-a>=b?!1:!0}
function hk(){var a=this;xj("QUEUED").then(function(b){b&&!ok(b,12E4)&&Pf(function(){return H(a,function d(){return x(d,function(e){if(1==e.h)return void 0===b.id?e.B(2):w(e,zj(b.id),2);hk();e.h=0})})})})}
function gk(){Bj().catch(function(a){sf(a)})}
function kk(){return H(this,function b(){return x(b,function(c){return c.return(Cj().catch(function(d){sf(d)}))})})}
function ak(){ek||(ek=new Xj({Va:!0}));return ek}
;function qk(a){var b=this;this.h=null;a?this.h=a:Dh()&&(this.h=nh());Nf(function(){Lh(b)},5E3)}
qk.prototype.isReady=function(){!this.h&&Dh()&&(this.h=nh());return!!this.h};
function qh(a,b,c,d){function e(r){r=void 0===r?!1:r;var q;if(d.retry&&"www.youtube-nocookie.com"!=h&&(r||(q=Jh(b,c,l,k)),q)){var B=g.onSuccess,I=g.onFetchSuccess;g.onSuccess=function(J,ba){Kh(q);B(J,ba)};
c.onFetchSuccess=function(J,ba){Kh(q);I(J,ba)}}try{r&&d.retry&&!d.Ba.bypassNetworkless?(g.method="POST",!d.Ba.writeThenSend&&Q("nwl_send_fast_on_unload")?nk(n,g):lk(n,g)):(g.method="POST",g.postParams||(g.postParams={}),vg(n,g))}catch(J){if("InvalidAccessError"==J.name)q&&(Kh(q),q=0),tf(Error("An extension is blocking network request."));
else throw J;}q&&Nf(function(){Lh(a)},5E3)}
!F("VISITOR_DATA")&&"visitor_id"!==b&&.01>Math.random()&&tf(new ii("Missing VISITOR_DATA when sending innertube request.",b,c,d));if(!a.isReady()){var f=new ii("innertube xhrclient not ready",b,c,d);sf(f);throw f;}var g={headers:{"Content-Type":"application/json"},method:"POST",postParams:c,postBodyFormat:"JSON",onTimeout:function(){d.onTimeout()},
onFetchTimeout:d.onTimeout,onSuccess:function(r,q){if(d.onSuccess)d.onSuccess(q)},
onFetchSuccess:function(r){if(d.onSuccess)d.onSuccess(r)},
onError:function(r,q){if(d.onError)d.onError(q)},
onFetchError:function(r){if(d.onError)d.onError(r)},
timeout:d.timeout,withCredentials:!0},h="";(f=a.h.Sa)&&(h=f);var k=a.h.Ua||!1,l=Eh(k,h,d);Object.assign(g.headers,l);g.headers.Authorization&&!h&&(g.headers["x-origin"]=window.location.origin);f="/youtubei/"+a.h.innertubeApiVersion+"/"+b;var p={alt:"json"};a.h.Ta&&g.headers.Authorization||(p.key=a.h.innertubeApiKey);var n=jg(""+h+f,p||{},!0);bk?fj().then(function(r){e(r)}):e(!1)}
;function rk(a,b,c){c=void 0===c?{}:c;var d=qk;F("ytLoggingEventsDefaultDisabled",!1)&&qk==qk&&(d=null);sh(a,b,d,c)}
;var sk=[{za:function(a){return"Cannot read property '"+a.key+"'"},
qa:{TypeError:[{regexp:/Cannot read property '([^']+)' of (null|undefined)/,groups:["key","value"]},{regexp:/\u65e0\u6cd5\u83b7\u53d6\u672a\u5b9a\u4e49\u6216 (null|undefined) \u5f15\u7528\u7684\u5c5e\u6027\u201c([^\u201d]+)\u201d/,groups:["value","key"]},{regexp:/\uc815\uc758\ub418\uc9c0 \uc54a\uc74c \ub610\ub294 (null|undefined) \ucc38\uc870\uc778 '([^']+)' \uc18d\uc131\uc744 \uac00\uc838\uc62c \uc218 \uc5c6\uc2b5\ub2c8\ub2e4./,groups:["value","key"]},{regexp:/No se puede obtener la propiedad '([^']+)' de referencia nula o sin definir/,
groups:["key"]},{regexp:/Unable to get property '([^']+)' of (undefined or null) reference/,groups:["key","value"]}],Error:[{regexp:/(Permission denied) to access property "([^']+)"/,groups:["reason","key"]}]}},{za:function(a){return"Cannot call '"+a.key+"'"},
qa:{TypeError:[{regexp:/(?:([^ ]+)?\.)?([^ ]+) is not a function/,groups:["base","key"]},{regexp:/([^ ]+) called on (null or undefined)/,groups:["key","value"]},{regexp:/Object (.*) has no method '([^ ]+)'/,groups:["base","key"]},{regexp:/Object doesn't support property or method '([^ ]+)'/,groups:["key"]},{regexp:/\u30aa\u30d6\u30b8\u30a7\u30af\u30c8\u306f '([^']+)' \u30d7\u30ed\u30d1\u30c6\u30a3\u307e\u305f\u306f\u30e1\u30bd\u30c3\u30c9\u3092\u30b5\u30dd\u30fc\u30c8\u3057\u3066\u3044\u307e\u305b\u3093/,
groups:["key"]},{regexp:/\uac1c\uccb4\uac00 '([^']+)' \uc18d\uc131\uc774\ub098 \uba54\uc11c\ub4dc\ub97c \uc9c0\uc6d0\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4./,groups:["key"]}]}}];function tk(){this.h=[];this.i=[]}
var uk;function vk(){uk||(uk=new tk);return uk}
;var wk=new M;function xk(a){function b(){return a.charCodeAt(d++)}
var c=a.length,d=0;do{var e=yk(b);if(Infinity===e)break;var f=e>>3;switch(e&7){case 0:e=yk(b);if(2===f)return e;break;case 1:if(2===f)return;d+=8;break;case 2:e=yk(b);if(2===f)return a.substr(d,e);d+=e;break;case 5:if(2===f)return;d+=4;break;default:return}}while(d<c)}
function yk(a){var b=a(),c=b&127;if(128>b)return c;b=a();c|=(b&127)<<7;if(128>b)return c;b=a();c|=(b&127)<<14;if(128>b)return c;b=a();return 128>b?c|(b&127)<<21:Infinity}
;function zk(a,b,c,d){if(a)if(Array.isArray(a)){var e=d;for(d=0;d<a.length&&!(a[d]&&(e+=Ak(d,a[d],b,c),500<e));d++);d=e}else if("object"===typeof a)for(e in a){if(a[e]){var f=e;var g=a[e],h=b,k=c;f="string"!==typeof g||"clickTrackingParams"!==f&&"trackingParams"!==f?0:(g=xk(atob(g.replace(/-/g,"+").replace(/_/g,"/"))))?Ak(f+".ve",g,h,k):0;d+=f;d+=Ak(e,a[e],b,c);if(500<d)break}}else c[b]=Bk(a),d+=c[b].length;else c[b]=Bk(a),d+=c[b].length;return d}
function Ak(a,b,c,d){c+="."+a;a=Bk(b);d[c]=a;return c.length+a.length}
function Bk(a){return("string"===typeof a?a:String(JSON.stringify(a))).substr(0,500)}
;var Ck=new Set,Dk=0,Ek=0,Fk=0,Gk=[],Hk=["PhantomJS","Googlebot","TO STOP THIS SECURITY SCAN go/scan"];function Ik(a){Jk(a,"WARNING")}
function Jk(a,b,c,d,e,f){f=void 0===f?{}:f;f.name=c||F("INNERTUBE_CONTEXT_CLIENT_NAME",1);f.version=d||F("INNERTUBE_CONTEXT_CLIENT_VERSION",void 0);c=f||{};b=void 0===b?"ERROR":b;b=void 0===b?"ERROR":b;if(a&&(a.hasOwnProperty("level")&&a.level&&(b=a.level),Q("console_log_js_exceptions")&&(d=[],d.push("Name: "+a.name),d.push("Message: "+a.message),a.hasOwnProperty("params")&&d.push("Error Params: "+JSON.stringify(a.params)),a.hasOwnProperty("args")&&d.push("Error args: "+JSON.stringify(a.args)),d.push("File name: "+
a.fileName),d.push("Stacktrace: "+a.stack),window.console.log(d.join("\n"),a)),!(5<=Dk))){var g=Bd(a);d=g.message||"Unknown Error";e=g.name||"UnknownError";var h=g.stack||a.i||"Not available";h.startsWith(e+": "+d)&&(f=h.split("\n"),f.shift(),h=f.join("\n"));f=g.lineNumber||"Not available";g=g.fileName||"Not available";var k=0;if(a.hasOwnProperty("args")&&a.args&&a.args.length)for(var l=0;l<a.args.length&&!(k=zk(a.args[l],"params."+l,c,k),500<=k);l++);else if(a.hasOwnProperty("params")&&a.params){var p=
a.params;if("object"===typeof a.params)for(l in p){if(p[l]){var n="params."+l,r=Bk(p[l]);c[n]=r;k+=n.length+r.length;if(500<k)break}}else c.params=Bk(p)}if(Gk.length)for(l=0;l<Gk.length&&!(k=zk(Gk[l],"params.context."+l,c,k),500<=k);l++);navigator.vendor&&!c.hasOwnProperty("vendor")&&(c["device.vendor"]=navigator.vendor);l={message:d,name:e,lineNumber:f,fileName:g,stack:h,params:c,sampleWeight:1};c=Number(a.columnNumber);isNaN(c)||(l.lineNumber=l.lineNumber+":"+c);if("IGNORED"===a.level)a=0;else a:{a=
vk();c=u(a.i);for(d=c.next();!d.done;d=c.next())if(d=d.value,l.message&&l.message.match(d.Jk)){a=d.weight;break a}a=u(a.h);for(c=a.next();!c.done;c=a.next())if(c=c.value,c.Ia(l)){a=c.weight;break a}a=1}l.sampleWeight=a;a=u(sk);for(c=a.next();!c.done;c=a.next())if(c=c.value,c.qa[l.name])for(e=u(c.qa[l.name]),d=e.next();!d.done;d=e.next())if(f=d.value,d=l.message.match(f.regexp)){l.params["params.error.original"]=d[0];e=f.groups;f={};for(g=0;g<e.length;g++)f[e[g]]=d[g+1],l.params["params.error."+e[g]]=
d[g+1];l.message=c.za(f);break}l.params||(l.params={});a=vk();l.params["params.errorServiceSignature"]="msg="+a.i.length+"&cb="+a.h.length;l.params["params.serviceWorker"]="false";y.document&&y.document.querySelectorAll&&(l.params["params.fscripts"]=String(document.querySelectorAll("script:not([nonce])").length));window.yterr&&"function"===typeof window.yterr&&window.yterr(l);if(0!==l.sampleWeight&&!Ck.has(l.message)){"ERROR"===b?(wk.R("handleError",l),Q("record_app_crashed_web")&&0===Fk&&1===l.sampleWeight&&
(Fk++,rk("appCrashed",{appCrashType:"APP_CRASH_TYPE_BREAKPAD"})),Ek++):"WARNING"===b&&wk.R("handleWarning",l);if(Q("kevlar_gel_error_routing")){a=b;b:{c=u(Hk);for(d=c.next();!d.done;d=c.next())if(Eg(d.value.toLowerCase())){c=!0;break b}c=!1}if(c)c=void 0;else{d={stackTrace:l.stack};l.fileName&&(d.filename=l.fileName);c=l.lineNumber&&l.lineNumber.split?l.lineNumber.split(":"):[];0!==c.length&&(1!==c.length||isNaN(Number(c[0]))?2!==c.length||isNaN(Number(c[0]))||isNaN(Number(c[1]))||(d.lineNumber=Number(c[0]),
d.columnNumber=Number(c[1])):d.lineNumber=Number(c[0]));c={level:"ERROR_LEVEL_UNKNOWN",message:l.message,errorClassName:l.name,sampleWeight:l.sampleWeight};"ERROR"===a?c.level="ERROR_LEVEL_ERROR":"WARNING"===a&&(c.level="ERROR_LEVEL_WARNNING");d={isObfuscated:!0,browserStackInfo:d};e={pageUrl:window.location.href,kvPairs:[]};F("FEXP_EXPERIMENTS")&&(e.experimentIds=F("FEXP_EXPERIMENTS"));if(f=l.params)for(g=u(Object.keys(f)),h=g.next();!h.done;h=g.next())h=h.value,e.kvPairs.push({key:"client."+h,value:String(f[h])});
f=F("SERVER_NAME",void 0);g=F("SERVER_VERSION",void 0);f&&g&&(e.kvPairs.push({key:"server.name",value:f}),e.kvPairs.push({key:"server.version",value:g}));c={errorMetadata:e,stackTrace:d,logMessage:c}}c&&(rk("clientError",c),("ERROR"===a||Q("errors_flush_gel_always_killswitch"))&&ih())}if(!Q("suppress_error_204_logging")){a=l.params||{};b={urlParams:{a:"logerror",t:"jserror",type:l.name,msg:l.message.substr(0,250),line:l.lineNumber,level:b,"client.name":a.name},postParams:{url:F("PAGE_NAME",window.location.href),
file:l.fileName},method:"POST"};a.version&&(b["client.version"]=a.version);if(b.postParams){l.stack&&(b.postParams.stack=l.stack);c=u(Object.keys(a));for(d=c.next();!d.done;d=c.next())d=d.value,b.postParams["client."+d]=a[d];if(a=F("LATEST_ECATCHER_SERVICE_TRACKING_PARAMS",void 0))for(c=u(Object.keys(a)),d=c.next();!d.done;d=c.next())d=d.value,b.postParams[d]=a[d];a=F("SERVER_NAME",void 0);c=F("SERVER_VERSION",void 0);a&&c&&(b.postParams["server.name"]=a,b.postParams["server.version"]=c)}vg(F("ECATCHER_REPORT_HOST",
"")+"/error_204",b)}Ck.add(l.message);Dk++}}}
function Kk(a,b){for(var c=[],d=1;d<arguments.length;++d)c[d-1]=arguments[d];a.args||(a.args=[]);a.args.push.apply(a.args,c instanceof Array?c:ha(u(c)))}
;var Lk={Ub:29434,Xb:3611,Ne:3854,hg:42993,Pi:4724,Aj:96370,ob:27686,pb:85013,qb:23462,sb:42016,tb:62407,ub:26926,rb:43781,vb:51236,wb:79148,xb:50160,yb:77504,Kb:87907,Lb:18630,Mb:54445,Nb:80935,Ob:105675,Pb:37521,Qb:47786,Rb:98349,Sb:123695,Tb:6827,Vb:7282,Wb:124448,ac:32276,Zb:76278,cc:93911,dc:106531,ec:27259,fc:27262,hc:27263,jc:21759,kc:27107,lc:62936,mc:49568,nc:38408,oc:80637,pc:68727,qc:68728,sc:80353,tc:80356,uc:74610,wc:45707,xc:83962,yc:83970,zc:46713,Ac:89711,Bc:74612,Cc:93265,Dc:74611,
Fc:113533,Gc:93252,Hc:99357,Jc:94521,Kc:114252,Lc:113532,Mc:94522,Ic:94583,Nc:88E3,Oc:93253,Pc:93254,Qc:94387,Rc:94388,Sc:93255,Tc:97424,Ec:72502,Uc:110111,Vc:76019,Xc:117092,Yc:117093,Wc:89431,Zc:110466,bd:77240,cd:60508,dd:105350,ed:73393,fd:113534,gd:92098,hd:84517,jd:83759,kd:80357,ld:86113,md:72598,nd:72733,od:107349,pd:124275,qd:118203,rd:117431,sd:117429,td:117430,ud:117432,vd:120080,wd:117259,xd:121692,yd:97615,zd:31402,Ad:84774,Bd:95117,Cd:98930,Dd:98931,Ed:98932,Fd:43347,Gd:45474,Hd:100352,
Id:84758,Jd:98443,Kd:117985,Ld:74613,Md:74614,Nd:64502,Od:74615,Pd:74616,Qd:122224,Rd:74617,Sd:77820,Td:74618,Ud:93278,Vd:93274,Wd:93275,Xd:93276,Yd:22110,Zd:29433,be:120541,de:82047,ee:113550,ge:75836,he:75837,ie:42352,je:84512,ke:76065,le:75989,me:16623,ne:32594,oe:27240,pe:32633,qe:74858,se:3945,re:16989,te:45520,ue:25488,we:25492,xe:25494,ye:55760,ze:14057,Ae:18451,Be:57204,Ce:57203,De:17897,Ee:57205,Fe:18198,Ge:17898,He:17909,Ie:43980,Je:46220,Ke:11721,Le:49954,Me:96369,Oe:56251,Pe:25624,Qe:16906,
Re:99999,Se:68172,Te:27068,Ue:47973,Ve:72773,We:26970,Xe:26971,Ye:96805,Ze:17752,af:73233,bf:109512,cf:22256,df:14115,ef:22696,ff:89278,gf:89277,hf:109513,jf:43278,kf:43459,lf:43464,mf:89279,nf:43717,pf:55764,qf:22255,rf:89281,sf:40963,tf:43277,uf:43442,vf:91824,wf:120137,xf:96367,yf:36850,zf:72694,Af:37414,Bf:36851,Df:124863,Cf:121343,Ef:73491,Ff:54473,Gf:43375,Hf:46674,If:32473,Jf:72901,Kf:72906,Lf:50947,Mf:50612,Nf:50613,Of:50942,Pf:84938,Qf:84943,Rf:84939,Sf:84941,Tf:84944,Uf:84940,Vf:84942,Wf:35585,
Xf:51926,Yf:79983,Zf:63238,ag:18921,cg:63241,dg:57893,eg:41182,fg:33424,gg:22207,ig:36229,jg:22206,kg:22205,lg:18993,mg:19001,ng:18990,og:18991,pg:18997,qg:18725,rg:19003,sg:36874,tg:44763,ug:33427,vg:67793,wg:22182,xg:37091,yg:34650,zg:50617,Ag:47261,Bg:22287,Cg:25144,Dg:97917,Eg:62397,Fg:36961,Gg:108035,Hg:27426,Ig:27857,Jg:27846,Kg:27854,Lg:69692,Mg:61411,Ng:39299,Og:38696,Pg:62520,Qg:36382,Rg:108701,Sg:50663,Tg:36387,Ug:14908,Vg:37533,Wg:105443,Xg:61635,Yg:62274,Zg:65702,ah:65703,bh:65701,dh:76256,
eh:37671,fh:49953,hh:36216,ih:28237,jh:39553,kh:29222,lh:26107,mh:38050,nh:26108,ph:120745,oh:26109,qh:26110,rh:66881,sh:28236,th:14586,uh:57929,vh:74723,wh:44098,xh:44099,yh:23528,zh:61699,Ah:59149,Bh:101951,Ch:97346,Dh:118051,Eh:95102,Fh:64882,Gh:119505,Hh:63595,Ih:63349,Jh:95101,Kh:75240,Lh:27039,Mh:68823,Nh:21537,Oh:83464,Ph:75707,Qh:83113,Rh:101952,Sh:101953,Uh:79610,Vh:24402,Wh:24400,Xh:32925,Yh:57173,Zh:122502,ai:64423,bi:64424,ci:33986,di:100828,fi:21409,gi:11070,hi:11074,ii:17880,ji:14001,
li:30709,mi:30707,ni:30711,oi:30710,ri:30708,ki:26984,si:63648,ti:63649,vi:51879,wi:111059,xi:5754,yi:20445,zi:110386,Ai:113746,Bi:66557,Ci:17310,Di:28631,Ei:21589,Fi:68012,Gi:60480,Hi:31571,Ii:76980,Ji:41577,Ki:45469,Li:38669,Mi:13768,Ni:13777,Oi:62985,Qi:59369,Ri:43927,Si:43928,Ti:12924,Ui:100355,Xi:56219,Yi:27669,Zi:10337,Wi:47896,aj:122629,bj:121258,cj:107598,dj:96639,ej:107536,fj:96661,gj:96658,hj:116646,ij:121122,jj:96660,kj:104443,lj:96659,mj:106442,nj:63667,oj:63668,pj:63669,qj:78314,rj:55761,
sj:96368,tj:67374,uj:48992,vj:49956,wj:31961,xj:26388,yj:23811,zj:5E4,Bj:47355,Cj:47356,Dj:37935,Ej:45521,Fj:21760,Gj:83769,Hj:49977,Ij:49974,Jj:93497,Kj:93498,Lj:34325,Mj:115803,Nj:123707,Oj:100081,Pj:35309,Qj:68314,Rj:25602,Sj:100339,Tj:59018,Uj:18248,Vj:50625,Wj:9729,Xj:37168,Yj:37169,Zj:21667,ak:16749,bk:18635,ck:39305,dk:18046,ek:53969,fk:8213,gk:93926,hk:102852,ik:110099,jk:22678,kk:69076,mk:100856,nk:17736,pk:3832,qk:55759,rk:64031,sk:93044,tk:93045,uk:34388,vk:17657,wk:17655,xk:39579,yk:39578,
zk:77448,Ak:8196,Bk:11357,Ck:69877,Dk:8197,Ek:82039};function Mk(a,b,c){L.call(this);var d=this;c=c||F("POST_MESSAGE_ORIGIN",void 0)||window.document.location.protocol+"//"+window.document.location.hostname;this.j=b||null;this.C="*";this.l=c;this.sessionId=null;this.channel="widget";this.G=!!a;this.A=function(e){a:if(!("*"!=d.l&&e.origin!=d.l||d.j&&e.source!=d.j||"string"!==typeof e.data)){try{var f=JSON.parse(e.data)}catch(g){break a}if(!(null==f||d.G&&(d.sessionId&&d.sessionId!=f.id||d.channel&&d.channel!=f.channel))&&f)switch(f.event){case "listening":"null"!=
e.origin&&(d.l=d.C=e.origin);d.j=e.source;d.sessionId=f.id;d.i&&(d.i(),d.i=null);break;case "command":d.m&&(!d.o||0<=$a(d.o,f.func))&&d.m(f.func,f.args,e.origin)}}};
this.o=this.i=this.m=null;window.addEventListener("message",this.A)}
v(Mk,L);Mk.prototype.sendMessage=function(a,b){if(b=b||this.j){this.sessionId&&(a.id=this.sessionId);this.channel&&(a.channel=this.channel);try{var c=JSON.stringify(a);b.postMessage(c,this.C)}catch(d){tf(d)}}};
Mk.prototype.D=function(){window.removeEventListener("message",this.A);L.prototype.D.call(this)};function Nk(){this.l=[];this.isReady=!1;this.u={};var a=this.i=new Mk(!!F("WIDGET_ID_ENFORCE")),b=this.bb.bind(this);a.m=b;a.o=null;this.i.channel="widget";if(a=F("WIDGET_ID"))this.i.sessionId=a}
m=Nk.prototype;m.bb=function(a,b,c){"addEventListener"===a&&b?(a=b[0],this.u[a]||"onReady"===a||(this.addEventListener(a,Ok(this,a)),this.u[a]=!0)):this.ra(a,b,c)};
m.ra=function(){};
function Ok(a,b){return function(c){return a.sendMessage(b,c)}}
m.addEventListener=function(){};
m.Ma=function(){this.isReady=!0;this.sendMessage("initialDelivery",this.la());this.sendMessage("onReady");E(this.l,this.Ea,this);this.l=[]};
m.la=function(){return null};
function Pk(a,b){a.sendMessage("infoDelivery",b)}
m.Ea=function(a){this.isReady?this.i.sendMessage(a):this.l.push(a)};
m.sendMessage=function(a,b){this.Ea({event:a,info:void 0===b?null:b})};
m.dispose=function(){this.i=null};function Qk(a){return(0===a.search("cue")||0===a.search("load"))&&"loadModule"!==a}
function Rk(a,b,c){"string"===typeof a&&(a={mediaContentUrl:a,startSeconds:b,suggestedQuality:c});a:{if((b=a.mediaContentUrl)&&(b=/\/([ve]|embed)\/([^#?]+)/.exec(b))&&b[2]){b=b[2];break a}b=null}a.videoId=b;return Sk(a)}
function Sk(a,b,c){if("string"===typeof a)return{videoId:a,startSeconds:b,suggestedQuality:c};b=["endSeconds","startSeconds","mediaContentUrl","suggestedQuality","videoId"];c={};for(var d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}
function Tk(a,b,c,d){if(Oa(a)&&!Array.isArray(a)){b="playlist list listType index startSeconds suggestedQuality".split(" ");c={};for(d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}b={index:b,startSeconds:c,suggestedQuality:d};"string"===typeof a&&16===a.length?b.list="PL"+a:b.playlist=a;return b}
;function Uk(a){Nk.call(this);this.h=a;this.j=[];this.addEventListener("onReady",C(this.Ya,this));this.addEventListener("onVideoProgress",C(this.ib,this));this.addEventListener("onVolumeChange",C(this.jb,this));this.addEventListener("onApiChange",C(this.cb,this));this.addEventListener("onPlaybackQualityChange",C(this.fb,this));this.addEventListener("onPlaybackRateChange",C(this.gb,this));this.addEventListener("onStateChange",C(this.hb,this));this.addEventListener("onWebglSettingsChanged",C(this.kb,
this))}
v(Uk,Nk);m=Uk.prototype;m.ra=function(a,b,c){if(this.h.isExternalMethodAvailable(a,c)){b=b||[];if(0<b.length&&Qk(a)){var d=b;if(Oa(d[0])&&!Array.isArray(d[0]))d=d[0];else{var e={};switch(a){case "loadVideoById":case "cueVideoById":e=Sk.apply(window,d);break;case "loadVideoByUrl":case "cueVideoByUrl":e=Rk.apply(window,d);break;case "loadPlaylist":case "cuePlaylist":e=Tk.apply(window,d)}d=e}b.length=1;b[0]=d}this.h.handleExternalCall(a,b,c);Qk(a)&&Pk(this,this.la())}};
m.Ya=function(){var a=this.Ma.bind(this);this.i.i=a};
m.addEventListener=function(a,b){this.j.push({eventType:a,listener:b});this.h.addEventListener(a,b)};
m.la=function(){if(!this.h)return null;var a=this.h.getApiInterface();eb(a,"getVideoData");for(var b={apiInterface:a},c=0,d=a.length;c<d;c++){var e=a[c];if(0===e.search("get")||0===e.search("is")){var f=0;0===e.search("get")?f=3:0===e.search("is")&&(f=2);f=e.charAt(f).toLowerCase()+e.substr(f+1);try{var g=this.h[e]();b[f]=g}catch(h){}}}b.videoData=this.h.getVideoData();b.currentTimeLastUpdated_=Date.now()/1E3;return b};
m.hb=function(a){a={playerState:a,currentTime:this.h.getCurrentTime(),duration:this.h.getDuration(),videoData:this.h.getVideoData(),videoStartBytes:0,videoBytesTotal:this.h.getVideoBytesTotal(),videoLoadedFraction:this.h.getVideoLoadedFraction(),playbackQuality:this.h.getPlaybackQuality(),availableQualityLevels:this.h.getAvailableQualityLevels(),currentTimeLastUpdated_:Date.now()/1E3,playbackRate:this.h.getPlaybackRate(),mediaReferenceTime:this.h.getMediaReferenceTime()};this.h.getVideoUrl&&(a.videoUrl=
this.h.getVideoUrl());this.h.getVideoContentRect&&(a.videoContentRect=this.h.getVideoContentRect());this.h.getProgressState&&(a.progressState=this.h.getProgressState());this.h.getPlaylist&&(a.playlist=this.h.getPlaylist());this.h.getPlaylistIndex&&(a.playlistIndex=this.h.getPlaylistIndex());this.h.getStoryboardFormat&&(a.storyboardFormat=this.h.getStoryboardFormat());Pk(this,a)};
m.fb=function(a){Pk(this,{playbackQuality:a})};
m.gb=function(a){Pk(this,{playbackRate:a})};
m.cb=function(){for(var a=this.h.getOptions(),b={namespaces:a},c=0,d=a.length;c<d;c++){var e=a[c],f=this.h.getOptions(e);b[e]={options:f};for(var g=0,h=f.length;g<h;g++){var k=f[g],l=this.h.getOption(e,k);b[e][k]=l}}this.sendMessage("apiInfoDelivery",b)};
m.jb=function(){Pk(this,{muted:this.h.isMuted(),volume:this.h.getVolume()})};
m.ib=function(a){a={currentTime:a,videoBytesLoaded:this.h.getVideoBytesLoaded(),videoLoadedFraction:this.h.getVideoLoadedFraction(),currentTimeLastUpdated_:Date.now()/1E3,playbackRate:this.h.getPlaybackRate(),mediaReferenceTime:this.h.getMediaReferenceTime()};this.h.getProgressState&&(a.progressState=this.h.getProgressState());Pk(this,a)};
m.kb=function(){var a={sphericalProperties:this.h.getSphericalProperties()};Pk(this,a)};
m.dispose=function(){Nk.prototype.dispose.call(this);for(var a=0;a<this.j.length;a++){var b=this.j[a];this.h.removeEventListener(b.eventType,b.listener)}this.j=[]};function Vk(){var a=pb(Wk),b;return Le(new Ee(function(c,d){a.onSuccess=function(e){pg(e)?c(new Xk(e)):d(new Yk("Request failed, status="+(e&&"status"in e?e.status:-1),"net.badstatus",e))};
a.onError=function(e){d(new Yk("Unknown request error","net.unknown",e))};
a.onTimeout=function(e){d(new Yk("Request timed out","net.timeout",e))};
b=vg("//googleads.g.doubleclick.net/pagead/id",a)}),function(c){c instanceof Me&&b.abort();
return Je(c)})}
function Yk(a,b,c){Xa.call(this,a+", errorCode="+b);this.errorCode=b;this.xhr=c;this.name="PromiseAjaxError"}
v(Yk,Xa);function Xk(a){this.xhr=a}
;function Zk(){this.i=0;this.h=null}
Zk.prototype.then=function(a,b,c){return 1===this.i&&a?(a=a.call(c,this.h),De(a)?a:$k(a)):2===this.i&&b?(a=b.call(c,this.h),De(a)?a:al(a)):this};
Zk.prototype.getValue=function(){return this.h};
Zk.prototype.$goog_Thenable=!0;function al(a){var b=new Zk;a=void 0===a?null:a;b.i=2;b.h=void 0===a?null:a;return b}
function $k(a){var b=new Zk;a=void 0===a?null:a;b.i=1;b.h=void 0===a?null:a;return b}
;function bl(a){Xa.call(this,a.message||a.description||a.name);this.isMissing=a instanceof cl;this.isTimeout=a instanceof Yk&&"net.timeout"==a.errorCode;this.isCanceled=a instanceof Me}
v(bl,Xa);bl.prototype.name="BiscottiError";function cl(){Xa.call(this,"Biscotti ID is missing from server")}
v(cl,Xa);cl.prototype.name="BiscottiMissingError";var Wk={format:"RAW",method:"GET",timeout:5E3,withCredentials:!0},dl=null;function $f(){if(Q("condition_biscotti_fetch_on_consent_cookie_html5_clients")&&!ed.get("CONSENT","").startsWith("YES+"))return Je(Error("User has not consented - not fetching biscotti id."));if("1"==nb())return Je(Error("Biscotti ID is not available in private embed mode"));dl||(dl=Le(Vk().then(el),function(a){return fl(2,a)}));
return dl}
function el(a){a=a.xhr.responseText;if(0!=a.lastIndexOf(")]}'",0))throw new cl;a=JSON.parse(a.substr(4));if(1<(a.type||1))throw new cl;a=a.id;ag(a);dl=$k(a);gl(18E5,2);return a}
function fl(a,b){b=new bl(b);ag("");dl=al(b);0<a&&gl(12E4,a-1);throw b;}
function gl(a,b){Jf(function(){Le(Vk().then(el,function(c){return fl(b,c)}),Ka)},a)}
function hl(){try{var a=A("yt.ads.biscotti.getId_");return a?a():$f()}catch(b){return Je(b)}}
;function il(a){if("1"!=nb()){a&&Zf();try{hl().then(function(){},function(){}),Jf(il,18E5)}catch(b){sf(b)}}}
;var jl=Date.now().toString();
function kl(){a:{if(window.crypto&&window.crypto.getRandomValues)try{var a=Array(16),b=new Uint8Array(16);window.crypto.getRandomValues(b);for(var c=0;c<a.length;c++)a[c]=b[c];var d=a;break a}catch(e){}d=Array(16);for(a=0;16>a;a++){b=Date.now();for(c=0;c<b%23;c++)d[a]=Math.random();d[a]=Math.floor(256*Math.random())}if(jl)for(a=1,b=0;b<jl.length;b++)d[a%16]=d[a%16]^d[(a-1)%16]/4^jl.charCodeAt(b),a++}a=[];for(b=0;b<d.length;b++)a.push("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_".charAt(d[b]&63));
return a.join("")}
;var ll,ml=y.ytLoggingDocDocumentNonce_;ml||(ml=kl(),Va("ytLoggingDocDocumentNonce_",ml));ll=ml;var nl={ae:0,Yb:1,ic:2,gh:3,ce:4,lk:5,Th:6,Vi:7,0:"DEFAULT",1:"CHAT",2:"CONVERSATIONS",3:"MINIPLAYER",4:"DIALOG",5:"VOZ",6:"MUSIC_WATCH_TABS",7:"SHARE"};function ol(a){this.h=a}
function pl(a){return new ol({trackingParams:a})}
ol.prototype.getAsJson=function(){var a={};void 0!==this.h.trackingParams?a.trackingParams=this.h.trackingParams:(a.veType=this.h.veType,void 0!==this.h.veCounter&&(a.veCounter=this.h.veCounter),void 0!==this.h.elementIndex&&(a.elementIndex=this.h.elementIndex));void 0!==this.h.dataElement&&(a.dataElement=this.h.dataElement.getAsJson());void 0!==this.h.youtubeData&&(a.youtubeData=this.h.youtubeData);return a};
ol.prototype.toString=function(){return JSON.stringify(this.getAsJson())};
ol.prototype.isClientVe=function(){return!this.h.trackingParams&&!!this.h.veType};function ql(a){a=void 0===a?0:a;return 0==a?"client-screen-nonce":"client-screen-nonce."+a}
function rl(a){a=void 0===a?0:a;return 0==a?"ROOT_VE_TYPE":"ROOT_VE_TYPE."+a}
function sl(a){return F(rl(void 0===a?0:a),void 0)}
z("yt_logging_screen.getRootVeType",sl,void 0);function tl(a){return(a=sl(void 0===a?0:a))?new ol({veType:a,youtubeData:void 0}):null}
function ul(){var a=F("csn-to-ctt-auth-info");a||(a={},N("csn-to-ctt-auth-info",a));return a}
function vl(a){a=void 0===a?0:a;var b=F(ql(a));if(!b&&!F("USE_CSN_FALLBACK",!0))return null;b||0!=a||(b="UNDEFINED_CSN");return b?b:null}
z("yt_logging_screen.getCurrentCsn",vl,void 0);function wl(a,b,c){var d=ul();(c=vl(c))&&delete d[c];b&&(d[a]=b)}
function xl(a){return ul()[a]}
z("yt_logging_screen.getCttAuthInfo",xl,void 0);function yl(a,b,c,d){c=void 0===c?0:c;if(a!==F(ql(c))||b!==F(rl(c)))wl(a,d,c),N(ql(c),a),N(rl(c),b),b=function(){setTimeout(function(){a&&sh("foregroundHeartbeatScreenAssociated",{clientDocumentNonce:ll,clientScreenNonce:a},qk)},0)},"requestAnimationFrame"in window?window.requestAnimationFrame(b):b()}
z("yt_logging_screen.setCurrentScreen",yl,void 0);function zl(a){Mh.call(this,1,arguments);this.csn=a}
v(zl,Mh);var Vh=new Nh("screen-created",zl),Al=[],Cl=Bl,Dl=0;function El(a,b,c,d){var e=d;Q("web_dedupe_ve_grafting")&&(e=d.filter(function(f){f.csn!==b?(f.csn=b,f=!0):f=!1;return f}));
c={csn:b,parentVe:c.getAsJson(),childVes:bb(e,function(f){return f.getAsJson()})};
d=u(d);for(e=d.next();!e.done;e=d.next())e=e.value.getAsJson(),(kb(e)||!e.trackingParams&&!e.veType)&&Ik(Error("Child VE logged with no data"));d={F:xl(b),O:b};"UNDEFINED_CSN"==b?Fl("visualElementAttached",c,d):a?sh("visualElementAttached",c,a,d):rk("visualElementAttached",c,d)}
function Bl(){for(var a=Math.random()+"",b=[],c=0,d=0;d<a.length;d++){var e=a.charCodeAt(d);255<e&&(b[c++]=e&255,e>>=8);b[c++]=e}return Ec(b)}
function Fl(a,b,c){Al.push({payloadName:a,payload:b,options:c});Dl||(Dl=Wh())}
function Xh(a){if(Al){for(var b=u(Al),c=b.next();!c.done;c=b.next())c=c.value,c.payload&&(c.payload.csn=a.csn,sh(c.payloadName,c.payload,null,c.options));Al.length=0}Dl=0}
;function Gl(){this.i=new Set;this.h=new Set;this.j=new Map}
Gl.prototype.clear=function(){this.i.clear();this.h.clear();this.j.clear()};
La(Gl);function Hl(a,b){for(var c=[],d=1;d<arguments.length;++d)c[d-1]=arguments[d];if(!Il(a)||c.some(function(e){return!Il(e)}))throw Error("Only objects may be merged.");
c=u(c);for(d=c.next();!d.done;d=c.next())Jl(a,d.value);return a}
function Jl(a,b){for(var c in b)if(Il(b[c])){if(c in a&&!Il(a[c]))throw Error("Cannot merge an object into a non-object.");c in a||(a[c]={});Jl(a[c],b[c])}else if(Kl(b[c])){if(c in a&&!Kl(a[c]))throw Error("Cannot merge an array into a non-array.");c in a||(a[c]=[]);Ll(a[c],b[c])}else a[c]=b[c];return a}
function Ll(a,b){b=u(b);for(var c=b.next();!c.done;c=b.next())c=c.value,Il(c)?a.push(Jl({},c)):Kl(c)?a.push(Ll([],c)):a.push(c);return a}
function Il(a){return"object"===typeof a&&!Array.isArray(a)}
function Kl(a){return"object"===typeof a&&Array.isArray(a)}
;function Ml(a,b){Mh.call(this,1,arguments)}
v(Ml,Mh);function Nl(a,b){Mh.call(this,1,arguments)}
v(Nl,Mh);var Ol=new Nh("aft-recorded",Ml),Pl=new Nh("timing-sent",Nl);var Ql=window;function Rl(){this.timing={};this.clearResourceTimings=function(){};
this.webkitClearResourceTimings=function(){};
this.mozClearResourceTimings=function(){};
this.msClearResourceTimings=function(){};
this.oClearResourceTimings=function(){}}
var W=Ql.performance||Ql.mozPerformance||Ql.msPerformance||Ql.webkitPerformance||new Rl;var Sl=!1,Tl={'script[name="scheduler/scheduler"]':"sj",'script[name="player/base"]':"pj",'link[rel="stylesheet"][name="www-player"]':"pc",'link[rel="stylesheet"][name="player/www-player"]':"pc",'script[name="desktop_polymer/desktop_polymer"]':"dpj",'link[rel="import"][name="desktop_polymer"]':"dph",'script[name="mobile-c3/mobile-c3"]':"mcj",'link[rel="stylesheet"][name="mobile-c3"]':"mcc",'script[name="player-plasma-ias-phone/base"]':"mcppj",'script[name="player-plasma-ias-tablet/base"]':"mcptj",
'link[rel="stylesheet"][name="mobile-polymer-player-ias"]':"mcpc",'link[rel="stylesheet"][name="mobile-polymer-player-svg-ias"]':"mcpsc",'script[name="mobile_blazer_core_mod"]':"mbcj",'link[rel="stylesheet"][name="mobile_blazer_css"]':"mbc",'script[name="mobile_blazer_logged_in_users_mod"]':"mbliuj",'script[name="mobile_blazer_logged_out_users_mod"]':"mblouj",'script[name="mobile_blazer_noncore_mod"]':"mbnj","#player_css":"mbpc",'script[name="mobile_blazer_desktopplayer_mod"]':"mbpj",'link[rel="stylesheet"][name="mobile_blazer_tablet_css"]':"mbtc",
'script[name="mobile_blazer_watch_mod"]':"mbwj"};C(W.clearResourceTimings||W.webkitClearResourceTimings||W.mozClearResourceTimings||W.msClearResourceTimings||W.oClearResourceTimings||Ka,W);function Ul(a){var b=Vl(a);if(b.aft)return b.aft;a=F((a||"")+"TIMING_AFT_KEYS",["ol"]);for(var c=a.length,d=0;d<c;d++){var e=b[a[d]];if(e)return e}return NaN}
function Wl(){var a;if(Q("csi_use_performance_navigation_timing")){var b,c,d,e=null===(d=null===(c=null===(b=null===(a=null===W||void 0===W?void 0:W.getEntriesByType)||void 0===a?void 0:a.call(W,"navigation"))||void 0===b?void 0:b[0])||void 0===c?void 0:c.toJSON)||void 0===d?void 0:d.call(c);e?(e.requestStart=Xl(e.requestStart),e.responseEnd=Xl(e.responseEnd),e.redirectStart=Xl(e.redirectStart),e.redirectEnd=Xl(e.redirectEnd),e.domainLookupEnd=Xl(e.domainLookupEnd),e.connectStart=Xl(e.connectStart),
e.connectEnd=Xl(e.connectEnd),e.responseStart=Xl(e.responseStart),e.secureConnectionStart=Xl(e.secureConnectionStart),e.domainLookupStart=Xl(e.domainLookupStart),e.isPerformanceNavigationTiming=!0,a=e):a=W.timing}else a=W.timing;return a}
function Yl(){return Q("csi_use_time_origin")&&W.timeOrigin?Math.floor(W.timeOrigin):W.timing.navigationStart}
function Xl(a){return Math.round(Yl()+a)}
function Zl(a){var b;(b=A("ytcsi."+(a||"")+"data_"))||(b={tick:{},info:{}},Va("ytcsi."+(a||"")+"data_",b));return b}
function $l(a){a=Zl(a);a.info||(a.info={});return a.info}
function Vl(a){a=Zl(a);a.tick||(a.tick={});return a.tick}
function am(a){var b=Zl(a).nonce;b||(b=kl(),Zl(a).nonce=b);return b}
function bm(a){var b=Vl(a||""),c=Ul(a);c&&!Sl&&(Sh(Ol,new Ml(Math.round(c-b._start),a)),Sl=!0)}
;function cm(){if(W.getEntriesByType){var a=W.getEntriesByType("paint");if(a=db(a,function(b){return"first-paint"===b.name}))return Xl(a.startTime)}a=W.timing;
return a.Xa?Math.max(0,a.Xa):0}
;function dm(){var a=A("ytcsi.debug");a||(a=[],z("ytcsi.debug",a,void 0),z("ytcsi.reference",{},void 0));return a}
function em(a){a=a||"";var b=A("ytcsi.reference");b||(dm(),b=A("ytcsi.reference"));if(b[a])return b[a];var c=dm(),d={timerName:a,info:{},tick:{},span:{}};c.push(d);return b[a]=d}
;var fm=y.ytLoggingLatencyUsageStats_||{};z("ytLoggingLatencyUsageStats_",fm,void 0);function gm(){this.h=0}
function hm(){gm.h||(gm.h=new gm);return gm.h}
gm.prototype.tick=function(a,b,c){im(this,"tick_"+a+"_"+b)||rk("latencyActionTicked",{tickName:a,clientActionNonce:b},{timestamp:c})};
gm.prototype.info=function(a,b){var c=Object.keys(a).join("");im(this,"info_"+c+"_"+b)||(a=Object.assign({},a),a.clientActionNonce=b,rk("latencyActionInfo",a))};
gm.prototype.span=function(a,b){var c=Object.keys(a).join("");im(this,"span_"+c+"_"+b)||(a.clientActionNonce=b,rk("latencyActionSpan",a))};
function im(a,b){fm[b]=fm[b]||{count:0};var c=fm[b];c.count++;c.time=R();a.h||(a.h=Nf(function(){var d=R(),e;for(e in fm)fm[e]&&6E4<d-fm[e].time&&delete fm[e];a&&(a.h=0)},5E3));
return 5<c.count?(6===c.count&&1>1E5*Math.random()&&(c=new ii("CSI data exceeded logging limit with key",b.split("_")),0<=b.indexOf("plev")||Ik(c)),!0):!1}
;var X={},jm=(X.auto_search="LATENCY_ACTION_AUTO_SEARCH",X.ad_to_ad="LATENCY_ACTION_AD_TO_AD",X.ad_to_video="LATENCY_ACTION_AD_TO_VIDEO",X.app_startup="LATENCY_ACTION_APP_STARTUP",X["artist.analytics"]="LATENCY_ACTION_CREATOR_ARTIST_ANALYTICS",X["artist.events"]="LATENCY_ACTION_CREATOR_ARTIST_CONCERTS",X["artist.presskit"]="LATENCY_ACTION_CREATOR_ARTIST_PROFILE",X.browse="LATENCY_ACTION_BROWSE",X.channels="LATENCY_ACTION_CHANNELS",X.creator_channel_dashboard="LATENCY_ACTION_CREATOR_CHANNEL_DASHBOARD",
X["channel.analytics"]="LATENCY_ACTION_CREATOR_CHANNEL_ANALYTICS",X["channel.comments"]="LATENCY_ACTION_CREATOR_CHANNEL_COMMENTS",X["channel.content"]="LATENCY_ACTION_CREATOR_POST_LIST",X["channel.copyright"]="LATENCY_ACTION_CREATOR_CHANNEL_COPYRIGHT",X["channel.editing"]="LATENCY_ACTION_CREATOR_CHANNEL_EDITING",X["channel.monetization"]="LATENCY_ACTION_CREATOR_CHANNEL_MONETIZATION",X["channel.music"]="LATENCY_ACTION_CREATOR_CHANNEL_MUSIC",X["channel.translations"]="LATENCY_ACTION_CREATOR_CHANNEL_TRANSLATIONS",
X["channel.videos"]="LATENCY_ACTION_CREATOR_CHANNEL_VIDEOS",X["channel.live_streaming"]="LATENCY_ACTION_CREATOR_LIVE_STREAMING",X.chips="LATENCY_ACTION_CHIPS",X["dialog.copyright_strikes"]="LATENCY_ACTION_CREATOR_DIALOG_COPYRIGHT_STRIKES",X["dialog.uploads"]="LATENCY_ACTION_CREATOR_DIALOG_UPLOADS",X.embed="LATENCY_ACTION_EMBED",X.entity_key_serialization_perf="LATENCY_ACTION_ENTITY_KEY_SERIALIZATION_PERF",X.entity_key_deserialization_perf="LATENCY_ACTION_ENTITY_KEY_DESERIALIZATION_PERF",X.home="LATENCY_ACTION_HOME",
X.library="LATENCY_ACTION_LIBRARY",X.live="LATENCY_ACTION_LIVE",X.live_pagination="LATENCY_ACTION_LIVE_PAGINATION",X.onboarding="LATENCY_ACTION_KIDS_ONBOARDING",X.parent_profile_settings="LATENCY_ACTION_KIDS_PARENT_PROFILE_SETTINGS",X.parent_tools_collection="LATENCY_ACTION_PARENT_TOOLS_COLLECTION",X.parent_tools_dashboard="LATENCY_ACTION_PARENT_TOOLS_DASHBOARD",X.player_att="LATENCY_ACTION_PLAYER_ATTESTATION",X["post.comments"]="LATENCY_ACTION_CREATOR_POST_COMMENTS",X["post.edit"]="LATENCY_ACTION_CREATOR_POST_EDIT",
X.prebuffer="LATENCY_ACTION_PREBUFFER",X.prefetch="LATENCY_ACTION_PREFETCH",X.profile_settings="LATENCY_ACTION_KIDS_PROFILE_SETTINGS",X.profile_switcher="LATENCY_ACTION_KIDS_PROFILE_SWITCHER",X.results="LATENCY_ACTION_RESULTS",X.search_ui="LATENCY_ACTION_SEARCH_UI",X.search_suggest="LATENCY_ACTION_SUGGEST",X.search_zero_state="LATENCY_ACTION_SEARCH_ZERO_STATE",X.secret_code="LATENCY_ACTION_KIDS_SECRET_CODE",X.seek="LATENCY_ACTION_PLAYER_SEEK",X.settings="LATENCY_ACTION_SETTINGS",X.tenx="LATENCY_ACTION_TENX",
X.video_to_ad="LATENCY_ACTION_VIDEO_TO_AD",X.watch="LATENCY_ACTION_WATCH",X.watch_it_again="LATENCY_ACTION_KIDS_WATCH_IT_AGAIN",X["watch,watch7"]="LATENCY_ACTION_WATCH",X["watch,watch7_html5"]="LATENCY_ACTION_WATCH",X["watch,watch7ad"]="LATENCY_ACTION_WATCH",X["watch,watch7ad_html5"]="LATENCY_ACTION_WATCH",X.wn_comments="LATENCY_ACTION_LOAD_COMMENTS",X.ww_rqs="LATENCY_ACTION_WHO_IS_WATCHING",X["video.analytics"]="LATENCY_ACTION_CREATOR_VIDEO_ANALYTICS",X["video.comments"]="LATENCY_ACTION_CREATOR_VIDEO_COMMENTS",
X["video.edit"]="LATENCY_ACTION_CREATOR_VIDEO_EDIT",X["video.translations"]="LATENCY_ACTION_CREATOR_VIDEO_TRANSLATIONS",X["video.video_editor"]="LATENCY_ACTION_CREATOR_VIDEO_VIDEO_EDITOR",X["video.video_editor_async"]="LATENCY_ACTION_CREATOR_VIDEO_VIDEO_EDITOR_ASYNC",X["video.monetization"]="LATENCY_ACTION_CREATOR_VIDEO_MONETIZATION",X.voice_assistant="LATENCY_ACTION_VOICE_ASSISTANT",X.cast_load_by_entity_to_watch="LATENCY_ACTION_CAST_LOAD_BY_ENTITY_TO_WATCH",X.networkless_performance="LATENCY_ACTION_NETWORKLESS_PERFORMANCE",
X),Y={},km=(Y.ad_allowed="adTypesAllowed",Y.yt_abt="adBreakType",Y.ad_cpn="adClientPlaybackNonce",Y.ad_docid="adVideoId",Y.yt_ad_an="adNetworks",Y.ad_at="adType",Y.aida="appInstallDataAgeMs",Y.browse_id="browseId",Y.p="httpProtocol",Y.t="transportProtocol",Y.cpn="clientPlaybackNonce",Y.ccs="creatorInfo.creatorCanaryState",Y.csn="clientScreenNonce",Y.docid="videoId",Y.GetHome_rid="requestIds",Y.GetSearch_rid="requestIds",Y.GetPlayer_rid="requestIds",Y.GetWatchNext_rid="requestIds",Y.GetBrowse_rid=
"requestIds",Y.GetLibrary_rid="requestIds",Y.is_continuation="isContinuation",Y.is_nav="isNavigation",Y.b_p="kabukiInfo.browseParams",Y.is_prefetch="kabukiInfo.isPrefetch",Y.is_secondary_nav="kabukiInfo.isSecondaryNav",Y.prev_browse_id="kabukiInfo.prevBrowseId",Y.query_source="kabukiInfo.querySource",Y.voz_type="kabukiInfo.vozType",Y.yt_lt="loadType",Y.mver="creatorInfo.measurementVersion",Y.yt_ad="isMonetized",Y.nr="webInfo.navigationReason",Y.nrsu="navigationRequestedSameUrl",Y.ncnp="webInfo.nonPreloadedNodeCount",
Y.pnt="performanceNavigationTiming",Y.prt="playbackRequiresTap",Y.plt="playerInfo.playbackType",Y.pis="playerInfo.playerInitializedState",Y.paused="playerInfo.isPausedOnLoad",Y.yt_pt="playerType",Y.fmt="playerInfo.itag",Y.yt_pl="watchInfo.isPlaylist",Y.yt_pre="playerInfo.preloadType",Y.yt_ad_pr="prerollAllowed",Y.pa="previousAction",Y.yt_red="isRedSubscriber",Y.rce="mwebInfo.responseContentEncoding",Y.scrh="screenHeight",Y.scrw="screenWidth",Y.st="serverTimeMs",Y.ssdm="shellStartupDurationMs",Y.br_trs=
"tvInfo.bedrockTriggerState",Y.kebqat="kabukiInfo.earlyBrowseRequestInfo.abandonmentType",Y.kebqa="kabukiInfo.earlyBrowseRequestInfo.adopted",Y.label="tvInfo.label",Y.is_mdx="tvInfo.isMdx",Y.preloaded="tvInfo.isPreloaded",Y.upg_player_vis="playerInfo.visibilityState",Y.query="unpluggedInfo.query",Y.upg_chip_ids_string="unpluggedInfo.upgChipIdsString",Y.yt_vst="videoStreamType",Y.vph="viewportHeight",Y.vpw="viewportWidth",Y.yt_vis="isVisible",Y.rcl="mwebInfo.responseContentLength",Y.GetSettings_rid=
"requestIds",Y.GetTrending_rid="requestIds",Y.GetMusicSearchSuggestions_rid="requestIds",Y.REQUEST_ID="requestIds",Y),lm="isContinuation isNavigation kabukiInfo.earlyBrowseRequestInfo.adopted kabukiInfo.isPrefetch kabukiInfo.isSecondaryNav isMonetized navigationRequestedSameUrl performanceNavigationTiming playerInfo.isPausedOnLoad prerollAllowed isRedSubscriber tvInfo.isMdx tvInfo.isPreloaded isVisible watchInfo.isPlaylist playbackRequiresTap".split(" "),mm={},nm=(mm.ccs="CANARY_STATE_",mm.mver="MEASUREMENT_VERSION_",
mm.pis="PLAYER_INITIALIZED_STATE_",mm.yt_pt="LATENCY_PLAYER_",mm.pa="LATENCY_ACTION_",mm.yt_vst="VIDEO_STREAM_TYPE_",mm),om="all_vc ap aq c cver cbrand cmodel cplatform ctheme ei l_an l_mm plid srt yt_fss yt_li vpst vpni2 vpil2 icrc icrt pa GetAccountOverview_rid GetHistory_rid cmt d_vpct d_vpnfi d_vpni nsru pc pfa pfeh pftr pnc prerender psc rc start tcrt tcrc ssr vpr vps yt_abt yt_fn yt_fs yt_pft yt_pre yt_pt yt_pvis ytu_pvis yt_ref yt_sts tds".split(" ");
function pm(a){return!!F("FORCE_CSI_ON_GEL",!1)||Q("csi_on_gel")||!!Zl(a).useGel}
function qm(a,b,c){var d=rm(c);d.gelTicks&&(d.gelTicks["tick_"+a]=!0);c||b||R();return pm(c)?(em(c||"").tick[a]=b||R(),d=am(c),"_start"===a?(a=hm(),im(a,"baseline_"+d)||rk("latencyActionBaselined",{clientActionNonce:d},{timestamp:b})):hm().tick(a,d,b),bm(c),!0):!1}
function sm(a,b,c){c=rm(c);if(c.gelInfos)c.gelInfos["info_"+a]=!0;else{var d={};c.gelInfos=(d["info_"+a]=!0,d)}if(a.match("_rid")){var e=a.split("_rid")[0];a="REQUEST_ID"}if(a in km){c=km[a];0<=$a(lm,c)&&(b=!!b);a in nm&&"string"===typeof b&&(b=nm[a]+b.toUpperCase());a=b;b=c.split(".");for(var f=d={},g=0;g<b.length-1;g++){var h=b[g];f[h]={};f=f[h]}f[b[b.length-1]]="requestIds"===c?[{id:a,endpoint:e}]:a;return Hl({},d)}0<=$a(om,a)||Ik(new ii("Unknown label logged with GEL CSI",a))}
function rm(a){a=Zl(a);if(a.gel){var b=a.gel;b.gelInfos||(b.gelInfos={});b.gelTicks||(b.gelTicks={})}else a.gel={gelTicks:{},gelInfos:{}};return a.gel}
function tm(a){a=rm(a);a.gelInfos||(a.gelInfos={});return a.gelInfos}
;function um(a,b,c){null!==b&&($l(c)[a]=b,pm(c)?(a=sm(a,b,c))&&pm(c)&&(b=em(c||""),Hl(b.info,a),Hl(tm(c),a),c=am(c),hm().info(a,c)):em(c||"").info[a]=b)}
function Z(a,b,c){var d=Vl(c);if(!b&&"_"!==a[0]){var e=a;W.mark&&(0==e.lastIndexOf("mark_",0)||(e="mark_"+e),c&&(e+=" ("+c+")"),W.mark(e))}e=b||R();d[a]=e;qm(a,b,c)||(vm(c),em(c||"").tick[a]=b||R());return d[a]}
function wm(a,b){if(pm(void 0)){var c=rm(void 0);if(c.gelSpans)c.gelSpans[a]=!0;else{var d={};c.gelSpans=(d[a]=!0,d)}a={spanName:a,spanLengthUsec:String(Math.round(1E3*b))};em("").span[String(a.spanName)]=a;b=rm(void 0);b.gelSpans||(b.gelSpans={});Hl(b.gelSpans,a);b=am(void 0);hm().span(a,b)}}
function xm(){var a=am(void 0);requestAnimationFrame(function(){setTimeout(function(){a===am(void 0)&&Z("ol",void 0,void 0)},0)})}
function vm(a){if(!A("yt.timing."+(a||"")+"pingSent_")){var b=F((a||"")+"TIMING_ACTION",void 0),c=Vl(a);if(b=!!A("ytglobal.timing"+(a||"")+"ready_")&&b)b="_start"in Vl(void 0);if(b&&Ul(a))if(bm(a),a)ym(a);else{b=!0;var d=F("TIMING_WAIT",[]);if(d.length)for(var e=0,f=d.length;e<f;++e)if(!(d[e]in c)){b=!1;break}b&&ym(a)}}}
function zm(){var a=document;if("visibilityState"in a)a=a.visibilityState;else{var b=zf+"VisibilityState";a=b in a?a[b]:void 0}switch(a){case "hidden":return 0;case "visible":return 1;case "prerender":return 2;case "unloaded":return 3;default:return-1}}
function ym(a){if(!pm(a)){var b=Vl(a),c=$l(a),d=b._start,e=F("CSI_SERVICE_NAME","youtube"),f={v:2,s:e,action:F((a||"")+"TIMING_ACTION",void 0)},g=c.srt;void 0!==b.srt&&delete c.srt;b.aft=Ul(a);var h=Vl(a),k=h.pbr,l=h.vc;h=h.pbs;k&&l&&h&&k<l&&l<h&&$l(a).yt_pvis&&"youtube"===e&&(um("yt_lt","hot_bg",a),e=b.vc,k=b.pbs,delete b.aft,c.aft=Math.round(k-e));for(var p in c)"_"!==p.charAt(0)&&(f[p]=c[p]);b.ps=R();p={};e=[];for(var n in b)"_"!==n.charAt(0)&&(k=Math.round(b[n]-d),p[n]=k,e.push(n+"."+k));f.rt=
e.join(",");b=!!c.ap;c="";for(var r in f)f.hasOwnProperty(r)&&(c+="&"+r+"="+f[r]);f="/csi_204?"+c.substring(1);window.navigator&&window.navigator.sendBeacon&&(b||Q("always_send_csi_204_with_beacon"))?Kg(f):Hg(f);z("yt.timing."+(a||"")+"pingSent_",!0,void 0);Sh(Pl,new Nl(p.aft+(Number(g)||0),a))}}
function Am(a,b){a=document.querySelector(a);if(!a)return!1;var c="",d=a.nodeName;"SCRIPT"===d?(c=a.src,c||(c=a.getAttribute("data-timing-href"))&&(c=window.location.protocol+c)):"LINK"===d&&(c=a.href);Ga()&&a.setAttribute("nonce",Ga());return c?(a=W.getEntriesByName(c))&&a[0]&&(a=a[0],c=Yl(),Z("rsf_"+b,c+Math.round(a.fetchStart)),Z("rse_"+b,c+Math.round(a.responseEnd)),void 0!==a.transferSize&&(b=$l(void 0),c=tm(void 0),"rc"in b||"rc"in c||um("rc",""),0===a.transferSize))?!0:!1:!1}
function Bm(){var a=window.location.protocol,b=W.getEntriesByType("resource");b=ab(b,function(c){return 0===c.name.indexOf(a+"//fonts.gstatic.com/s/")});
(b=cb(b,function(c,d){return d.duration>c.duration?d:c},{duration:0}))&&0<b.startTime&&0<b.responseEnd&&(Z("wffs",Xl(b.startTime)),Z("wffe",Xl(b.responseEnd)))}
var Cm=window;Cm.ytcsi&&(Cm.ytcsi.info=um,Cm.ytcsi.tick=Z);function Dm(){this.l=[];this.u=[];this.h=[];this.i=new Set;this.m=new Map}
function Em(a,b,c){c=void 0===c?0:c;b.then(function(d){var e,f;a.i.has(c)&&a.j&&a.j();var g=vl(c),h=tl(c);g&&h&&(d.csn=g,(null===(e=d.response)||void 0===e?0:e.trackingParams)&&El(a.client,g,h,[pl(d.response.trackingParams)]),(null===(f=d.playerResponse)||void 0===f?0:f.trackingParams)&&El(a.client,g,h,[pl(d.playerResponse.trackingParams)]))})}
function Fm(a,b,c,d){d=void 0===d?0:d;if(a.i.has(d))a.l.push([b,c]);else{var e=vl(d);c=c||tl(d);e&&c&&El(a.client,e,c,[b])}}
Dm.prototype.clickCommand=function(a,b,c){c=vl(void 0===c?0:c);if(!a.clickTrackingParams||!c)return!1;var d=this.client;var e="INTERACTION_LOGGING_GESTURE_TYPE_GENERIC_CLICK";a={csn:c,ve:pl(a.clickTrackingParams).getAsJson(),gestureType:e};b&&(a.clientData=b);b={F:xl(c),O:c};"UNDEFINED_CSN"==c?Fl("visualElementGestured",a,b):d?sh("visualElementGestured",a,d,b):rk("visualElementGestured",a,b);return!0};
function Gm(a,b,c){c=void 0===c?{}:c;a.i.add(c.layer||0);a.j=function(){Hm(a,b,c);var f=tl(c.layer);if(f){for(var g=u(a.l),h=g.next();!h.done;h=g.next())h=h.value,Fm(a,h[0],h[1]||f,c.layer);f=u(a.u);for(g=f.next();!g.done;g=f.next()){var k=g.value;g=void 0;g=void 0===g?0:g;h=vl(g);var l=k[0]||tl(g);h&&l&&(g=a.client,k=k[1],k={csn:h,ve:l.getAsJson(),clientData:k},l={F:xl(h),O:h},"UNDEFINED_CSN"==h?Fl("visualElementStateChanged",k,l):g?sh("visualElementStateChanged",k,g,l):rk("visualElementStateChanged",
k,l))}}};
vl(c.layer)||a.j();if(c.wa)for(var d=u(c.wa),e=d.next();!e.done;e=d.next())Em(a,e.value,c.layer);else Jk(Error("Delayed screen needs a data promise."))}
function Hm(a,b,c){c=void 0===c?{}:c;c.layer||(c.layer=0);var d=void 0!==c.Za?c.Za:c.layer;var e=vl(d);d=tl(d);var f;d&&(void 0!==c.parentCsn?f={clientScreenNonce:c.parentCsn,visualElement:d}:e&&"UNDEFINED_CSN"!==e&&(f={clientScreenNonce:e,visualElement:d}));try{var g=a.client,h=f,k=c.va,l=c.F,p=Cl(),n={csn:p,pageVe:(new ol({veType:b,youtubeData:void 0})).getAsJson()};h&&h.visualElement?n.implicitGesture={parentCsn:h.clientScreenNonce,gesturedVe:h.visualElement.getAsJson()}:h&&Ik(new ii("newScreen() parent element does not have a VE - rootVe",
b));k&&(n.cloneCsn=k);k={F:l,O:p};g?sh("screenCreated",n,g,k):rk("screenCreated",n,k);Sh(Vh,new zl(p));var r=p}catch(q){Kk(q,{Nk:b,rootVe:d,parentVisualElement:void 0,Ik:e,Mk:f,va:c.va});Jk(q);return}yl(r,b,c.layer,c.F);if((b=e&&"UNDEFINED_CSN"!==e&&d)&&!(b=Q("screen_manager_skip_hide_killswitch"))){a:{b=u(Object.values(nl));for(f=b.next();!f.done;f=b.next())if(vl(f.value)==e){b=!0;break a}b=!1}b=!b}b&&(b=a.client,f=!0,g=(f=void 0===f?!1:f)?16:8,d={csn:e,ve:d.getAsJson(),eventType:g},f={F:xl(e),O:e,
La:f},"UNDEFINED_CSN"==e?Fl("visualElementHidden",d,f):b?sh("visualElementHidden",d,b,f):rk("visualElementHidden",d,f));a.h[a.h.length-1]&&!a.h[a.h.length-1].csn&&(a.h[a.h.length-1].csn=r||"");um("csn",r);Gl.getInstance().clear();d=tl(c.layer);e&&"UNDEFINED_CSN"!==e&&d&&(Q("web_mark_root_visible")||Q("music_web_mark_root_visible"))&&(e=r,r=Q("use_default_events_client")?void 0:qk,b={csn:e,ve:d.getAsJson(),eventType:1},f={F:xl(e),O:e},"UNDEFINED_CSN"==e?Fl("visualElementShown",b,f):r?sh("visualElementShown",
b,r,f):rk("visualElementShown",b,f));a.i.delete(c.layer||0);a.j=void 0;e=u(a.m);for(r=e.next();!r.done;r=e.next())r=u(r.value),b=r.next().value,r.next().value.has(c.layer)&&d&&Fm(a,b,d,c.layer)}
;function Im(a){a&&(a.dataset?a.dataset[Jm("loaded")]="true":a.setAttribute("data-loaded","true"))}
function Km(a,b){return a?a.dataset?a.dataset[Jm(b)]:a.getAttribute("data-"+b):null}
var Lm={};function Jm(a){return Lm[a]||(Lm[a]=String(a).replace(/\-([a-z])/g,function(b,c){return c.toUpperCase()}))}
;var Mm=/\.vflset|-vfl[a-zA-Z0-9_+=-]+/,Nm=/-[a-zA-Z]{2,3}_[a-zA-Z]{2,3}(?=(\/|$))/;function Om(a,b,c){c=void 0===c?null:c;if(window.spf&&spf.script){c="";if(a){var d=a.indexOf("jsbin/"),e=a.lastIndexOf(".js"),f=d+6;-1<d&&-1<e&&e>f&&(c=a.substring(f,e),c=c.replace(Mm,""),c=c.replace(Nm,""),c=c.replace("debug-",""),c=c.replace("tracing-",""))}spf.script.load(a,c,b)}else Pm(a,b,c)}
function Pm(a,b,c){c=void 0===c?null:c;var d=Qm(a),e=document.getElementById(d),f=e&&Km(e,"loaded"),g=e&&!f;f?b&&b():(b&&(f=Pg(d,b),b=""+Pa(b),Rm[b]=f),g||(e=Sm(a,d,function(){Km(e,"loaded")||(Im(e),Sg(d),Jf(Ua(Tg,d),0))},c)))}
function Sm(a,b,c,d){d=void 0===d?null:d;var e=Mc(document,"SCRIPT");e.id=b;e.onload=function(){c&&setTimeout(c,0)};
e.onreadystatechange=function(){switch(e.readyState){case "loaded":case "complete":e.onload()}};
d&&e.setAttribute("nonce",d);Zb(e,Uc(a));a=document.getElementsByTagName("head")[0]||document.body;a.insertBefore(e,a.firstChild);return e}
function Tm(a){a=Qm(a);var b=document.getElementById(a);b&&(Tg(a),b.parentNode.removeChild(b))}
function Um(a,b){a&&b&&(a=""+Pa(b),(a=Rm[a])&&Rg(a))}
function Qm(a){var b=document.createElement("a");Vb(b,a);a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"js-"+bc(a)}
var Rm={};var Vm=[],Wm=!1;function Xm(){if((!Q("condition_ad_status_fetch_on_consent_cookie_html5_clients")||ed.get("CONSENT","").startsWith("YES+"))&&"1"!=nb()){var a=function(){Wm=!0;"google_ad_status"in window?N("DCLKSTAT",1):N("DCLKSTAT",2)};
try{Om("//static.doubleclick.net/instream/ad_status.js",a)}catch(b){}Vm.push(Pf(function(){if(!(Wm||"google_ad_status"in window)){try{Um("//static.doubleclick.net/instream/ad_status.js",a)}catch(b){}Wm=!0;N("DCLKSTAT",3)}},5E3))}}
function Ym(){var a=Number(F("DCLKSTAT",0));return isNaN(a)?0:a}
;function Zm(){this.i=!1;this.h=null}
Zm.prototype.initialize=function(a,b,c,d,e,f){var g=this;f=void 0===f?!1:f;b?(this.i=!0,Om(b,function(){g.i=!1;var h=0<=b.indexOf("/th/");(h?window.trayride:window.botguard)?$m(g,c,!!f,h,d):(Tm(b),Ik(new ii("Unable to load Botguard","from "+b)))},e)):a&&(e=Mc(document,"SCRIPT"),e.textContent=a,e.nonce=Ga(),document.head.appendChild(e),document.head.removeChild(e),((a=a.includes("trayride"))?window.trayride:window.botguard)?$m(this,c,!!f,a,d):Ik(Error("Unable to load Botguard from JS")))};
function $m(a,b,c,d,e){var f,g;if(d=d?null===(f=window.trayride)||void 0===f?void 0:f.ad:null===(g=window.botguard)||void 0===g?void 0:g.bg)if(c)try{an(a,new d(b,e?function(){return e(b)}:Ka))}catch(h){h instanceof Error&&Ik(h)}else{try{an(a,new d(b))}catch(h){h instanceof Error&&Ik(h)}e&&e(b)}else Ik(Error("Failed to finish initializing VM"))}
Zm.prototype.invoke=function(a){a=void 0===a?{}:a;return this.h?this.h.hasOwnProperty("hot")?this.h.hot(void 0,void 0,a):this.h.invoke(void 0,void 0,a):null};
Zm.prototype.dispose=function(){this.h=null};
function an(a,b){a.h=b}
;var bn=new Zm;function cn(){return!!bn.h}
function dn(a){a=void 0===a?{}:a;return bn.invoke(a)}
;function en(a){L.call(this);this.i={};this.started=!1;this.connection=a;this.connection.subscribe("command",this.Da,this)}
v(en,L);m=en.prototype;m.start=function(){this.started||this.h||(this.started=!0,this.connection.S("RECEIVING"))};
m.S=function(a,b){this.started&&!this.h&&this.connection.S(a,b)};
m.Da=function(a,b,c){if(this.started&&!this.h){var d=b||{};switch(a){case "addEventListener":"string"===typeof d.event&&this.addListener(d.event);break;case "removeEventListener":"string"===typeof d.event&&this.removeListener(d.event);break;default:this.api.isReady()&&this.api.isExternalMethodAvailable(a,c||null)&&(b=fn(a,b||{}),c=this.api.handleExternalCall(a,b,c||null),(c=gn(a,c))&&this.S(a,c))}}};
m.addListener=function(a){if(!(a in this.i)){var b=this.eb.bind(this,a);this.i[a]=b;this.addEventListener(a,b)}};
m.eb=function(a,b){this.started&&!this.h&&this.connection.S(a,this.ka(a,b))};
m.ka=function(a,b){if(null!=b)return{value:b}};
m.removeListener=function(a){a in this.i&&(this.removeEventListener(a,this.i[a]),delete this.i[a])};
m.D=function(){var a=this.connection;a.h||We(a.i,"command",this.Da,this);this.connection=null;for(var b in this.i)this.i.hasOwnProperty(b)&&this.removeListener(b);L.prototype.D.call(this)};function hn(a,b){en.call(this,b);this.api=a;this.start()}
v(hn,en);hn.prototype.addEventListener=function(a,b){this.api.addEventListener(a,b)};
hn.prototype.removeEventListener=function(a,b){this.api.removeEventListener(a,b)};
function fn(a,b){switch(a){case "loadVideoById":return a=Sk(b),[a];case "cueVideoById":return a=Sk(b),[a];case "loadVideoByPlayerVars":return[b];case "cueVideoByPlayerVars":return[b];case "loadPlaylist":return a=Tk(b),[a];case "cuePlaylist":return a=Tk(b),[a];case "seekTo":return[b.seconds,b.allowSeekAhead];case "playVideoAt":return[b.index];case "setVolume":return[b.volume];case "setPlaybackQuality":return[b.suggestedQuality];case "setPlaybackRate":return[b.suggestedRate];case "setLoop":return[b.loopPlaylists];
case "setShuffle":return[b.shufflePlaylist];case "getOptions":return[b.module];case "getOption":return[b.module,b.option];case "setOption":return[b.module,b.option,b.value];case "handleGlobalKeyDown":return[b.keyCode,b.shiftKey,b.ctrlKey,b.altKey,b.metaKey,b.key,b.code]}return[]}
function gn(a,b){switch(a){case "isMuted":return{muted:b};case "getVolume":return{volume:b};case "getPlaybackRate":return{playbackRate:b};case "getAvailablePlaybackRates":return{availablePlaybackRates:b};case "getVideoLoadedFraction":return{videoLoadedFraction:b};case "getPlayerState":return{playerState:b};case "getCurrentTime":return{currentTime:b};case "getPlaybackQuality":return{playbackQuality:b};case "getAvailableQualityLevels":return{availableQualityLevels:b};case "getDuration":return{duration:b};
case "getVideoUrl":return{videoUrl:b};case "getVideoEmbedCode":return{videoEmbedCode:b};case "getPlaylist":return{playlist:b};case "getPlaylistIndex":return{playlistIndex:b};case "getOptions":return{options:b};case "getOption":return{option:b}}}
hn.prototype.ka=function(a,b){switch(a){case "onReady":return;case "onStateChange":return{playerState:b};case "onPlaybackQualityChange":return{playbackQuality:b};case "onPlaybackRateChange":return{playbackRate:b};case "onError":return{errorCode:b}}return en.prototype.ka.call(this,a,b)};
hn.prototype.D=function(){en.prototype.D.call(this);delete this.api};function jn(a){a=void 0===a?!1:a;L.call(this);this.i=new M(a);Hd(this,Ua(Fd,this.i))}
D(jn,L);jn.prototype.subscribe=function(a,b,c){return this.h?0:this.i.subscribe(a,b,c)};
jn.prototype.l=function(a,b){this.h||this.i.R.apply(this.i,arguments)};function kn(a,b,c){jn.call(this);this.j=a;this.destination=b;this.id=c}
v(kn,jn);kn.prototype.S=function(a,b){this.h||this.j.S(this.destination,this.id,a,b)};
kn.prototype.D=function(){this.destination=this.j=null;jn.prototype.D.call(this)};function ln(a,b,c){L.call(this);this.destination=a;this.origin=c;this.i=Gf(window,"message",this.j.bind(this));this.connection=new kn(this,a,b);Hd(this,Ua(Fd,this.connection))}
v(ln,L);ln.prototype.S=function(a,b,c,d){this.h||a!==this.destination||(a={id:b,command:c},d&&(a.data=d),this.destination.postMessage(xe(a),this.origin))};
ln.prototype.j=function(a){var b;if(b=!this.h)if(b=a.origin===this.origin)a:{b=this.destination;do{b:{var c=a.source;do{if(c===b){c=!0;break b}if(c===c.parent)break;c=c.parent}while(null!=c);c=!1}if(c){b=!0;break a}b=b.opener}while(null!=b);b=!1}if(b&&(b=a.data,"string"===typeof b)){try{b=JSON.parse(b)}catch(d){return}b.command&&(c=this.connection,c.h||c.l("command",b.command,b.data,a.origin))}};
ln.prototype.D=function(){Hf(this.i);this.destination=null;L.prototype.D.call(this)};function mn(){L.call(this);this.i=[]}
v(mn,L);mn.prototype.D=function(){for(;this.i.length;){var a=this.i.pop();a.target.removeEventListener(a.name,a.Ia)}L.prototype.D.call(this)};function nn(a){a=a||{};var b={},c={};this.url=a.url||"";this.args=a.args||pb(b);this.assets=a.assets||{};this.attrs=a.attrs||pb(c);this.fallback=a.fallback||null;this.fallbackMessage=a.fallbackMessage||null;this.html5=!!a.html5;this.disable=a.disable||{};this.loaded=!!a.loaded;this.messages=a.messages||{}}
nn.prototype.clone=function(){var a=new nn,b;for(b in this)if(this.hasOwnProperty(b)){var c=this[b];"object"==Ma(c)?a[b]=pb(c):a[b]=c}return a};var on=/cssbin\/(?:debug-)?([a-zA-Z0-9_-]+?)(?:-2x|-web|-rtl|-vfl|.css)/;function pn(a){a=a||"";if(window.spf){var b=a.match(on);spf.style.load(a,b?b[1]:"",void 0)}else qn(a)}
function qn(a){var b=rn(a),c=document.getElementById(b),d=c&&Km(c,"loaded");d||c&&!d||(c=sn(a,b,function(){Km(c,"loaded")||(Im(c),Sg(b),Jf(Ua(Tg,b),0))}))}
function sn(a,b,c){var d=document.createElement("link");d.id=b;d.onload=function(){c&&setTimeout(c,0)};
a=Uc(a);Wb(d,a);(document.getElementsByTagName("head")[0]||document.body).appendChild(d);return d}
function rn(a){var b=Mc(document,"A");Vb(b,new Hb(a,Ib));a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"css-"+bc(a)}
;function tn(a,b,c,d){L.call(this);var e=this;this.G=b;this.webPlayerContextConfig=d;this.ha=!1;this.api={};this.V=this.m=null;this.J=new M;this.i={};this.M=this.aa=this.elementId=this.ia=this.config=null;this.K=!1;this.l=this.A=null;this.ba={};this.Ga=["onReady"];this.lastError=null;this.sa=NaN;this.C={};this.Ha=new mn(this);this.U=0;this.j=this.o=a;Hd(this,Ua(Fd,this.J));un(this);vn(this);Hd(this,Ua(Fd,this.Ha));c?this.U=Jf(function(){e.loadNewVideoConfig(c)},0):d&&(wn(this),xn(this))}
v(tn,L);m=tn.prototype;m.getId=function(){return this.G};
m.loadNewVideoConfig=function(a){if(!this.h){this.U&&(Kf(this.U),this.U=0);var b=a||{};b instanceof nn||(b=new nn(b));this.config=b;this.setConfig(a);xn(this);this.isReady()&&yn(this)}};
function wn(a){var b,c;a.webPlayerContextConfig?c=a.webPlayerContextConfig.rootElementId:c=a.config.attrs.id;a.elementId=c||a.elementId;"video-player"===a.elementId&&(a.elementId=a.G,a.webPlayerContextConfig?a.webPlayerContextConfig.rootElementId=a.G:a.config.attrs.id=a.G);(null===(b=a.j)||void 0===b?void 0:b.id)===a.elementId&&(a.elementId+="-player",a.webPlayerContextConfig?a.webPlayerContextConfig.rootElementId=a.elementId:a.config.attrs.id=a.elementId)}
m.setConfig=function(a){var b;this.ia=a;this.config=zn(a);wn(this);this.aa||(this.aa=An(this,(null===(b=this.config.args)||void 0===b?void 0:b.jsapicallback)||"onYouTubePlayerReady"));this.config.args?this.config.args.jsapicallback=null:this.config.args={jsapicallback:null};var c;if(null===(c=this.config)||void 0===c?0:c.attrs)a=this.config.attrs,(c=a.width)&&this.j&&(this.j.style.width=Wc(Number(c)||c)),(a=a.height)&&this.j&&(this.j.style.height=Wc(Number(a)||a))};
function yn(a){var b;a.config&&!0!==a.config.loaded&&(a.config.loaded=!0,!a.config.args||"0"!==a.config.args.autoplay&&0!==a.config.args.autoplay&&!1!==a.config.args.autoplay?a.api.loadVideoByPlayerVars(null!==(b=a.config.args)&&void 0!==b?b:null):a.api.cueVideoByPlayerVars(a.config.args))}
function Bn(a){var b=!0,c=Cn(a);c&&a.config&&(a=Dn(a),b=Km(c,"version")===a);return b&&!!A("yt.player.Application.create")}
function xn(a){if(!a.h&&!a.K){var b=Bn(a);if(b&&"html5"===(Cn(a)?"html5":null))a.M="html5",a.isReady()||En(a);else if(Fn(a),a.M="html5",b&&a.l&&a.o)a.o.appendChild(a.l),En(a);else{a.config&&(a.config.loaded=!0);var c=!1;a.A=function(){c=!0;var d=Gn(a,"player_bootstrap_method")?A("yt.player.Application.createAlternate")||A("yt.player.Application.create"):A("yt.player.Application.create");var e=a.config?zn(a.config):void 0;d&&d(a.o,e,a.webPlayerContextConfig);En(a)};
a.K=!0;b?a.A():(Om(Dn(a),a.A),(b=Hn(a))&&pn(b),In(a)&&!c&&z("yt.player.Application.create",null,void 0))}}}
function Cn(a){var b=Ic(a.elementId);!b&&a.j&&a.j.querySelector&&(b=a.j.querySelector("#"+a.elementId));return b}
function En(a){var b;if(!a.h){var c=Cn(a),d=!1;c&&c.getApiInterface&&c.getApiInterface()&&(d=!0);d?(a.K=!1,!Gn(a,"html5_remove_not_servable_check_killswitch")&&(null===c||void 0===c?0:c.isNotServable)&&a.config&&(null===c||void 0===c?0:c.isNotServable(null===(b=a.config.args)||void 0===b?void 0:b.video_id))||Jn(a)):a.sa=Jf(function(){En(a)},50)}}
function Jn(a){un(a);a.ha=!0;var b=Cn(a);if(b){a.m=Kn(a,b,"addEventListener");a.V=Kn(a,b,"removeEventListener");var c=b.getApiInterface();c=c.concat(b.getInternalApiInterface());for(var d=a.api,e=0;e<c.length;e++){var f=c[e];d[f]||(d[f]=Kn(a,b,f))}}for(var g in a.i)a.i.hasOwnProperty(g)&&a.m&&a.m(g,a.i[g]);yn(a);a.aa&&a.aa(a.api);a.J.R("onReady",a.api)}
function Kn(a,b,c){var d=b[c];return function(e){for(var f=[],g=0;g<arguments.length;++g)f[g-0]=arguments[g];try{return a.lastError=null,d.apply(b,f)}catch(h){"sendAbandonmentPing"!==c&&(h.params=c,a.lastError=h,Ik(h))}}}
function un(a){a.ha=!1;if(a.V)for(var b in a.i)a.i.hasOwnProperty(b)&&a.V(b,a.i[b]);for(var c in a.C)a.C.hasOwnProperty(c)&&Kf(Number(c));a.C={};a.m=null;a.V=null;b=a.api;for(var d in b)b.hasOwnProperty(d)&&(b[d]=null);b.addEventListener=function(e,f){a.addEventListener(e,f)};
b.removeEventListener=function(e,f){a.removeEventListener(e,f)};
b.destroy=function(){a.dispose()};
b.getLastError=function(){return a.getLastError()};
b.getPlayerType=function(){return a.getPlayerType()};
b.getCurrentVideoConfig=function(){return a.ia};
b.loadNewVideoConfig=function(e){a.loadNewVideoConfig(e)};
b.isReady=function(){return a.isReady()}}
m.isReady=function(){return this.ha};
function vn(a){a.addEventListener("WATCH_LATER_VIDEO_ADDED",function(b){Sg("WATCH_LATER_VIDEO_ADDED",b)});
a.addEventListener("WATCH_LATER_VIDEO_REMOVED",function(b){Sg("WATCH_LATER_VIDEO_REMOVED",b)});
a.addEventListener("onAdAnnounce",function(b){Sg("a11y-announce",b)})}
m.addEventListener=function(a,b){var c=this,d=An(this,b);d&&(0<=$a(this.Ga,a)||this.i[a]||(b=Ln(this,a),this.m&&this.m(a,b)),this.J.subscribe(a,d),"onReady"===a&&this.isReady()&&Jf(function(){d(c.api)},0))};
m.removeEventListener=function(a,b){this.h||(b=An(this,b))&&We(this.J,a,b)};
function An(a,b){var c=b;if("string"===typeof b){if(a.ba[b])return a.ba[b];c=function(d){for(var e=[],f=0;f<arguments.length;++f)e[f-0]=arguments[f];(f=A(b))&&f.apply(y,e)};
a.ba[b]=c}return c?c:null}
function Ln(a,b){var c="ytPlayer"+b+a.G;a.i[b]=c;y[c]=function(d){var e=Jf(function(){if(!a.h){a.J.R(b,d);var f=a.C,g=String(e);g in f&&delete f[g]}},0);
lb(a.C,String(e))};
return c}
m.getPlayerType=function(){return this.M||(Cn(this)?"html5":null)};
m.getLastError=function(){return this.lastError};
function Fn(a){a.cancel();un(a);a.M=null;a.config&&(a.config.loaded=!1);var b=Cn(a);b&&(Bn(a)||!In(a)?a.l=b:(b&&b.destroy&&b.destroy(),a.l=null));if(a.o)for(a=a.o;b=a.firstChild;)a.removeChild(b)}
m.cancel=function(){this.A&&Um(Dn(this),this.A);Kf(this.sa);this.K=!1};
m.D=function(){Fn(this);if(this.l&&this.config&&this.l.destroy)try{this.l.destroy()}catch(b){Jk(b)}this.ba=null;for(var a in this.i)this.i.hasOwnProperty(a)&&(y[this.i[a]]=null);this.ia=this.config=this.api=null;delete this.o;delete this.j;L.prototype.D.call(this)};
function In(a){var b,c;a=null===(c=null===(b=a.config)||void 0===b?void 0:b.args)||void 0===c?void 0:c.fflags;return!!a&&-1!==a.indexOf("player_destroy_old_version=true")}
function Dn(a){return a.webPlayerContextConfig?a.webPlayerContextConfig.jsUrl:(a=a.config.assets)?a.js:""}
function Hn(a){return a.webPlayerContextConfig?a.webPlayerContextConfig.cssUrl:(a=a.config.assets)?a.css:""}
function Gn(a,b){var c;if(a.webPlayerContextConfig)var d=a.webPlayerContextConfig.serializedExperimentFlags;else if(null===(c=a.config)||void 0===c?0:c.args)d=a.config.args.fflags;return"true"===dg(d||"","&")[b]}
function zn(a){for(var b={},c=u(Object.keys(a)),d=c.next();!d.done;d=c.next()){d=d.value;var e=a[d];b[d]="object"===typeof e?pb(e):e}return b}
;var Mn={},Nn="player_uid_"+(1E9*Math.random()>>>0);function On(a,b,c){var d="player";c=void 0===c?!0:c;d="string"===typeof d?Ic(d):d;var e=Nn+"_"+Pa(d),f=Mn[e];if(f&&c)return Pn(a,b)?f.api.loadVideoByPlayerVars(a.args||null):f.loadNewVideoConfig(a),f.api;f=new tn(d,e,a,b);Mn[e]=f;Sg("player-added",f.api);Hd(f,function(){delete Mn[f.getId()]});
return f.api}
function Pn(a,b){return b&&b.serializedExperimentFlags?b.serializedExperimentFlags.includes("web_player_remove_playerproxy=true"):a&&a.args&&a.args.fflags?a.args.fflags.includes("web_player_remove_playerproxy=true"):!1}
;var Qn=null,Rn=null,Sn=null;function Tn(){var a=Qn.getVideoData(1);a=a.title?a.title+" - YouTube":"YouTube";document.title!==a&&(document.title=a)}
;function Un(a,b,c){a="ST-"+bc(a).toString(36);b=b?gc(b):"";c=c||5;var d=ed.get("CONSENT",void 0);d&&!d.startsWith("YES+")||uh(a,b,c)}
;function Vn(a,b,c){b=void 0===b?{}:b;c=void 0===c?!1:c;var d=F("EVENT_ID");d&&(b.ei||(b.ei=d));if(b){d=a;var e=void 0===e?!0:e;var f=F("VALID_SESSION_TEMPDATA_DOMAINS",[]),g=ec(window.location.href);g&&f.push(g);g=ec(d);if(0<=$a(f,g)||!g&&0==d.lastIndexOf("/",0))if(Q("autoescape_tempdata_url")&&(f=document.createElement("a"),Vb(f,d),d=f.href),d){g=d.match(cc);d=g[5];f=g[6];g=g[7];var h="";d&&(h+=d);f&&(h+="?"+f);g&&(h+="#"+g);d=h;f=d.indexOf("#");if(d=0>f?d:d.substr(0,f))if(e&&!b.csn&&(b.itct||b.ved)&&
(b=Object.assign({csn:vl()},b)),k){var k=parseInt(k,10);isFinite(k)&&0<k&&Un(d,b,k)}else Un(d,b)}}if(c)return!1;if((window.ytspf||{}).enabled)spf.navigate(a);else{var l=void 0===l?{}:l;var p=void 0===p?"":p;var n=void 0===n?window:n;c=n.location;a=hc(a,l)+p;a=a instanceof Hb?a:Nb(a);c.href=Jb(a)}return!0}
;z("yt.setConfig",N,void 0);z("yt.config.set",N,void 0);z("yt.setMsg",vf,void 0);z("yt.msgs.set",vf,void 0);z("yt.logging.errors.log",Jk,void 0);
z("writeEmbed",function(){var a=F("PLAYER_CONFIG",void 0);if(!a){var b=F("PLAYER_VARS",void 0);b&&(a={args:b})}il(!0);"gvn"===a.args.ps&&(document.body.style.backgroundColor="transparent");a.attrs||(a.attrs={width:"100%",height:"100%",id:"video-player"});var c=document.referrer;b=F("POST_MESSAGE_ORIGIN");window!==window.top&&c&&c!==document.URL&&(a.args.loaderUrl=c);F("EXPERIMENT_FLAGS").embeds_js_api_set_1p_cookie&&(c=ig(),c.embedsTokenValue&&(a.args.embedsTokenValue=c.embedsTokenValue));F("EXPERIMENT_FLAGS").embeds_web_force_csi_on_gel&&
N("FORCE_CSI_ON_GEL",!0);c=["ol"];em("").info.actionType="embed";c&&N("TIMING_AFT_KEYS",c);N("TIMING_ACTION","embed");c=F("TIMING_INFO",{});for(var d in c)c.hasOwnProperty(d)&&um(d,c[d]);um("is_nav",1);(d=vl())&&um("csn",d);(d=F("PREVIOUS_ACTION",void 0))&&!pm()&&um("pa",d);d=$l();c=F("CLIENT_PROTOCOL");var e=F("CLIENT_TRANSPORT");c&&um("p",c);e&&um("t",e);um("yt_vis",zm());um("yt_lt","cold");c=Wl();if(e=Yl())Z("srt",c.responseStart),1!==d.prerender&&(um("yt_sts","n",void 0),Z("_start",e,void 0));
d=cm();0<d&&Z("fpt",d);if(!Q("log_deltas_killswitch")){var f,g,h,k;W&&W.timing&&(W.timeOrigin&&W.timing.navigationStart&&wm("startTimeDelta",Math.floor(W.timeOrigin)-W.timing.navigationStart),(d=null===(k=null===(h=null===(g=null===(f=W.getEntriesByType)||void 0===f?void 0:f.call(W,"navigation"))||void 0===g?void 0:g[0])||void 0===h?void 0:h.toJSON)||void 0===k?void 0:k.call(h))&&d.responseEnd&&W.timing.responseEnd&&wm("responseEndDelta",Xl(d.responseEnd)-W.timing.responseEnd))}f=Wl();f.isPerformanceNavigationTiming&&
um("pnt",1,void 0);Z("nreqs",f.requestStart,void 0);Z("nress",f.responseStart,void 0);Z("nrese",f.responseEnd,void 0);0<f.redirectEnd-f.redirectStart&&(Z("nrs",f.redirectStart,void 0),Z("nre",f.redirectEnd,void 0));0<f.domainLookupEnd-f.domainLookupStart&&(Z("ndnss",f.domainLookupStart,void 0),Z("ndnse",f.domainLookupEnd,void 0));0<f.connectEnd-f.connectStart&&(Z("ntcps",f.connectStart,void 0),Z("ntcpe",f.connectEnd,void 0));f.secureConnectionStart>=Yl()&&0<f.connectEnd-f.secureConnectionStart&&(Z("nstcps",
f.secureConnectionStart,void 0),Z("ntcpe",f.connectEnd,void 0));W&&W.getEntriesByType&&Bm();f=[];if(document.querySelector&&W&&W.getEntriesByName)for(var l in Tl)Tl.hasOwnProperty(l)&&(g=Tl[l],Am(l,g)&&f.push(g));f.length&&um("rc",f.join(","));if(pm(void 0)){l={actionType:jm[F("TIMING_ACTION",void 0)]||"LATENCY_ACTION_UNKNOWN",previousAction:jm[F("PREVIOUS_ACTION",void 0)]||"LATENCY_ACTION_UNKNOWN"};if(f=vl())l.clientScreenNonce=f;f=am(void 0);hm().info(l,f)}l=$l();g=Vl();if("cold"===l.yt_lt&&(f=
rm(),h=f.gelTicks?f.gelTicks:f.gelTicks={},f=f.gelInfos?f.gelInfos:f.gelInfos={},pm())){for(var p in g)"tick_"+p in h||qm(p,g[p]);p=tm();g=am();h={};for(var n in l)"info_"+n in f||!(k=sm(n,l[n]))||(Hl(p,k),Hl(h,k));hm().info(h,g)}z("ytglobal.timingready_",!0,void 0);vm();(n=F("WEB_PLAYER_CONTEXT_CONFIGS",void 0))&&"WEB_PLAYER_CONTEXT_CONFIG_ID_EMBEDDED_PLAYER"in n?(n=n.WEB_PLAYER_CONTEXT_CONFIG_ID_EMBEDDED_PLAYER,n.serializedForcedExperimentIds||(p=ig(),p.forced_experiments&&(n.serializedForcedExperimentIds=
p.forced_experiments)),Qn=On(a,n,!1)):Qn=On(a);Qn.addEventListener("onVideoDataChange",Tn);a=F("POST_MESSAGE_ID","player");F("ENABLE_JS_API")?Sn=new Uk(Qn):F("ENABLE_POST_API")&&"string"===typeof a&&"string"===typeof b&&(Rn=new ln(window.parent,a,b),Sn=new hn(Qn,Rn.connection));Xm();F("EXPERIMENT_FLAGS").networkless_logging_web_embedded&&fk()},void 0);
var Wn=rf(function(){xm();var a=wh.getInstance(),b=!!((zh("f"+(Math.floor(119/31)+1))||0)&67108864),c=1<window.devicePixelRatio;if(document.body&&Kd(document.body,"exp-invert-logo"))if(c&&!Kd(document.body,"inverted-hdpi")){var d=document.body;if(d.classList)d.classList.add("inverted-hdpi");else if(!Kd(d,"inverted-hdpi")){var e=Id(d);Jd(d,e+(0<e.length?" inverted-hdpi":"inverted-hdpi"))}}else!c&&Kd(document.body,"inverted-hdpi")&&Ld();if(b!=c){b="f"+(Math.floor(119/31)+1);d=zh(b)||0;d=c?d|67108864:
d&-67108865;0==d?delete vh[b]:(c=d.toString(16),vh[b]=c.toString());c=!0;Q("web_secure_pref_cookie_killswitch")&&(c=!1);b=a.h;d=[];for(var f in vh)d.push(f+"="+encodeURIComponent(String(vh[f])));uh(b,d.join("&"),63072E3,a.i,c)}Dm.h||(Dm.h=new Dm);a=Dm.h;f=16623;var g=void 0===g?{}:g;Object.values(Lk).includes(f)||(Ik(new ii("createClientScreen() called with a non-page VE",f)),f=83769);g.isHistoryNavigation||a.h.push({rootVe:f,key:g.key||""});a.l=[];a.u=[];g.wa?Gm(a,f,g):Hm(a,f,g)}),Xn=rf(function(){Qn&&
Qn.sendAbandonmentPing&&Qn.sendAbandonmentPing();
F("PL_ATT")&&bn.dispose();for(var a=0,b=Vm.length;a<b;a++)Tf(Vm[a]);Vm.length=0;Tm("//static.doubleclick.net/instream/ad_status.js");Wm=!1;N("DCLKSTAT",0);Gd(Sn,Rn);Qn&&(Qn.removeEventListener("onVideoDataChange",Tn),Qn.destroy())});
window.addEventListener?(window.addEventListener("load",Wn),window.addEventListener("unload",Xn)):window.attachEvent&&(window.attachEvent("onload",Wn),window.attachEvent("onunload",Xn));Va("yt.abuse.player.botguardInitialized",A("yt.abuse.player.botguardInitialized")||cn);Va("yt.abuse.player.invokeBotguard",A("yt.abuse.player.invokeBotguard")||dn);Va("yt.abuse.dclkstatus.checkDclkStatus",A("yt.abuse.dclkstatus.checkDclkStatus")||Ym);
Va("yt.player.exports.navigate",A("yt.player.exports.navigate")||Vn);Va("yt.util.activity.init",A("yt.util.activity.init")||Vf);Va("yt.util.activity.getTimeSinceActive",A("yt.util.activity.getTimeSinceActive")||Yf);Va("yt.util.activity.setTimestamp",A("yt.util.activity.setTimestamp")||Wf);}).call(this);
