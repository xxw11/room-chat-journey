(function(t){function e(e){for(var s,i,o=e[0],c=e[1],l=e[2],p=0,f=[];p<o.length;p++)i=o[p],Object.prototype.hasOwnProperty.call(n,i)&&n[i]&&f.push(n[i][0]),n[i]=0;for(s in c)Object.prototype.hasOwnProperty.call(c,s)&&(t[s]=c[s]);u&&u(e);while(f.length)f.shift()();return r.push.apply(r,l||[]),a()}function a(){for(var t,e=0;e<r.length;e++){for(var a=r[e],s=!0,o=1;o<a.length;o++){var c=a[o];0!==n[c]&&(s=!1)}s&&(r.splice(e--,1),t=i(i.s=a[0]))}return t}var s={},n={app:0},r=[];function i(e){if(s[e])return s[e].exports;var a=s[e]={i:e,l:!1,exports:{}};return t[e].call(a.exports,a,a.exports,i),a.l=!0,a.exports}i.m=t,i.c=s,i.d=function(t,e,a){i.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:a})},i.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},i.t=function(t,e){if(1&e&&(t=i(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var a=Object.create(null);if(i.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var s in t)i.d(a,s,function(e){return t[e]}.bind(null,s));return a},i.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return i.d(e,"a",e),e},i.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},i.p="/";var o=window["webpackJsonp"]=window["webpackJsonp"]||[],c=o.push.bind(o);o.push=e,o=o.slice();for(var l=0;l<o.length;l++)e(o[l]);var u=c;r.push([0,"chunk-vendors"]),a()})({0:function(t,e,a){t.exports=a("56d7")},"034f":function(t,e,a){"use strict";var s=a("85ec"),n=a.n(s);n.a},1:function(t,e){},"1be2":function(t,e,a){"use strict";var s=a("faf5"),n=a.n(s);n.a},"1e3e":function(t,e,a){},3236:function(t,e,a){"use strict";var s=a("c52b"),n=a.n(s);n.a},"3a11":function(t,e,a){"use strict";var s=a("3a9c"),n=a.n(s);n.a},"3a9c":function(t,e,a){},"4f49":function(t,e,a){"use strict";var s=a("6a82"),n=a.n(s);n.a},"56d7":function(t,e,a){"use strict";a.r(e);a("e260"),a("e6cf"),a("cca6"),a("a79d");var s=a("2b0e"),n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{attrs:{id:"app"}},[a("router-view")],1)},r=[],i=(a("034f"),a("2877")),o={},c=Object(i["a"])(o,n,r,!1,null,null,null),l=c.exports,u=a("8c4f"),p=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"main"},[a("div",{staticClass:"left"},[a("Left")],1),a("div",{staticClass:"right"},[a("Right")],1)])},f=[],d=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticStyle:{"text-align":"center","border-right":"2px solid #f5f6fa"}},[a("img",{staticStyle:{"margin-top":"5%"},attrs:{src:"img/logo.png"}}),a("div",{staticClass:"tubiao"},[a("span",{staticClass:"glyphicon glyphicon-edit",on:{click:t.menu1}}),a("br"),a("br"),a("br"),a("span",{staticClass:"glyphicon glyphicon-comment",on:{click:t.menu2}}),a("br"),a("br"),a("br"),a("span",{staticClass:"glyphicon glyphicon-user",on:{click:t.menu3}})]),a("span",{staticClass:"glyphicon glyphicon-cog",staticStyle:{"margin-top":"7.5em","text-align":"center"}})])},m=[],v=new s["a"],g={methods:{menu1:function(){v.$emit("val","1")},menu2:function(){v.$emit("val","2")},menu3:function(){v.$emit("val","3")}}},h=g,_=(a("93f0"),Object(i["a"])(h,d,m,!1,null,null,null)),b=_.exports,y=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[1==t.kk?a("div",[a("Create")],1):t._e(),2==t.kk?a("div",[a("Chat")],1):t._e(),3==t.kk?a("div",[a("Profile")],1):t._e()])},C=[],S=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"createGroup"},[t._m(0),t._m(1),a("br"),a("label",{attrs:{for:"photo",id:"photoLab"}},[t._v("Photo")]),a("div",{attrs:{id:"photo"}},[a("center",[a("img",{attrs:{src:"img/avatar.png",alt:"150*150"}})]),a("center",[a("p",{staticStyle:{color:"rgb(144, 144, 151)"}},[t._v("You can upload jpg,gif or png files.")])]),a("center",[a("p",{staticStyle:{color:"rgb(144, 144, 151)"}},[t._v("Max file size 3mb.")])])],1),a("br"),t._m(2),a("br"),t._m(3),a("br"),t._m(4),a("br"),a("br"),a("center",[a("button",{staticClass:"btn btn-primary btn-lg ",attrs:{type:"button"}},[t._v("Create group")])])],1)},w=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("h3",[a("strong",[t._v("Create group")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"cre-box"},[a("div",{staticClass:"input-group",staticStyle:{display:"flex"}},[a("input",{staticClass:"form-control",attrs:{type:"text",placeholder:"Search for message or users..."}}),a("input",{staticClass:"search",attrs:{type:"button"}})])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"settingAccount"},[a("label",{attrs:{for:"cgName"}},[t._v("Name")]),a("input",{staticClass:"form-control",attrs:{type:"text",id:"cgName",placeholder:"Group Name"}})])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"settingAccount"},[a("label",{attrs:{for:"cgTopic"}},[t._v("Topic(optional)")]),a("input",{staticClass:"form-control",attrs:{type:"text",id:"cgTopic",placeholder:"Group Topic"}})])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"settingAccount"},[a("label",{attrs:{for:"cgDes"}},[t._v("Description")]),a("input",{staticClass:"form-control",attrs:{type:"text",id:"cgDes",placeholder:"Group Description"}})])}],x=(a("d66e"),{}),$=Object(i["a"])(x,S,w,!1,null,null,null),T=$.exports,E=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"mainChat"},[a("div",{attrs:{id:"chat"}},[a("Dialog")],1),1==t.mm?a("div",{staticClass:"popup"},[a("Share")],1):t._e(),2==t.mm?a("div",{staticClass:"popup"},[a("Xiugai")],1):t._e()])},k=[],j=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"mainDialog"},[a("div",{attrs:{id:"daohang"}},[t._m(0),a("a",{attrs:{href:"#",id:"daoa",title:"搜索"},on:{click:t.isSearch}},[a("span",{staticClass:"fa fa-search"})]),a("a",{attrs:{href:"#",title:"分享"},on:{click:t.show1}},[a("span",{staticClass:"fa fa-user-plus"})]),a("li",{staticClass:"dropdown",staticStyle:{"list-style-type":"none",position:"relative"}},[t._m(1),a("ul",{staticClass:"dropdown-menu",attrs:{id:"daohangUl"}},[a("li",{on:{click:t.show2}},[t._v("Mute"),a("span",{staticClass:"fa fa-sliders",staticStyle:{transform:"rotate(-90deg)"}})]),t._m(2)])])]),a("div",{ref:"chatShow",attrs:{id:"chatShow"}},[1==t.isShow?a("div",{staticStyle:{width:"80%","margin-left":"10%","margin-top":"2em"}},[t._m(3)]):t._e(),a("header",[t._v("聊天室人数:"+t._s(t.count))]),t._l(t.list,(function(e,s){return a("div",{key:s,staticClass:"msg"},[a("p",[t._v(t._s(e.content))])])}))],2),a("div",{attrs:{id:"chatSend"}},[a("div",{attrs:{id:"fasong"}},[a("textarea",{directives:[{name:"model",rawName:"v-model",value:t.contentText,expression:"contentText"}],ref:"sendMsg",attrs:{cols:"140",rows:"4",placeholder:"Type your message..."},domProps:{value:t.contentText},on:{keyup:function(e){return!e.type.indexOf("key")&&t._k(e.keyCode,"enter",13,e.key,"Enter")?null:t.sendText()},input:function(e){e.target.composing||(t.contentText=e.target.value)}}})]),t._m(4),a("a",{attrs:{href:"#"},on:{click:function(e){return t.getData()}}},[a("span",{staticClass:"fa fa-paperclip"})]),a("div",{attrs:{id:"senda"},on:{click:function(e){return t.sendText()}}},[a("center",[a("a",{attrs:{href:"#"}},[a("span",{staticClass:"fa fa-send-o"})])])],1)])])},O=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{attrs:{id:"daoSelf"}},[a("img",{attrs:{src:"img/logo.png"}}),a("div",{staticStyle:{"margin-left":"1em"}},[a("h5",[t._v("Name")]),a("p",[t._v("简介")])])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("a",{staticClass:"dropdown-toggle",attrs:{href:"#","data-toggle":"dropdown"}},[a("span",{staticClass:"fa fa-ellipsis-v",attrs:{title:"更多"}})])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("li",[t._v("Delet"),a("span",{staticClass:"fa fa-trash-o"})])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"input-group",staticStyle:{display:"flex"}},[a("input",{staticClass:"form-control",attrs:{type:"text",placeholder:"Search for message or users"}}),a("input",{staticClass:"search",attrs:{type:"button"}})])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("a",{attrs:{href:"#"}},[a("span",{staticClass:"fa fa-smile-o"})])}],P={data:function(){return{isShow:-1,ws:null,count:0,userId:null,list:[],contentText:""}},mounted:function(){this.initWebSocket()},methods:{show1:function(){v.$emit("obj","1")},show2:function(){v.$emit("obj","2")},show0:function(){v.$emit("obj","0")},isSearch:function(){this.isShow=-this.isShow},scrollBottom:function(){var t=this.$refs["chatShow"];t.scrollTop=t.scrollHeight},sendText:function(){var t=this;if(t.$refs["sendMsg"].focus(),t.contentText){var e={msg:t.contentText};t.ws.send(JSON.stringify(e)),t.contentText="",setTimeout((function(){t.scrollBottom()}),500)}},initWebSocket:function(){var t=this;if(window.WebSocket){var e=new WebSocket("ws://");t.ws=e,e.onopen=function(t){console.log("服务器连接成功")},e.onclose=function(t){console.log("服务器连接关闭")},e.onerror=function(){console.log("服务器连接出错")},e.onmessage=function(e){var a=JSON.parse(e.data);t.list.push({userName:a.from_user,msg:a.msg})}}},getData:function(){var t=this;alert("aa"),t.$http.get("http://39.106.119.191/api/user").then((function(t){console.log(t)}),(function(t){console.log(t)}))}}},D=P,I=(a("4f49"),Object(i["a"])(D,j,O,!1,null,null,null)),M=I.exports,N=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"mainShare"},[a("div",{attrs:{id:"close"}},[a("img",{attrs:{src:"img/close.png"},on:{click:t.close}})]),a("div",{attrs:{id:"shareIntro"}},[t._m(0),a("div",{attrs:{id:"shuoming"}},[a("center",[t._v("blablablablabla")])],1)]),t._m(1)])},z=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{attrs:{id:"shareGroup"}},[a("div",{attrs:{id:"shareTou"}},[a("img",{attrs:{src:"img/logo.png"}})]),a("div",{staticStyle:{"margin-left":"5%"}},[a("h3",[t._v("Documentation")]),a("a",{attrs:{href:"#"}},[t._v(" Quick setup and build tools. "),a("span",{staticClass:"glyphicon glyphicon-link",staticStyle:{"font-size":"1em",color:"rgb(193, 197, 203)"}})])])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{attrs:{id:"fenxiang"}},[a("br"),a("div",{attrs:{id:"fen"}},[a("br"),a("p",[t._v("新浪微博"),a("a",{attrs:{href:"#"}},[a("span",{staticClass:"fa fa-weibo"})])]),a("hr"),a("p",[t._v("微信"),a("a",{attrs:{href:"#"}},[a("span",{staticClass:"fa fa-weixin"})])]),a("hr"),a("p",[t._v("QQ"),a("a",{attrs:{href:"#"}},[a("span",{staticClass:"fa fa-qq"})])])])])}],G={methods:{close:function(){v.$emit("obj","0")}}},W=G,A=(a("3a11"),Object(i["a"])(W,N,z,!1,null,null,null)),B=A.exports,J=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"mainXiugai"},[a("div",{attrs:{id:"close"}},[a("img",{attrs:{src:"img/close.png"},on:{click:t.close}})]),a("div",{attrs:{id:"selfInt"}},[a("br"),a("center",[a("div",{attrs:{id:"touxiang"}},[a("img",{attrs:{src:"img/logo.png"}})])]),a("center",[a("h4",[a("b",[t._v("Matthew Wiggins")])])]),a("center",[a("p",{staticStyle:{color:"rgb(187,192,198)","font-size":"1.2em"}},[t._v("这是一段个人简介")])])],1),a("div",{attrs:{id:"setInt"}},[a("br"),a("div",{attrs:{id:"setPhoto"}},[a("p",[t._v("Photo")]),a("div",{attrs:{id:"setphoto"}},[a("center",[a("img",{attrs:{src:"img/avatar.png",width:"50px",height:"42px"}})]),a("center",[a("p",{staticStyle:{color:"rgb(144, 144, 151)"}},[t._v("You can upload jpg,gif or png files.")])]),a("center",[a("p",{staticStyle:{color:"rgb(144, 144, 151)"}},[t._v("Max file size 3mb.")])])],1)]),t._m(0),t._m(1),t._m(2),a("button",{staticClass:"btn btn-primary btn-lg btn-block",attrs:{type:"button"}},[t._v("确认保存")])])])},q=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{attrs:{id:"setName"}},[a("p",[t._v("Name")]),a("input",{staticClass:"form-control",attrs:{type:"text",id:"name",placeholder:"Type your name"}})])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticStyle:{"margin-top":"1em"},attrs:{id:"setTopic"}},[a("p",[t._v("Topic(optional)")]),a("input",{staticClass:"form-control",attrs:{type:"text",id:"topic",placeholder:"Group Topic"}})])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticStyle:{"margin-top":"1em"},attrs:{id:"setDes"}},[a("p",[t._v("Description")]),a("textarea",{staticClass:"form-control",attrs:{rows:"2",id:"des",placeholder:"Group Description"}})])}],L={methods:{close:function(){v.$emit("obj","0")}}},Q=L,U=(a("3236"),Object(i["a"])(Q,J,q,!1,null,null,null)),X=U.exports,Y={data:function(){return{mm:0}},components:{Dialog:M,Share:B,Xiugai:X},mounted:function(){var t=this,e=this;v.$on("obj",(function(t){e.mm=t})),this.$watch("mm",(function(){if(0==t.mm){var e=document.getElementById("chat");e.style="width:100%"}else{var a=document.getElementById("chat");a.style="width:75%"}}))}},R=Y,H=(a("f196"),Object(i["a"])(R,E,k,!1,null,null,null)),F=H.exports,K=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"mainProfile"},[a("div",{attrs:{id:"Profile"}},[t._m(0),t._m(1),a("div",{staticClass:"pro-box",attrs:{id:"proOne"}},[a("br"),a("center",[a("div",{attrs:{id:"touxiang"}},[a("img",{attrs:{src:"img/logo.png"}})])]),a("center",[a("h4",[a("b",[t._v("Matthew Wiggins")])])]),a("center",[a("p",{staticStyle:{color:"rgb(187,192,198)","font-size":"1.2em"}},[t._v("这是一段个人简介")])])],1),t._m(2)]),a("div",{attrs:{id:"Settings"}},[t._m(3),a("p",{staticStyle:{"margin-left":"5%","font-size":"1.2em",color:"rgb(144, 144, 151)"}},[t._v("Update your profile details")]),a("hr"),a("div",{attrs:{id:"upSet"}},[t._m(4),a("hr"),a("div",{attrs:{id:"avatar"}},[a("label",{attrs:{for:"ava"}},[t._v("Avatar")]),a("div",{attrs:{id:"ava"}},[a("center",[a("img",{attrs:{src:"img/avatar.png",alt:"150*150"}})]),a("center",[a("p",{staticStyle:{color:"rgb(144, 144, 151)"}},[t._v("You can upload jpg,gif or png files.")])]),a("center",[a("p",{staticStyle:{color:"rgb(144, 144, 151)"}},[t._v("Max file size 3mb.")])])],1)]),t._m(5),a("br"),t._m(6),a("br"),t._m(7),a("br"),a("center",[a("button",{staticClass:"btn btn-primary btn-lg ",attrs:{type:"button"}},[t._v("Save Preferences")])])],1)])])},V=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("h3",[a("strong",[t._v("Profile")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"pro-box"},[a("div",{staticClass:"input-group",staticStyle:{display:"flex"}},[a("input",{staticClass:"form-control",attrs:{type:"text",placeholder:"Search for message or users"}}),a("input",{staticClass:"search",attrs:{type:"button"}})])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"pro-box",attrs:{id:"proTwo"}},[a("br"),a("div",{staticClass:"proTwoInf"},[a("div",{staticClass:"proTwoSpan"},[a("p",[t._v("Country")]),a("span",[t._v("Warsaw,Poland")])]),a("div",{staticClass:"proTwoImg"},[a("img",{attrs:{src:"img/diqiu.png"}})])]),a("hr"),a("div",{staticClass:"proTwoInf"},[a("div",{staticClass:"proTwoSpan"},[a("p",[t._v("Phone")]),a("span",[t._v("+39 02 8721 43 19")])]),a("div",{staticClass:"proTwoImg"},[a("img",{attrs:{src:"img/yuyin.png"}})])]),a("hr"),a("div",{staticClass:"proTwoInf"},[a("div",{staticClass:"proTwoSpan"},[a("p",[t._v("Email")]),a("span",[t._v("anna@gmail.com")])]),a("div",{staticClass:"proTwoImg"},[a("img",{attrs:{src:"img/youjian.png"}})])]),a("hr"),a("div",{staticClass:"proTwoInf"},[a("div",{staticClass:"proTwoSpan"},[a("p",[t._v("Time")]),a("span",[t._v("10:03 am")])]),a("div",{staticClass:"proTwoImg"},[a("img",{attrs:{src:"img/shizhong.png"}})])])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("h4",{staticStyle:{"margin-left":"5%"}},[a("strong",[t._v("Settings")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticStyle:{height:"10%",display:"flex"},attrs:{id:"account"}},[a("div",{staticStyle:{width:"83%"}},[a("h4",{staticStyle:{"margin-left":"5%"}},[a("strong",[t._v("Account")])]),a("p",{staticStyle:{"margin-left":"5%","font-size":"1.2em",color:"#8a8a91"}},[t._v("Update your profile details.")])]),a("img",{attrs:{src:"img/account.png"}})])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"proSet"},[a("label",{attrs:{for:""}},[t._v("Name")]),a("input",{staticClass:"form-control",attrs:{type:"text",id:"name",placeholder:"Type your name"}})])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"proSet"},[a("label",{attrs:{for:""}},[t._v("Phone")]),a("input",{staticClass:"form-control",attrs:{type:"text",id:"phone",placeholder:"(123) 456-7890"}})])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"proSet"},[a("label",{attrs:{for:""}},[t._v("Email")]),a("input",{staticClass:"form-control",attrs:{type:"text",id:"email",placeholder:"you@yoursite.com"}})])}],Z=(a("1be2"),{}),tt=Object(i["a"])(Z,K,V,!1,null,null,null),et=tt.exports,at={data:function(){return{kk:1}},components:{Create:T,Chat:F,Profile:et},mounted:function(){var t=this;v.$on("val",(function(e){t.kk=e}))}},st=at,nt=Object(i["a"])(st,y,C,!1,null,null,null),rt=nt.exports,it={components:{Left:b,Right:rt}},ot=it,ct=(a("5ca1"),Object(i["a"])(ot,p,f,!1,null,null,null)),lt=ct.exports;s["a"].use(u["a"]);var ut=[{path:"/",component:lt}],pt=new u["a"]({mode:"history",base:"/",routes:ut}),ft=pt,dt=a("28dd");s["a"].config.productionTip=!1,s["a"].use(dt["a"]),new s["a"]({router:ft,render:function(t){return t(l)}}).$mount("#app")},"5ca1":function(t,e,a){"use strict";var s=a("f255"),n=a.n(s);n.a},"6a82":function(t,e,a){},"85ec":function(t,e,a){},"93f0":function(t,e,a){"use strict";var s=a("c2d9"),n=a.n(s);n.a},c2d9:function(t,e,a){},c52b:function(t,e,a){},d077:function(t,e,a){},d66e:function(t,e,a){"use strict";var s=a("d077"),n=a.n(s);n.a},f196:function(t,e,a){"use strict";var s=a("1e3e"),n=a.n(s);n.a},f255:function(t,e,a){},faf5:function(t,e,a){}});
//# sourceMappingURL=app.58326244.js.map