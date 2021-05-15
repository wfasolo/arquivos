//variables
var baseurl = 'https://privacidade.paulus.com.br/script';  
var use_lgpd = document.getElementById('use_lgpd').value;

var text_banner = 'Utilizamos cookies e outras tecnologias semelhantes para melhorar a sua experiência em nossos serviços, personalizar publicidade e recomendar conteúdo de seu interesse. Ao utilizar nossos serviços, você concorda com nossa ';
var text_alter = '<p id="cookie-banner-lgpd-mb-15"><b>Política alterada</b></p>';
var link_policy_privacy = 'https://privacidade.paulus.com.br';
var link_portal_privacy = 'https://privacidade.paulus.com.br';
var text_button = 'OK, entendi!';
var version_lgpd = '1.0';// ao alterar a versão irá pedir para o usuário aceitar novamente os termos

//import css / call function inside function show
function import_css(){
    var head  = document.getElementsByTagName('head')[0];
    var link  = document.createElement('link');           
    link.rel  = 'stylesheet';
    link.type = 'text/css';
    link.href = baseurl + '/css/lgpd-paulus-lib.min.css';
    link.media = 'all';
    head.appendChild(link); 
} 

//create background
function create_back_tranp(){    
    var div  = document.createElement('div');  
    div.setAttribute("id", "loader-overlay");
    
    document.body.insertBefore(div, document.body.firstChild);     
}

//hide background
function hide_back(){   
    div_back = document.getElementById('loader-overlay');
	div_back.setAttribute("style", "display:none")
}

//functions manipulate cookies
function set_cookie(name, value, days) {
    var d = new Date;
    d.setTime(d.getTime() + 24*60*60*1000*days);
    document.cookie = name + "=" + value + ";path=/;expires=" + d.toGMTString();
}

function get_cookie(name){
    var v = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
    return v ? v[2] : null;
}

function delete_cookie(){
    var current_version_cookie = get_cookie('lgpd-paulus-version'+use_lgpd); 
    if(current_version_cookie != null){
        if(version_lgpd.replace('.','') > current_version_cookie.replace('.','')){
            set_cookie('lgpd-paulus-version'+use_lgpd, '', -1);
            set_cookie('lgpd-paulus-accepted'+use_lgpd, '', -1);   
            text_banner = text_alter + text_banner; 
            text_alter = '';        
        }   
    }
}

function first_view_cookie(){
    var exist_cookie = get_cookie('lgpd-paulus-first-view'+use_lgpd); 
    if(exist_cookie === null){
        set_cookie('lgpd-paulus-first-view'+use_lgpd, true, 365); 
    }else{  
        text_banner = text_alter + text_banner;   
    }
}

var LGPDPAULUS = (function (e) {    
    var t = {};
    delete_cookie();
    first_view_cookie();
    function n(o) {
        if (t[o]) return t[o].exports;
        var r = (t[o] = { i: o, l: !1, exports: {} });
        return e[o].call(r.exports, r, r.exports, n), (r.l = !0), r.exports;
    }
    return (
        (n.m = e),
        (n.c = t),
        (n.d = function (e, t, o) {
            n.o(e, t) || Object.defineProperty(e, t, { enumerable: !0, get: o });
        }),
        (n.r = function (e) {
            "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, { value: "Module" }), Object.defineProperty(e, "__esModule", { value: !0 });
        }),
        (n.t = function (e, t) {
            if ((1 & t && (e = n(e)), 8 & t)) return e;
            if (4 & t && "object" == typeof e && e && e.__esModule) return e;
            var o = Object.create(null);
            if ((n.r(o), Object.defineProperty(o, "default", { enumerable: !0, value: e }), 2 & t && "string" != typeof e))
                for (var r in e)
                    n.d(
                        o,
                        r,
                        function (t) {
                            return e[t];
                        }.bind(null, r)
                    );
            return o;
        }),
        (n.n = function (e) {
            var t =
                e && e.__esModule
                    ? function () {
                          return e.default;
                      }
                    : function () {
                          return e;
                      };
            return n.d(t, "a", t), t;
        }),
        (n.o = function (e, t) {
            return Object.prototype.hasOwnProperty.call(e, t);
        }),
        (n.p = ""),
        n((n.s = 1))
    );
})([
    function (e, t, n) {
        "use strict";
        
        Object.defineProperty(t, "__esModule", { value: !0 });
        t.default = class {
            static getCookie(e) {
                return document.cookie.split(";").filter((t) => t.includes(e));
            }
            static setCookie({ cookieName: e, value: t, domain: n = "" }) {
                
                const o = new Date();
                o.setTime(o.getTime() + 31104e6);
                const r = n && "" !== n ? `domain=${n};` : "";
                document.cookie = `${e}=${t};${r}path=/;expires=${o.toUTCString()};`;
            }
            static deleteCookie({ cookieName: e, domain: t = "" }) {
                const n = t && "" !== t ? `domain=${t};` : "";
                document.cookie = `${e}='';${n}path=/;expires=Thu, 01 Jan 1970 00:00:00 GMT;`;
            }
        };
    },
    function (e, t, n) {
        "use strict";
        Object.defineProperty(t, "__esModule", { value: !0 });
        const o = { CookieBanner: n(2).default };
        t.default = o;
    },
    function (e, t, n) {
        "use strict";
        Object.defineProperty(t, "__esModule", { value: !0 });
        const o = n(3),
            r = n(5),
            i = n(0),
            a = n(6),
            s = n(7),
            u = n(8);
        n(9), n(11);
        t.default = class {
            constructor(e = {}) {
                (this.domainName = ""),
                    (this.options = u.Options.merge(e)),
                    (this.animator = new r.default(this.options.animation)),
                    (this.dom = new s.default({ ...this.options })),
                    (this.cookieVersioning = new a.default()),
                    (this.datetimeOnInit = new Date()),
                    this.start(),
                    (this.analytics = new o.default(this.environment, this.options.tenant));
            }
            start() {                
                (this.domainName = this.chooseDomainName(window.location.hostname)), this.setEnvironment(), this.setInitialCookie(), this.toggleCookieBanner(), this.setAllListeners();
            }
            setEnvironment() {
                this.domainName.includes(".paulus.com.br") ? (this.environment = "qa") : ["localhost", "127.0.0.1", "192.168.240.38"].includes(this.domainName) ? (this.environment = "dev") : (this.environment = "prod");
            }
            setInitialCookie() {
                const e = i.default.getCookie("lgpd-paulus-accepted"+use_lgpd),
                    t = String(e.some((e) => e && e.includes("true")));
                e.length > 1 &&
                    [".paulus.com.br", ".paulus.com.br", ""].forEach((e) => {
                        i.default.deleteCookie({ cookieName: "lgpd-paulus-accepted"+use_lgpd, domain: e });
                    }),
                    1 != e.length && i.default.setCookie({ cookieName: "lgpd-paulus-accepted"+use_lgpd, value: t, domain: this.domainName });
            }
            show(e) {   
                import_css(); 
                create_back_tranp();
                e.setAttribute("class", "cookie-banner-lgpd-visible"), this.animator.animateIn(e), e.setAttribute("style", "display:flex;"), this.options.lifecycle.onCookieBannerShow && this.options.lifecycle.onCookieBannerShow(e);
            }
            async hide(e) {               
                e.setAttribute("class", "cookie-banner-lgpd-hidden"), await this.animator.animateOut(e), e.setAttribute("style", "display:none"), this.options.lifecycle.onCookieBannerHide && this.options.lifecycle.onCookieBannerHide(e);
            }
            chooseDomainName(e) {
                let t = "";
                return (
                    [".paulus.com.br", ".paulus.com.br", "localhost", "127.0.0.1", "192.168.240.38"].forEach((n) => {
                        e.includes(n) && (t = n);
                    }),
                    t
                );
            }
            getOrCreateCookieBannerLgpd() {                               
                return this.dom.getCookieBanner() || this.dom.injectCookieInPage();
            }
            toggleCookieBanner() {
                const e = this.getOrCreateCookieBannerLgpd();
                !i.default.getCookie("lgpd-paulus-accepted"+use_lgpd).some((e) => e && e.includes("true")) || this.cookieVersioning.isAcceptedCookieVersionBefore() ? this.show(e) : this.hide(e);
            }
            setClickListener(e, t) {                
                const n = document.getElementsByClassName(e);
                Array.from(n).forEach((e) => {
                    e.addEventListener("click", t.bind(this));
                });
            }
            onButtonClick(e) {
                hide_back();
                this.options.lifecycle.onConsentAccepted && this.options.lifecycle.onConsentAccepted(e);
                const t = { eventCategory: "lgpd-analytics", eventAction: "click", eventLabel: text_button, eventValue: new Date().valueOf() - this.datetimeOnInit.valueOf() };
                this.analytics.sendCommonEvent(t),
                    e.defaultPrevented || (i.default.setCookie({ cookieName: "lgpd-paulus-accepted"+use_lgpd, value: "true", domain: this.domainName }), this.cookieVersioning.setVersionCookie(this.domainName), this.toggleCookieBanner());
            }
            onPrivacyLinkClick() {
                this.analytics.sendCommonEvent({ eventCategory: "lgpd-analytics", eventAction: "link", eventLabel: "Polí­tica de Privacidade" });
            }
            onPrivacyPortalLinkClick() {
                this.analytics.sendCommonEvent({ eventCategory: "lgpd-analytics", eventAction: "link", eventLabel: "Portal da Privacidade" });
            }
            setAllListeners() {
                this.setClickListener("cookie-banner-lgpd_privacy-link", this.onPrivacyLinkClick),
                    this.setClickListener("cookie-banner-lgpd_accept-button", this.onButtonClick),
                    this.setClickListener("cookie-banner-lgpd_privacy-portal-link", this.onPrivacyPortalLinkClick);
            }
        };
    },
    function (e, t, n) {
        "use strict";
        Object.defineProperty(t, "__esModule", { value: !0 });
        const o = n(4);
        t.default = class {
            constructor(e, t) {
                (this.tenant = t), (this.environment = e), this.init();
            }
            init() {                
                let e = null;
                window.cdaaas && window.cdaaas.SETTINGS && window.cdaaas.SETTINGS.SITE_ID && (e = window.cdaaas.SETTINGS.SITE_ID),
                    (this.tenant = this.tenant || e),
                    this.tenant && ("prod" != this.environment && o.Settings.useQAConfiguration(), (this.client = new o.HorizonClient(this.tenant, "desktop")));
            }
            sendCommonEvent(e) {
                if (this.client)
                    try {
                        this.client.send({ id: "common-event", version: "0.1", contentType: "common", properties: e });
                    } catch (e) {
                        console.error("Erro ao enviar o common-event");
                    }
            }
        };
    },
    function (e, t, n) {
        "undefined" != typeof self && self,
            (e.exports = (function (e) {
                var t = {};
                function n(o) {
                    if (t[o]) return t[o].exports;
                    var r = (t[o] = { i: o, l: !1, exports: {} });
                    return e[o].call(r.exports, r, r.exports, n), (r.l = !0), r.exports;
                }
                return (
                    (n.m = e),
                    (n.c = t),
                    (n.d = function (e, t, o) {
                        n.o(e, t) || Object.defineProperty(e, t, { configurable: !1, enumerable: !0, get: o });
                    }),
                    (n.n = function (e) {
                        var t =
                            e && e.__esModule
                                ? function () {
                                      return e.default;
                                  }
                                : function () {
                                      return e;
                                  };
                        return n.d(t, "a", t), t;
                    }),
                    (n.o = function (e, t) {
                        return Object.prototype.hasOwnProperty.call(e, t);
                    }),
                    (n.p = ""),
                    n((n.s = 6))
                );
            })([
                function (e, t, n) {
                    "use strict";
                    Object.defineProperty(t, "__esModule", { value: !0 });
                    var o = r(n(10));
                    function r(e) {
                        return e && e.__esModule ? e : { default: e };
                    }
                    var i = {
                            AVOID_COOKIE_USAGE: !1,
                            EVENTS_BUFFER_SIZE: 100,
                            EVENTS_SENDER_INTERVAL: 1e4,
                            EVENTS_SENDER_MIN_INTERVAL: 5e3,
                            EVENTS_SENDER_MAX_INTERVAL: 2e4,
                            EVENTS_DISCARD_AFTER_MSECS: 36e5,
                            EVENTS_BULK_SIZE: 10,
                            HORIZON_CALLBACK_STACK_LIMIT: 1e3,
                            HORIZON_TRACK_IDENTIFICATION_RESOURCE: "id",
                            HORIZON_TRACK_HOST: "paulus.com.br",
                            HORIZON_CLIENT_UUID: r(n(2)).default.getResource("clientInstanceUUID", (0, o.default)()),
                            HORIZON_REQUEST_ENCODING: "base64",
                            HORIZON_SCHEMAS_HOST: "paulus.com.br",
                            IDENTIFICATION_LOAD_RETRY_AFTER_MSECS: 5e3,
                            PACKAGE_VERSION: "1.7.0",
                            SCHEMA_VALIDATOR_SCRIPT_URL: baseurl + "/js/tv4.min.js",
                            SCHEMA_VALIDATOR_SCRIPT_MAX_RETRIES: 2,
                            SCHEMA_LOAD_COLLECTION_RETRY_AFTER_MSECS: 1e4,
                            USE_HTTPS: !0,
                        },
                        a = {
                            avoidCookieUsage: function () {
                                i.AVOID_COOKIE_USAGE = !0;
                            },
                            useHTTPOnly: function () {
                                i.USE_HTTPS = !1;
                            },
                            useQAConfiguration: function () {
                                (i.HORIZON_TRACK_HOST = "paulus.com.br"), (i.HORIZON_SCHEMAS_HOST = "paulus.com.br"), (i.HORIZON_REQUEST_ENCODING = "json");
                            },
                        };
                    t.default = Object.assign(i, a);
                },
                function (e, t, n) {
                    "use strict";
                    Object.defineProperty(t, "__esModule", { value: !0 });
                    var o = {
                            COMPONENT_NOT_READY: "[Horizon] Component is not ready.",
                            COMPONENT_UNAVAILABLE: "[Horizon] Class or function is required.",
                            DUPLICATED_SCHEMA: "[Horizon] Duplicated schema.",
                            ERROR_LOADING_RESOURCE: "[Horizon] Failed to load resource.",
                            INVALID_AUTH_TOKEN: "[Horizon] Invalid authorization token.",
                            INVALID_DATA: "[Horizon] Invalid data.",
                            INVALID_DATE: "[Horizon] Invalid date-time RFC 3339 format.",
                            INVALID_ENVIRONMENT: "[Horizon] Invalid environment value.",
                            INVALID_FORMAT: "[Horizon] Invalid event format.",
                            INVALID_REQUEST: "[Horizon] Invalid request.",
                            INVALID_TIMESTAMP: "[Horizon] Invalid timestamp.",
                            INVALID_VERSION_FORMAT: "[Horizon] Invalid version format.",
                            LIMIT_EXCEEDED: "[Horizon] Resource limit exceeded.",
                            MUST_BE_DEFINED: "[Horizon] Parameter or argument must be defined",
                            SCHEMA_VALIDATOR_ERROR_LOADING: "[Horizon] Could not load SchemaValidator.",
                            UNSUPPORTED_TYPE: "[Horizon] Unsupported type.",
                            UNSUPPORTED_TENANT: "[Horizon] Unsupported tenant.",
                            UNSUPPORTED_ENCODER: "[Horizon] Unsupported encoder.",
                            USE_MANAGER_ONLY_WHEN_AVOIDING_COOKIE: "[Horizon] Can not set or remove a logged user when AVOID_COOKIE_USAGE is not enabled.",
                        },
                        r = {
                            mustBeDefined: function (e) {
                                throw new Error(o.MUST_BE_DEFINED + ": " + e + ".");
                            },
                        };
                    t.default = Object.assign(o, r);
                },
                function (e, t, n) {
                    "use strict";
                    Object.defineProperty(t, "__esModule", { value: !0 });
                    var o = function () {
                        return (window.horizonResources = window.horizonResources || {}), window.horizonResources;
                    };
                    t.default = {
                        getContext: o,
                        getResource: function (e, t) {
                            var n = o();
                            return (n[e] = n[e] || t), n[e];
                        },
                    };
                },
                function (e, t, n) {
                    "use strict";
                    Object.defineProperty(t, "__esModule", { value: !0 }),
                        (t.default = {
                            execAsync: function (e, t) {
                                setTimeout(function () {
                                    return e(t);
                                }, 1);
                            },
                        });
                },
                function (e, t, n) {
                    "use strict";
                    Object.defineProperty(t, "__esModule", { value: !0 }),
                        (t.default = {
                            request: function (e, t, n, o) {
                                var r = new XMLHttpRequest();
                                r.open(e, t, !0),
                                    (r.onload = function () {
                                        return r.status < 400 ? n(JSON.parse(r.response)) : o(r.response);
                                    }),
                                    (r.onerror = o),
                                    r.send();
                            },
                        });
                },
                function (e, t, n) {
                    "use strict";
                    Object.defineProperty(t, "__esModule", { value: !0 });
                    var o = (function () {
                            function e(e, t) {
                                for (var n = 0; n < t.length; n++) {
                                    var o = t[n];
                                    (o.enumerable = o.enumerable || !1), (o.configurable = !0), "value" in o && (o.writable = !0), Object.defineProperty(e, o.key, o);
                                }
                            }
                            return function (t, n, o) {
                                return n && e(t.prototype, n), o && e(t, o), t;
                            };
                        })(),
                        r = c(n(3)),
                        i = c(n(2)),
                        a = c(n(1)),
                        s = c(n(4)),
                        u = c(n(0));
                    function c(e) {
                        return e && e.__esModule ? e : { default: e };
                    }
                    var l = function () {
                            return i.default.getResource("idManager", { loggedIDs: null, anonymousIDs: null, sessionIDs: null });
                        },
                        d = ["GLBID", "GST"],
                        f = "statusReady",
                        h = "statusNotReady",
                        p = "statusLoading",
                        v = "statusScheduled",
                        y = "statusError",
                        m = (function () {
                            function e(t, n) {
                                !(function (e, t) {
                                    if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function");
                                })(this, e),
                                    (this.state = n ? f : h),
                                    (this.url = t),
                                    (this.bypass = n),
                                    (this.callbacks = { onReady: [], onError: [], onRetry: [], onLoad: [] });
                            }
                            return (
                                o(e, [
                                    {
                                        key: "onLoad",
                                        value: function (e) {
                                            this.callbacks.onLoad.push(e);
                                        },
                                    },
                                    {
                                        key: "onRetry",
                                        value: function (e) {
                                            this.callbacks.onRetry.push(e);
                                        },
                                    },
                                    {
                                        key: "onReady",
                                        value: function (e) {
                                            if (this.state === f) return e(this.getClientIDs());
                                            if (this.callbacks.onReady.length > u.default.HORIZON_CALLBACK_STACK_LIMIT) throw new Error(a.default.LIMIT_EXCEEDED + " IDManager callback stack.");
                                            return this.callbacks.onReady.push(e);
                                        },
                                    },
                                    {
                                        key: "onError",
                                        value: function (e) {
                                            this.state === y ? e() : this.callbacks.onError.push(e);
                                        },
                                    },
                                    {
                                        key: "getAsKeyValue",
                                        value: function () {
                                            if (!this.isReady()) throw new Error("" + a.default.COMPONENT_NOT_READY);
                                            if (this.bypass) return "";
                                            var e = this.getClientIDs();
                                            return Object.keys(e)
                                                .map(function (t) {
                                                    return encodeURIComponent(t) + "=" + encodeURIComponent(e[t]);
                                                })
                                                .join("&");
                                        },
                                    },
                                    {
                                        key: "getClientIDs",
                                        value: function () {
                                            var e = l();
                                            return Object.assign(e.loggedIDs || {}, e.anonymousIDs || {}, e.sessionIDs || {});
                                        },
                                    },
                                    {
                                        key: "isReady",
                                        value: function () {
                                            return this.state === f;
                                        },
                                    },
                                    {
                                        key: "retry",
                                        value: function () {
                                            var e = this;
                                            (this.state = v),
                                                this.callbacks.onRetry.forEach(function (e) {
                                                    return e();
                                                }),
                                                setTimeout(function () {
                                                    (e.state = h), e.load();
                                                }, u.default.IDENTIFICATION_LOAD_RETRY_AFTER_MSECS);
                                        },
                                    },
                                    {
                                        key: "setLoggedUser",
                                        value: function (e, t) {
                                            if (-1 === d.indexOf(e)) throw Error(a.default.INVALID_AUTH_TOKEN);
                                            var n = l();
                                            n.loggedIDs = Object.assign(
                                                n.loggedIDs || {},
                                                (function (e, t, n) {
                                                    return t in e ? Object.defineProperty(e, t, { value: n, enumerable: !0, configurable: !0, writable: !0 }) : (e[t] = n), e;
                                                })({}, e, t)
                                            );
                                        },
                                    },
                                    {
                                        key: "setAnonymousUser",
                                        value: function (e) {
                                            var t = !(arguments.length > 1 && void 0 !== arguments[1]) || arguments[1],
                                                n = l();
                                            if (null == n.anonymousIDs || t) {
                                                if (!("glb_uid" in e) || !("glb_uid_public" in e)) throw a.default.mustBeDefined("glb_uid and glb_uid_public");
                                                var o = { glb_uid: e.glb_uid, glb_uid_public: e.glb_uid_public };
                                                n.anonymousIDs = Object.assign(n.anonymousIDs || {}, o);
                                            }
                                        },
                                    },
                                    {
                                        key: "getAnonymousUser",
                                        value: function () {
                                            return l().anonymousIDs;
                                        },
                                    },
                                    {
                                        key: "setSessionID",
                                        value: function (e) {
                                            e.hsid && (l().sessionIDs = Object.assign({}, { hsid: e.hsid }));
                                        },
                                    },
                                    {
                                        key: "removeLoggedUser",
                                        value: function () {
                                            var e = l();
                                            d.forEach(function (t) {
                                                e.loggedIDs[t] && delete e.loggedIDs[t];
                                            });
                                        },
                                    },
                                    {
                                        key: "load",
                                        value: function () {
                                            var e = this;
                                            if (this.state === h) {
                                                (this.state = p),
                                                    this.callbacks.onLoad.forEach(function (e) {
                                                        return e();
                                                    });
                                                var t = u.default.USE_HTTPS ? "https://" : "http://";
                                                s.default.request(
                                                    "GET",
                                                    "" + t + this.url,
                                                    function (t) {
                                                        e.setSessionID(t),
                                                            e.setAnonymousUser(t, !1),
                                                            (e.state = f),
                                                            e.callbacks.onReady.forEach(function (t) {
                                                                return r.default.execAsync(t, e.getClientIDs());
                                                            });
                                                    },
                                                    function (t) {
                                                        (e.state = y),
                                                            e.callbacks.onError.forEach(function (e) {
                                                                return r.default.execAsync(e, t);
                                                            }),
                                                            e.retry();
                                                    }
                                                );
                                            }
                                        },
                                    },
                                ]),
                                e
                            );
                        })(),
                        g = function (e) {
                            var t = l();
                            if (!t.instance) {
                                var n = e || u.default.HORIZON_TRACK_HOST + "/" + u.default.HORIZON_TRACK_IDENTIFICATION_RESOURCE,
                                    o = !1 === u.default.AVOID_COOKIE_USAGE;
                                t.instance = new m(n, o);
                            }
                            return t.instance;
                        };
                    t.default = {
                        getInstance: g,
                        getContextManager: l,
                        setLoggedUser: function (e, t) {
                            if (!u.default.AVOID_COOKIE_USAGE) throw Error(a.default.USE_MANAGER_ONLY_WHEN_AVOIDING_COOKIE);
                            (e && 0 !== e.length) || a.default.mustBeDefined("tokenName"), (t && 0 !== t.length) || a.default.mustBeDefined("tokenValue"), g().setLoggedUser(e, t);
                        },
                        removeLoggedUser: function () {
                            if (!u.default.AVOID_COOKIE_USAGE) throw Error(a.default.USE_MANAGER_ONLY_WHEN_AVOIDING_COOKIE);
                            g().removeLoggedUser();
                        },
                        setAnonymousUser: function (e) {
                            g().setAnonymousUser(e);
                        },
                        getAnonymousUser: function () {
                            return g().getAnonymousUser();
                        },
                    };
                },
                function (e, t, n) {
                    "use strict";
                    Object.defineProperty(t, "__esModule", { value: !0 }), (t.IDManager = t.Settings = t.HorizonClient = void 0), n(7);
                    var o = a(n(9)),
                        r = a(n(0)),
                        i = a(n(5));
                    function a(e) {
                        return e && e.__esModule ? e : { default: e };
                    }
                    var s = { setLoggedUser: i.default.setLoggedUser, removeLoggedUser: i.default.removeLoggedUser, setAnonymousUser: i.default.setAnonymousUser, getAnonymousUser: i.default.getAnonymousUser };
                    (t.HorizonClient = o.default), (t.Settings = r.default), (t.IDManager = s);
                },
                function (e, t, n) {
                    "use strict";
                    n(8).polyfill();
                },
                function (e, t, n) {
                    "use strict";
                    function o(e, t) {
                        if (null == e) throw new TypeError("Cannot convert first argument to object");
                        for (var n = Object(e), o = 1; o < arguments.length; o++) {
                            var r = arguments[o];
                            if (null != r)
                                for (var i = Object.keys(Object(r)), a = 0, s = i.length; a < s; a++) {
                                    var u = i[a],
                                        c = Object.getOwnPropertyDescriptor(r, u);
                                    void 0 !== c && c.enumerable && (n[u] = r[u]);
                                }
                        }
                        return n;
                    }
                    e.exports = {
                        assign: o,
                        polyfill: function () {
                            Object.assign || Object.defineProperty(Object, "assign", { enumerable: !1, configurable: !0, writable: !0, value: o });
                        },
                    };
                },
                function (e, t, n) {
                    "use strict";
                    Object.defineProperty(t, "__esModule", { value: !0 });
                    var o = (function () {
                            function e(e, t) {
                                for (var n = 0; n < t.length; n++) {
                                    var o = t[n];
                                    (o.enumerable = o.enumerable || !1), (o.configurable = !0), "value" in o && (o.writable = !0), Object.defineProperty(e, o.key, o);
                                }
                            }
                            return function (t, n, o) {
                                return n && e(t.prototype, n), o && e(t, o), t;
                            };
                        })(),
                        r = d(n(0)),
                        i = d(n(13)),
                        a = d(n(1)),
                        s = d(n(15)),
                        u = d(n(26)),
                        c = d(n(27)),
                        l = d(n(5));
                    function d(e) {
                        return e && e.__esModule ? e : { default: e };
                    }
                    var f = "stateReady",
                        h = "stateNotReady",
                        p = "stateLoading",
                        v = ["web", "instant-article", "app"],
                        y = (function () {
                            function e() {
                                var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : null,
                                    n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : null,
                                    o = this,
                                    d = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : null,
                                    f = arguments.length > 3 && void 0 !== arguments[3] ? arguments[3] : "web";
                                if (
                                    ((function (e, t) {
                                        if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function");
                                    })(this, e),
                                    (this.tenant = t || c.default.getTenant() || a.default.mustBeDefined("tenant")),
                                    (this.deviceGroup = n || c.default.getDeviceGroup() || a.default.mustBeDefined("deviceGroup")),
                                    (this.defaultContentType = d),
                                    -1 === v.indexOf(f))
                                )
                                    throw Error(a.default.INVALID_ENVIRONMENT);
                                (this.environment = f), (this.validator = i.default), (this.clientVersion = r.default.PACKAGE_VERSION), (this.state = h), (this.referer = document.referrer);
                                var p = null,
                                    y = null,
                                    m = null;
                                (this.setSchemasProvider = function (e) {
                                    p = e;
                                }),
                                    (this.getSchemasProvider = function () {
                                        if (!p) {
                                            var e = u.default.getInstance();
                                            o.setSchemasProvider(e);
                                        }
                                        return p;
                                    }),
                                    (this.setEventBus = function (e) {
                                        y = e;
                                    }),
                                    (this.getEventBus = function () {
                                        if (!y) {
                                            var e = s.default.getInstance(o.tenant, o.deviceGroup, o.environment, o.getIdManager());
                                            o.setEventBus(e);
                                        }
                                        return y;
                                    }),
                                    (this.setIdManager = function (e) {
                                        m = e;
                                    }),
                                    (this.getIdManager = function () {
                                        if (!m) {
                                            var e = l.default.getInstance();
                                            o.setIdManager(e);
                                        }
                                        return m;
                                    }),
                                    (this.isReady = function () {
                                        return !!p && !!m && o.validator.isReady() && p.isReady() && m.isReady();
                                    }),
                                    window.addEventListener("beforeunload", function () {
                                        o.unload();
                                    });
                            }
                            return (
                                o(e, [
                                    {
                                        key: "useDefaultContentType",
                                        value: function (e) {
                                            this.defaultContentType = e;
                                        },
                                    },
                                    {
                                        key: "setValidator",
                                        value: function (e) {
                                            this.validator = e;
                                        },
                                    },
                                    {
                                        key: "setReferer",
                                        value: function (e) {
                                            this.referer = e || document.referrer;
                                        },
                                    },
                                    {
                                        key: "unload",
                                        value: function () {
                                            this.flush();
                                        },
                                    },
                                    {
                                        key: "getScopeInfo",
                                        value: function () {
                                            return { url: document.location.href, actionTs: +Date.now(), horizonClientVersion: this.clientVersion, horizonClientReferer: this.referer };
                                        },
                                    },
                                    {
                                        key: "validateBeforeEnqueue",
                                        value: function (e) {
                                            var t = this.getSchemasProvider().get(e.id, e.version);
                                            this.validator.validateFor(e, t);
                                        },
                                    },
                                    {
                                        key: "onReady",
                                        value: function (e) {
                                            this.validator.isReady()
                                                ? this.getSchemasProvider().isReady()
                                                    ? this.getIdManager().isReady()
                                                        ? ((this.state = f), e())
                                                        : ((this.state = p), this.getIdManager().onReady(e), this.getIdManager().load())
                                                    : ((this.state = p), this.getSchemasProvider().onReady(e), this.getSchemasProvider().load())
                                                : ((this.state = p), this.validator.onReady(e), this.validator.load());
                                        },
                                    },
                                    {
                                        key: "flush",
                                        value: function () {
                                            var e = this;
                                            this.isReady()
                                                ? this.getEventBus().flush()
                                                : this.onReady(function () {
                                                      return e.flush();
                                                  });
                                        },
                                    },
                                    {
                                        key: "send",
                                        value: function (e) {
                                            this.validator.validateArgs(e), this.sendWithInfo(e, this.getScopeInfo());
                                        },
                                    },
                                    {
                                        key: "sendWithInfo",
                                        value: function (e, t) {
                                            var n = this;
                                            if (!this.isReady())
                                                return (
                                                    this.state === h && this.flush(),
                                                    void this.onReady(function () {
                                                        return n.sendWithInfo(e, t);
                                                    })
                                                );
                                            this.validateBeforeEnqueue(e);
                                            var o = Object.assign({}, e, t);
                                            o.contentType || (this.defaultContentType || a.default.mustBeDefined("contentType"), (o.contentType = this.defaultContentType)), this.getEventBus().enqueue(o);
                                        },
                                    },
                                ]),
                                e
                            );
                        })();
                    t.default = y;
                },
                function (e, t, n) {
                    var o = n(11),
                        r = n(12);
                    e.exports = function (e, t, n) {
                        var i = (t && n) || 0;
                        "string" == typeof e && ((t = "binary" === e ? new Array(16) : null), (e = null));
                        var a = (e = e || {}).random || (e.rng || o)();
                        if (((a[6] = (15 & a[6]) | 64), (a[8] = (63 & a[8]) | 128), t)) for (var s = 0; s < 16; ++s) t[i + s] = a[s];
                        return t || r(a);
                    };
                },
                function (e, t) {
                    var n =
                        ("undefined" != typeof crypto && crypto.getRandomValues && crypto.getRandomValues.bind(crypto)) ||
                        ("undefined" != typeof msCrypto && "function" == typeof window.msCrypto.getRandomValues && msCrypto.getRandomValues.bind(msCrypto));
                    if (n) {
                        var o = new Uint8Array(16);
                        e.exports = function () {
                            return n(o), o;
                        };
                    } else {
                        var r = new Array(16);
                        e.exports = function () {
                            for (var e, t = 0; t < 16; t++) 0 == (3 & t) && (e = 4294967296 * Math.random()), (r[t] = (e >>> ((3 & t) << 3)) & 255);
                            return r;
                        };
                    }
                },
                function (e, t) {
                    for (var n = [], o = 0; o < 256; ++o) n[o] = (o + 256).toString(16).substr(1);
                    e.exports = function (e, t) {
                        var o = t || 0,
                            r = n;
                        return [r[e[o++]], r[e[o++]], r[e[o++]], r[e[o++]], "-", r[e[o++]], r[e[o++]], "-", r[e[o++]], r[e[o++]], "-", r[e[o++]], r[e[o++]], "-", r[e[o++]], r[e[o++]], r[e[o++]], r[e[o++]], r[e[o++]], r[e[o++]]].join("");
                    };
                },
                function (e, t, n) {
                    "use strict";
                    Object.defineProperty(t, "__esModule", { value: !0 });
                    var o =
                            "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
                                ? function (e) {
                                      return typeof e;
                                  }
                                : function (e) {
                                      return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e;
                                  },
                        r = s(n(14)),
                        i = s(n(1)),
                        a = s(n(0));
                    function s(e) {
                        return e && e.__esModule ? e : { default: e };
                    }
                    var u = { ready: [] },
                        c = ["url"],
                        l = function () {
                            return !!window.tv4;
                        },
                        d = function (e) {
                            return null === e || (isNaN(e) && !isNaN(Date.parse(e))) ? null : i.default.INVALID_DATE;
                        };
                    t.default = {
                        validateFor: function (e, t) {
                            if (!l()) throw new Error(i.default.ERROR_LOADING_RESOURCE + " Validator is not ready.");
                            if (!t) throw new Error(i.default.INVALID_DATA + " Argument: schema.");
                            if (!/\d+\.\d+/.test(e.version)) throw new Error(i.default.INVALID_VERSION_FORMAT);
                            if (!tv4.validate(e.properties, t)) throw new Error(i.default.INVALID_DATA + " " + e.id + " " + e.version + ". " + tv4.error);
                        },
                        validateArgs: function (e) {
                            var t = Object.prototype.hasOwnProperty;
                            if (!(e && t.call(e, "id") && t.call(e, "version") && t.call(e, "properties"))) throw new Error(i.default.INVALID_FORMAT + " Missing properties: " + JSON.stringify(e));
                            if ("string" != typeof e.id || "string" != typeof e.version || "object" !== o(e.properties)) throw new Error(i.default.INVALID_FORMAT + " Wrong object type: " + JSON.stringify(e));
                            if (
                                c.filter(function (t) {
                                    return e[t] && "string" != typeof e[t];
                                }).length > 0
                            )
                                throw new Error(i.default.INVALID_FORMAT + " Wrong object type: " + JSON.stringify(e));
                            if (e.id.length < 2 || e.version.length < 3) throw new Error(i.default.INVALID_FORMAT + " Invalid property size: " + JSON.stringify(e));
                            var n = Object.assign({}, e);
                            delete n.id, delete n.version, delete n.properties, delete n.contentType;
                            var r = Object.keys(n);
                            if (
                                r.length > 0 &&
                                !r.every(function (e) {
                                    return -1 !== c.indexOf(e);
                                })
                            )
                                throw new Error(i.default.INVALID_FORMAT + " Extra keys aren't allowed: " + JSON.stringify(n));
                        },
                        tv4IsValidData: d,
                        isReady: l,
                        onReady: function (e) {
                            if (l()) return e();
                            if (u.ready.length > a.default.HORIZON_CALLBACK_STACK_LIMIT) throw new Error(i.default.LIMIT_EXCEEDED + " Validator callback stack.");
                            return u.ready.unshift(e);
                        },
                        load: function () {
                            if (!r.default.isDefined("tv4")) {
                                var e = (a.default.USE_HTTPS ? "https://" : "http://") + a.default.SCHEMA_VALIDATOR_SCRIPT_URL;
                                (0, r.default)([e], "tv4", {
                                    async: !0,
                                    numRetries: a.default.SCHEMA_VALIDATOR_SCRIPT_MAX_RETRIES,
                                    success: function () {
                                        tv4.addFormat("date-time", d),
                                            u.ready.forEach(function (e) {
                                                return e();
                                            });
                                    },
                                    error: function (e) {
                                        throw new Error(i.default.SCHEMA_VALIDATOR_ERROR_LOADING + " " + e);
                                    },
                                });
                            }
                        },
                    };
                },
                function (e, t, n) {
                    var o, r, i;
                    (r = []),
                        void 0 ===
                            (i =
                                "function" ==
                                typeof (o = function () {
                                    var e = function () {},
                                        t = {},
                                        n = {},
                                        o = {};
                                    function r(e, t) {
                                        if (e) {
                                            var r = o[e];
                                            if (((n[e] = t), r)) for (; r.length; ) r[0](e, t), r.splice(0, 1);
                                        }
                                    }
                                    function i(t, n) {
                                        t.call && (t = { success: t }), n.length ? (t.error || e)(n) : (t.success || e)(t);
                                    }
                                    function a(t, n, o, r) {
                                        var i,
                                            s,
                                            u = document,
                                            c = o.async,
                                            l = (o.numRetries || 0) + 1,
                                            d = o.before || e,
                                            f = t.replace(/^(css|img)!/, "");
                                        (r = r || 0),
                                            /(^css!|\.css$)/.test(t)
                                                ? (((s = u.createElement("link")).rel = "stylesheet"), (s.href = f), (i = "hideFocus" in s) && s.relList && ((i = 0), (s.rel = "preload"), (s.as = "style")))
                                                : /(^img!|\.(png|gif|jpygame|svg)$)/.test(t)
                                                ? ((s = u.createElement("img")).src = f)
                                                : (((s = u.createElement("script")).src = t), (s.async = void 0 === c || c)),
                                            (s.onload = s.onerror = s.onbeforeload = function (e) {
                                                var u = e.type[0];
                                                if (i)
                                                    try {
                                                        s.sheet.cssText.length || (u = "e");
                                                    } catch (e) {
                                                        18 != e.code && (u = "e");
                                                    }
                                                if ("e" == u) {
                                                    if ((r += 1) < l) return a(t, n, o, r);
                                                } else if ("preload" == s.rel && "style" == s.as) return (s.rel = "stylesheet");
                                                n(t, u, e.defaultPrevented);
                                            }),
                                            !1 !== d(t, s) && u.head.appendChild(s);
                                    }
                                    function s(e, n, o) {
                                        var s, u;
                                        if ((n && n.trim && (s = n), (u = (s ? o : n) || {}), s)) {
                                            if (s in t) throw "LoadJS";
                                            t[s] = !0;
                                        }
                                        function c(t, n) {
                                            !(function (e, t, n) {
                                                var o,
                                                    r,
                                                    i = (e = e.push ? e : [e]).length,
                                                    s = i,
                                                    u = [];
                                                for (
                                                    o = function (e, n, o) {
                                                        if (("e" == n && u.push(e), "b" == n)) {
                                                            if (!o) return;
                                                            u.push(e);
                                                        }
                                                        --i || t(u);
                                                    },
                                                        r = 0;
                                                    r < s;
                                                    r++
                                                )
                                                    a(e[r], o, n);
                                            })(
                                                e,
                                                function (e) {
                                                    i(u, e), t && i({ success: t, error: n }, e), r(s, e);
                                                },
                                                u
                                            );
                                        }
                                        if (u.returnPromise) return new Promise(c);
                                        c();
                                    }
                                    return (
                                        (s.ready = function (e, t) {
                                            return (
                                                (function (e, t) {
                                                    var r,
                                                        i,
                                                        a,
                                                        s = [],
                                                        u = (e = e.push ? e : [e]).length,
                                                        c = u;
                                                    for (
                                                        r = function (e, n) {
                                                            n.length && s.push(e), --c || t(s);
                                                        };
                                                        u--;

                                                    )
                                                        (i = e[u]), (a = n[i]) ? r(i, a) : (o[i] = o[i] || []).push(r);
                                                })(e, function (e) {
                                                    i(t, e);
                                                }),
                                                s
                                            );
                                        }),
                                        (s.done = function (e) {
                                            r(e, []);
                                        }),
                                        (s.reset = function () {
                                            (t = {}), (n = {}), (o = {});
                                        }),
                                        (s.isDefined = function (e) {
                                            return e in t;
                                        }),
                                        s
                                    );
                                })
                                    ? o.apply(t, r)
                                    : o) || (e.exports = i);
                },
                function (e, t, n) {
                    "use strict";
                    Object.defineProperty(t, "__esModule", { value: !0 });
                    var o = (function () {
                        function e(e, t) {
                            for (var n = 0; n < t.length; n++) {
                                var o = t[n];
                                (o.enumerable = o.enumerable || !1), (o.configurable = !0), "value" in o && (o.writable = !0), Object.defineProperty(e, o.key, o);
                            }
                        }
                        return function (t, n, o) {
                            return n && e(t.prototype, n), o && e(t, o), t;
                        };
                    })();
                    n(16);
                    var r = d(n(2)),
                        i = d(n(17)),
                        a = d(n(0)),
                        s = d(n(1)),
                        u = d(n(22)),
                        c = d(n(24)),
                        l = d(n(25));
                    function d(e) {
                        return e && e.__esModule ? e : { default: e };
                    }
                    var f = function () {
                            return r.default.getResource("bus", {});
                        },
                        h = (function () {
                            function e(t, n, o, r, i) {
                                var d = this;
                                !(function (e, t) {
                                    if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function");
                                })(this, e),
                                    (this.currentTenant = t || s.default.mustBeDefined("tenant")),
                                    (this.instanceID = n || s.default.mustBeDefined("instanceID")),
                                    (this.deviceGroup = o || s.default.mustBeDefined("deviceGroup")),
                                    (this.environment = r || s.default.mustBeDefined("environment")),
                                    (this.queue = new c.default(a.default.EVENTS_BUFFER_SIZE)),
                                    (this.idManager = i),
                                    (this.dispatchNumber = 1),
                                    (this.actionCounter = 0),
                                    new l.default()
                                        .every(a.default.EVENTS_SENDER_INTERVAL)
                                        .call(function () {
                                            d.queue = d.filterQueue();
                                            var e = d.prepareRequest();
                                            d.dispatch(e, a.default.HORIZON_REQUEST_ENCODING) ||
                                                e.actions.forEach(function (e) {
                                                    return d.enqueue(e);
                                                });
                                        })
                                        .call(u.default.applyThrottlingPolicy)
                                        .start();
                            }
                            return (
                                o(e, [
                                    {
                                        key: "setMaxQueueSize",
                                        value: function (e) {
                                            this.queue = c.default.fromArray(this.queue.items, e);
                                        },
                                    },
                                    {
                                        key: "filterQueue",
                                        value: function () {
                                            var e = +Date.now() - a.default.EVENTS_DISCARD_AFTER_MSECS;
                                            return this.queue.filter(function (t) {
                                                return t.actionTs > e;
                                            });
                                        },
                                    },
                                    {
                                        key: "prepareRequest",
                                        value: function () {
                                            var e = this.queue.splice(0, a.default.EVENTS_BULK_SIZE);
                                            return (
                                                (this.actionCounter += e.length),
                                                {
                                                    horizonClientUUID: this.instanceID,
                                                    horizonClientTenant: this.currentTenant,
                                                    horizonClientTs: Date.now(),
                                                    horizonClientType: "js",
                                                    horizonClientDeviceGroup: this.deviceGroup,
                                                    horizonDispatchNumber: this.dispatchNumber,
                                                    horizonActionCounter: this.actionCounter,
                                                    horizonEnvironment: this.environment,
                                                    actions: e,
                                                }
                                            );
                                        },
                                    },
                                    {
                                        key: "isValidRequest",
                                        value: function (e) {
                                            if (!e || (e && !e.actions)) throw new Error(s.default.INVALID_REQUEST);
                                            return e.actions.length > 0;
                                        },
                                    },
                                    {
                                        key: "dispatch",
                                        value: function (e) {
                                            var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : "json",
                                                n = a.default.USE_HTTPS ? "https://" : "http://",
                                                o = this.idManager.getAsKeyValue(),
                                                r = o ? "?" + o : "",
                                                s = "" + n + u.default.applyDestinationPolicy() + "/event/" + this.currentTenant + r,
                                                c = i.default.get(t);
                                            if (!this.isValidRequest(e)) return !1;
                                            this.dispatchNumber += 1;
                                            var l = c(e);
                                            return navigator.sendBeacon(s, l);
                                        },
                                    },
                                    {
                                        key: "enqueue",
                                        value: function (e) {
                                            if (!e.actionTs) throw new Error(s.default.INVALID_TIMESTAMP);
                                            this.queue.push(e);
                                        },
                                    },
                                    {
                                        key: "flush",
                                        value: function () {
                                            for (; this.queue.length > 0; ) {
                                                this.queue = this.filterQueue();
                                                var e = this.prepareRequest();
                                                this.dispatch(e, a.default.HORIZON_REQUEST_ENCODING);
                                            }
                                        },
                                    },
                                    {
                                        key: "length",
                                        get: function () {
                                            return this.queue.length;
                                        },
                                    },
                                ]),
                                e
                            );
                        })();
                    t.default = {
                        getInstance: function (e, t, n, o) {
                            var r = f(),
                                i = e + "-" + t;
                            return r[i] || (r[i] = new h(e, a.default.HORIZON_CLIENT_UUID, t, n, o)), r[i];
                        },
                        reset: function (e, t) {
                            (e && 0 !== e.length) || s.default.mustBeDefined("tenant"), (t && 0 !== t.length) || s.default.mustBeDefined("deviceGroup");
                            var n = e + "-" + t;
                            delete f()[n];
                        },
                        getContextBus: f,
                    };
                },
                function (e, t) {
                    function n(e) {
                        return (n =
                            "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
                                ? function (e) {
                                      return typeof e;
                                  }
                                : function (e) {
                                      return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e;
                                  })(e);
                    }
                    (function () {
                        (function () {
                            return "navigator" in this && "sendBeacon" in this.navigator;
                        }.call(this) ||
                            ("navigator" in this || (this.navigator = {}),
                            (this.navigator.sendBeacon = function (e, t) {
                                var n = this.event && this.event.type,
                                    o = "unload" === n || "beforeunload" === n,
                                    r = "XMLHttpRequest" in this ? new XMLHttpRequest() : new ActiveXObject("Microsoft.XMLHTTP");
                                r.open("POST", e, !o),
                                    (r.withCredentials = !0),
                                    r.setRequestHeader("Accept", "*/*"),
                                    (function (e) {
                                        return "string" == typeof e;
                                    })(t)
                                        ? (r.setRequestHeader("Content-Type", "text/plain;charset=UTF-8"), (r.responseType = "text/plain"))
                                        : (function (e) {
                                              return e instanceof Blob;
                                          })(t) &&
                                          t.type &&
                                          r.setRequestHeader("Content-Type", t.type);
                                try {
                                    r.send(t);
                                } catch (e) {
                                    return !1;
                                }
                                return !0;
                            }.bind(this))));
                    }.call("object" === ("undefined" == typeof window ? "undefined" : n(window)) ? window : {}));
                },
                function (e, t, n) {
                    "use strict";
                    Object.defineProperty(t, "__esModule", { value: !0 });
                    var o = a(n(18)),
                        r = a(n(21)),
                        i = a(n(1));
                    function a(e) {
                        return e && e.__esModule ? e : { default: e };
                    }
                    var s = {
                        base64: function (e) {
                            var t = new FormData();
                            return t.append("data", o.default.encode(r.default.encode(JSON.stringify(e)))), t.append("encoding", "base64"), t;
                        },
                        json: function (e) {
                            return JSON.stringify(e);
                        },
                    };
                    t.default = {
                        get: function (e) {
                            if (!(e in s)) throw new Error(i.default.UNSUPPORTED_ENCODER + " Invalid " + e + " encoder.");
                            return s[e];
                        },
                    };
                },
                function (e, t, n) {
                    (function (e, o) {
                        var r;
                        /*! http://mths.be/base64 v0.1.0 by @mathias | MIT license */ !(function (i) {
                            var a = ("object" == typeof e && e && e.exports, "object" == typeof o && o);
                            a.global !== a && a.window;
                            var s = function (e) {
                                this.message = e;
                            };
                            (s.prototype = new Error()).name = "InvalidCharacterError";
                            var u = function (e) {
                                    throw new s(e);
                                },
                                c = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",
                                l = /[\t\n\f\r ]/g,
                                d = {
                                    encode: function (e) {
                                        (e = String(e)), /[^\0-\xFF]/.test(e) && u("The string to be encoded contains characters outside of the Latin1 range.");
                                        for (var t, n, o, r, i = e.length % 3, a = "", s = -1, l = e.length - i; ++s < l; )
                                            (t = e.charCodeAt(s) << 16),
                                                (n = e.charCodeAt(++s) << 8),
                                                (o = e.charCodeAt(++s)),
                                                (a += c.charAt(((r = t + n + o) >> 18) & 63) + c.charAt((r >> 12) & 63) + c.charAt((r >> 6) & 63) + c.charAt(63 & r));
                                        return (
                                            2 == i
                                                ? ((t = e.charCodeAt(s) << 8), (n = e.charCodeAt(++s)), (a += c.charAt((r = t + n) >> 10) + c.charAt((r >> 4) & 63) + c.charAt((r << 2) & 63) + "="))
                                                : 1 == i && ((r = e.charCodeAt(s)), (a += c.charAt(r >> 2) + c.charAt((r << 4) & 63) + "==")),
                                            a
                                        );
                                    },
                                    decode: function (e) {
                                        var t = (e = String(e).replace(l, "")).length;
                                        t % 4 == 0 && (t = (e = e.replace(/==?$/, "")).length), (t % 4 == 1 || /[^+a-zA-Z0-9/]/.test(e)) && u("Invalid character: the string to be decoded is not correctly encoded.");
                                        for (var n, o, r = 0, i = "", a = -1; ++a < t; ) (o = c.indexOf(e.charAt(a))), (n = r % 4 ? 64 * n + o : o), r++ % 4 && (i += String.fromCharCode(255 & (n >> ((-2 * r) & 6))));
                                        return i;
                                    },
                                    version: "0.1.0",
                                };
                            void 0 ===
                                (r = function () {
                                    return d;
                                }.call(t, n, t, e)) || (e.exports = r);
                        })();
                    }.call(t, n(19)(e), n(20)));
                },
                function (e, t) {
                    e.exports = function (e) {
                        return (
                            e.webpackPolyfill ||
                                ((e.deprecate = function () {}),
                                (e.paths = []),
                                e.children || (e.children = []),
                                Object.defineProperty(e, "loaded", {
                                    enumerable: !0,
                                    get: function () {
                                        return e.l;
                                    },
                                }),
                                Object.defineProperty(e, "id", {
                                    enumerable: !0,
                                    get: function () {
                                        return e.i;
                                    },
                                }),
                                (e.webpackPolyfill = 1)),
                            e
                        );
                    };
                },
                function (e, t) {
                    var n;
                    n = (function () {
                        return this;
                    })();
                    try {
                        n = n || Function("return this")() || (0, eval)("this");
                    } catch (e) {
                        "object" == typeof window && (n = window);
                    }
                    e.exports = n;
                },
                function (e, t, n) {
                    !(function (e) {
                        var t,
                            n,
                            o,
                            r = String.fromCharCode;
                        function i(e) {
                            for (var t, n, o = [], r = 0, i = e.length; r < i; )
                                (t = e.charCodeAt(r++)) >= 55296 && t <= 56319 && r < i ? (56320 == (64512 & (n = e.charCodeAt(r++))) ? o.push(((1023 & t) << 10) + (1023 & n) + 65536) : (o.push(t), r--)) : o.push(t);
                            return o;
                        }
                        function a(e) {
                            if (e >= 55296 && e <= 57343) throw Error("Lone surrogate U+" + e.toString(16).toUpperCase() + " is not a scalar value");
                        }
                        function s(e, t) {
                            return r(((e >> t) & 63) | 128);
                        }
                        function u(e) {
                            if (0 == (4294967168 & e)) return r(e);
                            var t = "";
                            return (
                                0 == (4294965248 & e)
                                    ? (t = r(((e >> 6) & 31) | 192))
                                    : 0 == (4294901760 & e)
                                    ? (a(e), (t = r(((e >> 12) & 15) | 224)), (t += s(e, 6)))
                                    : 0 == (4292870144 & e) && ((t = r(((e >> 18) & 7) | 240)), (t += s(e, 12)), (t += s(e, 6))),
                                t + r((63 & e) | 128)
                            );
                        }
                        function c() {
                            if (o >= n) throw Error("Invalid byte index");
                            var e = 255 & t[o];
                            if ((o++, 128 == (192 & e))) return 63 & e;
                            throw Error("Invalid continuation byte");
                        }
                        function l() {
                            var e, r;
                            if (o > n) throw Error("Invalid byte index");
                            if (o == n) return !1;
                            if (((e = 255 & t[o]), o++, 0 == (128 & e))) return e;
                            if (192 == (224 & e)) {
                                if ((r = ((31 & e) << 6) | c()) >= 128) return r;
                                throw Error("Invalid continuation byte");
                            }
                            if (224 == (240 & e)) {
                                if ((r = ((15 & e) << 12) | (c() << 6) | c()) >= 2048) return a(r), r;
                                throw Error("Invalid continuation byte");
                            }
                            if (240 == (248 & e) && (r = ((7 & e) << 18) | (c() << 12) | (c() << 6) | c()) >= 65536 && r <= 1114111) return r;
                            throw Error("Invalid UTF-8 detected");
                        }
                        (e.version = "3.0.0"),
                            (e.encode = function (e) {
                                for (var t = i(e), n = t.length, o = -1, r = ""; ++o < n; ) r += u(t[o]);
                                return r;
                            }),
                            (e.decode = function (e) {
                                (t = i(e)), (n = t.length), (o = 0);
                                for (var a, s = []; !1 !== (a = l()); ) s.push(a);
                                return (function (e) {
                                    for (var t, n = e.length, o = -1, i = ""; ++o < n; ) (t = e[o]) > 65535 && ((i += r((((t -= 65536) >>> 10) & 1023) | 55296)), (t = 56320 | (1023 & t))), (i += r(t));
                                    return i;
                                })(s);
                            });
                    })(t);
                },
                function (e, t, n) {
                    "use strict";
                    Object.defineProperty(t, "__esModule", { value: !0 });
                    var o = i(n(23)),
                        r = i(n(0));
                    function i(e) {
                        return e && e.__esModule ? e : { default: e };
                    }
                    t.default = {
                        applyThrottlingPolicy: function (e) {
                            var t = r.default.EVENTS_SENDER_MIN_INTERVAL,
                                n = r.default.EVENTS_SENDER_MAX_INTERVAL,
                                i = Number(o.default.get("_hzt.interval")) || r.default.EVENTS_SENDER_INTERVAL;
                            i <= n && i >= t && e.interval !== i && e.reschedule(i);
                        },
                        applyDestinationPolicy: function () {
                            return o.default.get("_hzt.host") || r.default.HORIZON_TRACK_HOST;
                        },
                    };
                },
                function (e, t, n) {
                    var o, r, i;
                    /*!
                     * JavaScript Cookie v2.2.0
                     * https://github.com/js-cookie/js-cookie
                     *
                     * Copyright 2006, 2015 Klaus Hartl & Fagner Brack
                     * Released under the MIT license
                     */ (i = function () {
                        function e() {
                            for (var e = 0, t = {}; e < arguments.length; e++) {
                                var n = arguments[e];
                                for (var o in n) t[o] = n[o];
                            }
                            return t;
                        }
                        return (function t(n) {
                            function o(t, r, i) {
                                var a;
                                if ("undefined" != typeof document) {
                                    if (arguments.length > 1) {
                                        if ("number" == typeof (i = e({ path: "/" }, o.defaults, i)).expires) {
                                            var s = new Date();
                                            s.setMilliseconds(s.getMilliseconds() + 864e5 * i.expires), (i.expires = s);
                                        }
                                        i.expires = i.expires ? i.expires.toUTCString() : "";
                                        try {
                                            (a = JSON.stringify(r)), /^[\{\[]/.test(a) && (r = a);
                                        } catch (e) {}
                                        (r = n.write ? n.write(r, t) : encodeURIComponent(String(r)).replace(/%(23|24|26|2B|3A|3C|3E|3D|2F|3F|40|5B|5D|5E|60|7B|7D|7C)/g, decodeURIComponent)),
                                            (t = (t = (t = encodeURIComponent(String(t))).replace(/%(23|24|26|2B|5E|60|7C)/g, decodeURIComponent)).replace(/[\(\)]/g, escape));
                                        var u = "";
                                        for (var c in i) i[c] && ((u += "; " + c), !0 !== i[c] && (u += "=" + i[c]));
                                        return (document.cookie = t + "=" + r + u);
                                    }
                                    t || (a = {});
                                    for (var l = document.cookie ? document.cookie.split("; ") : [], d = /(%[0-9A-Z]{2})+/g, f = 0; f < l.length; f++) {
                                        var h = l[f].split("="),
                                            p = h.slice(1).join("=");
                                        this.json || '"' !== p.charAt(0) || (p = p.slice(1, -1));
                                        try {
                                            var v = h[0].replace(d, decodeURIComponent);
                                            if (((p = n.read ? n.read(p, v) : n(p, v) || p.replace(d, decodeURIComponent)), this.json))
                                                try {
                                                    p = JSON.parse(p);
                                                } catch (e) {}
                                            if (t === v) {
                                                a = p;
                                                break;
                                            }
                                            t || (a[v] = p);
                                        } catch (e) {}
                                    }
                                    return a;
                                }
                            }
                            return (
                                (o.set = o),
                                (o.get = function (e) {
                                    return o.call(o, e);
                                }),
                                (o.getJSON = function () {
                                    return o.apply({ json: !0 }, [].slice.call(arguments));
                                }),
                                (o.defaults = {}),
                                (o.remove = function (t, n) {
                                    o(t, "", e(n, { expires: -1 }));
                                }),
                                (o.withConverter = t),
                                o
                            );
                        })(function () {});
                    }),
                        void 0 === (r = "function" == typeof (o = i) ? o.call(t, n, t, e) : o) || (e.exports = r),
                        (e.exports = i());
                },
                function (e, t, n) {
                    "use strict";
                    Object.defineProperty(t, "__esModule", { value: !0 });
                    var o = (function () {
                            function e(e, t) {
                                for (var n = 0; n < t.length; n++) {
                                    var o = t[n];
                                    (o.enumerable = o.enumerable || !1), (o.configurable = !0), "value" in o && (o.writable = !0), Object.defineProperty(e, o.key, o);
                                }
                            }
                            return function (t, n, o) {
                                return n && e(t.prototype, n), o && e(t, o), t;
                            };
                        })(),
                        r = (function () {
                            function e() {
                                var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : 100;
                                !(function (e, t) {
                                    if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function");
                                })(this, e),
                                    (this._queue = []),
                                    (this.maxSize = t);
                            }
                            return (
                                o(
                                    e,
                                    [
                                        {
                                            key: "push",
                                            value: function (e) {
                                                this._queue = [e].concat(
                                                    (function (e) {
                                                        if (Array.isArray(e)) {
                                                            for (var t = 0, n = Array(e.length); t < e.length; t++) n[t] = e[t];
                                                            return n;
                                                        }
                                                        return Array.from(e);
                                                    })(this.slice(0, this.maxSize - 1))
                                                );
                                            },
                                        },
                                        {
                                            key: "forEach",
                                            value: function (e) {
                                                return this._queue.forEach(e);
                                            },
                                        },
                                        {
                                            key: "slice",
                                            value: function (e, t) {
                                                return this._queue.slice(e, t);
                                            },
                                        },
                                        {
                                            key: "splice",
                                            value: function (e, t) {
                                                return this._queue.splice(e, t);
                                            },
                                        },
                                        {
                                            key: "clear",
                                            value: function () {
                                                this._queue = [];
                                            },
                                        },
                                        {
                                            key: "filter",
                                            value: function (t) {
                                                return e.fromArray(this._queue.filter(t), this.maxSize);
                                            },
                                        },
                                        {
                                            key: "length",
                                            get: function () {
                                                return this._queue.length;
                                            },
                                        },
                                        {
                                            key: "items",
                                            get: function () {
                                                return JSON.parse(JSON.stringify(this._queue));
                                            },
                                        },
                                    ],
                                    [
                                        {
                                            key: "fromArray",
                                            value: function (t, n) {
                                                var o = new e(n);
                                                return (
                                                    t.forEach(function (e) {
                                                        return o.push(e);
                                                    }),
                                                    o
                                                );
                                            },
                                        },
                                    ]
                                ),
                                e
                            );
                        })();
                    t.default = r;
                },
                function (e, t, n) {
                    "use strict";
                    Object.defineProperty(t, "__esModule", { value: !0 });
                    var o = (function () {
                            function e(e, t) {
                                for (var n = 0; n < t.length; n++) {
                                    var o = t[n];
                                    (o.enumerable = o.enumerable || !1), (o.configurable = !0), "value" in o && (o.writable = !0), Object.defineProperty(e, o.key, o);
                                }
                            }
                            return function (t, n, o) {
                                return n && e(t.prototype, n), o && e(t, o), t;
                            };
                        })(),
                        r = (function () {
                            function e() {
                                !(function (e, t) {
                                    if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function");
                                })(this, e),
                                    (this.interval = 0),
                                    (this.tickIntervalId = 0),
                                    (this.callbacks = []);
                            }
                            return (
                                o(e, [
                                    {
                                        key: "tick",
                                        value: function () {
                                            var e = this;
                                            this.callbacks.forEach(function (t) {
                                                return t(e);
                                            });
                                        },
                                    },
                                    {
                                        key: "start",
                                        value: function () {
                                            return (this.tickIntervalId = setInterval(this.tick.bind(this), this.interval)), this;
                                        },
                                    },
                                    {
                                        key: "stop",
                                        value: function () {
                                            return clearInterval(this.tickIntervalId), (this.tickIntervalId = 0), this;
                                        },
                                    },
                                    {
                                        key: "reschedule",
                                        value: function (e) {
                                            return this.stop().every(e).start();
                                        },
                                    },
                                    {
                                        key: "every",
                                        value: function (e) {
                                            return (this.interval = e), this;
                                        },
                                    },
                                    {
                                        key: "call",
                                        value: function (e) {
                                            return this.callbacks.push(e), this;
                                        },
                                    },
                                    {
                                        key: "isRunning",
                                        get: function () {
                                            return !!this.tickIntervalId;
                                        },
                                    },
                                ]),
                                e
                            );
                        })();
                    t.default = r;
                },
                function (e, t, n) {
                    "use strict";
                    Object.defineProperty(t, "__esModule", { value: !0 });
                    var o = (function () {
                            function e(e, t) {
                                for (var n = 0; n < t.length; n++) {
                                    var o = t[n];
                                    (o.enumerable = o.enumerable || !1), (o.configurable = !0), "value" in o && (o.writable = !0), Object.defineProperty(e, o.key, o);
                                }
                            }
                            return function (t, n, o) {
                                return n && e(t.prototype, n), o && e(t, o), t;
                            };
                        })(),
                        r = c(n(3)),
                        i = c(n(2)),
                        a = c(n(1)),
                        s = c(n(0)),
                        u = c(n(4));
                    function c(e) {
                        return e && e.__esModule ? e : { default: e };
                    }
                    var l = "statusReady",
                        d = "statusNotReady",
                        f = "statusLoading",
                        h = "statusScheduled",
                        p = "statusError",
                        v = function () {
                            return i.default.getResource("schemas", { data: {} });
                        },
                        y = (function () {
                            function e(t) {
                                !(function (e, t) {
                                    if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function");
                                })(this, e),
                                    (this.url = t),
                                    (this.state = d),
                                    (this.callbacks = { onReady: [], onError: [], onRetry: [], onLoad: [] });
                            }
                            return (
                                o(e, [
                                    {
                                        key: "get",
                                        value: function (e, t) {
                                            var n = e + "-" + t;
                                            if (!this.isReady()) throw new Error("" + a.default.COMPONENT_NOT_READY);
                                            var o = v().data[n];
                                            if (!o) throw new Error(a.default.UNSUPPORTED_TYPE + ": " + n);
                                            return o;
                                        },
                                    },
                                    {
                                        key: "isReady",
                                        value: function () {
                                            return this.state === l;
                                        },
                                    },
                                    {
                                        key: "retry",
                                        value: function () {
                                            var e = this;
                                            (this.state = h),
                                                this.callbacks.onRetry.forEach(function (e) {
                                                    return e();
                                                }),
                                                setTimeout(function () {
                                                    (e.state = d), e.load();
                                                }, s.default.SCHEMA_LOAD_COLLECTION_RETRY_AFTER_MSECS);
                                        },
                                    },
                                    {
                                        key: "onLoad",
                                        value: function (e) {
                                            this.callbacks.onLoad.push(e);
                                        },
                                    },
                                    {
                                        key: "onRetry",
                                        value: function (e) {
                                            this.callbacks.onRetry.push(e);
                                        },
                                    },
                                    {
                                        key: "onReady",
                                        value: function (e) {
                                            if (this.state === l) return e(v().data);
                                            if (this.callbacks.onReady.length > s.default.HORIZON_CALLBACK_STACK_LIMIT) throw new Error(a.default.LIMIT_EXCEEDED + " Schemas callback stack.");
                                            return this.callbacks.onReady.push(e);
                                        },
                                    },
                                    {
                                        key: "onError",
                                        value: function (e) {
                                            this.state === p ? e() : this.callbacks.onError.push(e);
                                        },
                                    },
                                    {
                                        key: "load",
                                        value: function () {
                                            var e = this,
                                                t = v();
                                            if (this.state === d) {
                                                (this.state = f),
                                                    this.callbacks.onLoad.forEach(function (e) {
                                                        return e();
                                                    });
                                                var n = s.default.USE_HTTPS ? "https://" : "http://";
                                                u.default.request(
                                                    "GET",
                                                    "" + n + this.url,
                                                    function (n) {
                                                        (t.data = Object.assign(t.data || {}, n)),
                                                            (e.state = l),
                                                            e.callbacks.onReady.forEach(function (e) {
                                                                return r.default.execAsync(e, t.data);
                                                            });
                                                    },
                                                    function (t) {
                                                        (e.state = p),
                                                            e.callbacks.onError.forEach(function (e) {
                                                                return r.default.execAsync(e, t);
                                                            }),
                                                            e.retry();
                                                    }
                                                );
                                            }
                                        },
                                    },
                                ]),
                                e
                            );
                        })();
                    t.default = {
                        getInstance: function (e) {
                            var t = v();
                            return t.provider || (t.provider = new y(e || s.default.HORIZON_SCHEMAS_HOST + "/schemas")), t.provider;
                        },
                        getContextSchemas: v,
                    };
                },
                function (e, t, n) {
                    "use strict";
                    Object.defineProperty(t, "__esModule", { value: !0 });
                    var o = function (e) {
                            return window.cdaaas && window.cdaaas.SETTINGS ? window.cdaaas.SETTINGS[e] : null;
                        },
                        r = function (e) {
                            return window.utag_data ? window.utag_data[e] : null;
                        };
                    t.default = {
                        getTenant: function () {
                            return o("SITE_ID") || r("ut.profile") || "unknown";
                        },
                        getDeviceGroup: function () {
                            return o("MOBILE_GROUP") || r("platform") || "unknown";
                        },
                    };
                },
            ]));
    },
    function (e, t, n) {
        "use strict";
        Object.defineProperty(t, "__esModule", { value: !0 });
        t.default = class {
            constructor(e) {
                this.bannerAnimations = e;
            }
            animateIn(e) {
                this.bannerAnimations.animated && (this.setElementAnimated(e), this.bannerAnimations.animationIn && this.bannerAnimations.animationIn(e));
            }
            animateOut(e) {
                let t = Promise.resolve("");
                if (this.bannerAnimations.animated) {
                    this.setElementAnimated(e), parseFloat(window.getComputedStyle(e, null).getPropertyValue("animation-duration") || "0") > 0 && (t = this.animationPromise(e));
                }
                return t;
            }
            setElementAnimated(e) {
                e.classList.add("cookie-banner-lgpd-animated");
            }
            animationPromise(e) {
                return new Promise((t) => {
                    ["webkitAnimationEnd", "mozAnimationEnd", "MSAnimationEnd", "oAnimationEnd", "animationend"].forEach((n) => {
                        e.addEventListener(n, () => {
                            this.bannerAnimations.animationOut && this.bannerAnimations.animationOut(e, n), t(n);
                        });
                    });
                });
            }
        };
    },
    function (e, t, n) {
        "use strict";
        Object.defineProperty(t, "__esModule", { value: !0 });
        const o = n(0);
        
        t.default = class {
            setVersionCookie(e) {
                o.default.setCookie({ cookieName: "lgpd-paulus-version"+use_lgpd, value: version_lgpd, domain: e });
            }
            isAcceptedCookieVersionBefore() {
                const [e] = o.default.getCookie("lgpd-paulus-version"+use_lgpd);
                return this.getLastVersionDigit(e) < this.getLastVersionDigit(version_lgpd);
            }
            getLastVersionDigit(e) {
                const t = (e || "0").split("."),
                    n = Number(t[t.length - 1]);
                return isNaN(n) ? 0 : n;
            }
        };        
    },
    function (e, t, n) {
        "use strict";
        Object.defineProperty(t, "__esModule", { value: !0 });
        t.default = class {
            constructor(e) {
                this.domOptions = e;
            }
            getCookieBanner() {
                
                return document.getElementById("cookie-banner-lgpd");
            }
            getBannerRoot() {
                const e = document.createElement("div");
                return e.setAttribute("id", "cookie-banner-lgpd"), e.setAttribute("class", "cookie-banner-lgpd-hidden"), e.setAttribute("style", "display:none"), e;
            }
            getBannerContainer() {
                const e = document.createElement("div");
                return e.setAttribute("class", "cookie-banner-lgpd-container"), e;
            }
            getBannerTextBox() {
                const e = document.createElement("div");
                return e.setAttribute("class", "cookie-banner-lgpd_text-box"),e.setAttribute("id", "cookie-banner-lgpd_text-box"), e;
            }
            getBannerText() {
                const e = document.createElement("span");
                return (
                    e.setAttribute("class", "cookie-banner-lgpd_text"),
                    (e.innerHTML =
                        text_banner),
                    e
                );
            }
            getBannerPrivacyLink() {
                const e = document.createElement("a");
                return (
                    e.setAttribute("class", "cookie-banner-lgpd-link cookie-banner-lgpd_privacy-link"),
                    e.setAttribute("target", "_blank"),
                    e.setAttribute("style", this.generateLinkStyle()),
                    e.setAttribute("href", this.domOptions.customPrivacyLinkUrl || link_policy_privacy),
                    (e.innerText = "Polí­tica de Privacidade"),
                    e
                );
            }
            getBannerPrivacyPortalLink() {
                const e = document.createElement("a");
                return (
                    e.setAttribute("class", "cookie-banner-lgpd-link cookie-banner-lgpd_privacy-portal-link"),
                    e.setAttribute("target", "_blank"),
                    e.setAttribute("style", this.generateLinkStyle()),
                    e.setAttribute("href", this.domOptions.customPrivacyPortalLinkUrl || link_portal_privacy),
                    (e.innerText = ""),
                    e
                );
            }
            getMiddleBannerText() {
                const e = document.createElement("span");
                //return (e.innerText = ". Conheça nosso "), e;
                return (e.innerText = "."), e;
            }
            getEndBannerText() {
                const e = document.createElement("span");
                //return (e.innerText = " e veja a nossa nova Polí­tica."), e;
                return (e.innerText = ""), e;
            }
            getBannerButtonBox() {
                const e = document.createElement("div");
                return e.setAttribute("class", "cookie-banner-lgpd_button-box"),e.setAttribute("id", "cookie-banner-lgpd_button-box"), e;
            }
            getBannerButton() {
                const e = document.createElement("button");
                return e.setAttribute("class", "cookie-banner-lgpd_accept-button"), e.setAttribute("id", "cookie-banner-lgpd_accept-button"), e.setAttribute("style", this.generateButtonStyle()), (e.innerText = text_button), e;
            }
            createCookieBanner() {
                
                const e = this.getBannerRoot(),
                    t = this.getBannerContainer(),
                    n = this.getBannerButtonBox(),
                    o = this.getBannerButton(),
                    r = this.assembleBannerText();
                return n.appendChild(o), t.appendChild(r), t.appendChild(n), e.appendChild(t), e;
            }
            assembleBannerText() {
                const e = this.getBannerText(),
                    t = this.getBannerPrivacyLink(),
                    n = this.getBannerPrivacyPortalLink(),
                    o = this.getMiddleBannerText(),
                    r = this.getEndBannerText(),
                    i = this.getBannerTextBox();
                return e.appendChild(t), e.appendChild(o), e.appendChild(n), e.appendChild(r), i.appendChild(e), i;
            }
            generateLinkStyle() {
                return "" + (this.domOptions.style.linkColor ? "color:" + this.domOptions.style.linkColor : "");
            }
            generateButtonStyle() {
                return "" + (this.domOptions.style.buttonColor ? "background-color:" + this.domOptions.style.buttonColor : "");
            }
            validateCookieBannerDOM(e) {
                [
                    { isValid: () => e && "cookie-banner-lgpd" === e.id, errorMessage: "DOM root do cookie banner não pode ser nulo ou undefined e deve conter o id cookie-banner-lgpd" },
                    {
                        isValid() {
                            const t = e.querySelector(".cookie-banner-lgpd_accept-button");
                            return t && t.innerHTML.includes(text_button);
                        },
                        errorMessage: "DOM do cookie banner precisa conter um botão com a classe .cookie-banner-lgpd_accept-button e com o texto "+text_button+"",
                    },
                    {
                        isValid() {
                            const t = e.querySelector(".cookie-banner-lgpd_text");
                            return (
                                t &&
                                t.innerHTML.includes(
                                    text_banner
                                ) &&
                                t.innerText.includes("Polí­tica de Privacidade") &&
                                //t.innerText.includes(". Conheça nosso") &&
                                t.innerText.includes(".") &&
                                //t.innerText.includes("e veja a nossa nova Polí­tica.")
                                t.innerText.includes("")
                            );
                        },
                        errorMessage:
                            "DOM do cookie banner precisa conter o texto com a classe .cookie-banner-lgpd_text e o conteúdo: "+text_banner+"",
                    },
                    {
                        isValid() {
                            const t = e.querySelector(".cookie-banner-lgpd_text").querySelector(".cookie-banner-lgpd_privacy-link");
                            return Boolean(t);
                        },
                        errorMessage: "DOM de texto do cookie banner precisa conter o link para a polí­tica de privacidade",
                    },
                ].forEach((e) => {
                    if (!e.isValid()) throw "COOKIE_BANNER_ERROR: " + e.errorMessage;
                });
            }
            injectCookieInPage() {
                let e;
                return (
                    (e = this.domOptions.lifecycle.createCookieBanner
                        ? this.domOptions.lifecycle.createCookieBanner({ cookieBannerRoot: this.getBannerRoot(), cookieBannerText: this.assembleBannerText(), cookieBannerButton: this.getBannerButton() })
                        : this.createCookieBanner()),
                    this.validateCookieBannerDOM(e),
                    document.body.appendChild(e),
                    e
                );
            }
        };
    },
    function (e, t, n) {
        "use strict";
        Object.defineProperty(t, "__esModule", { value: !0 }),
            (t.bannerDefaultOptions = {
                style: { buttonColor: "#E3001B", linkColor: "#E3001B" },
                animation: { animationIn: void 0, animationOut: void 0, animated: !0 },
                lifecycle: { onCookieBannerShow: void 0, onCookieBannerHide: void 0, onConsentAccepted: void 0, createCookieBanner: void 0 },
                customPrivacyLinkUrl: void 0,
                customPrivacyPortalLinkUrl: void 0,
                tenant: void 0,
            });
        class o {
            static merge(e = {}) {
                return {
                    animation: { ...t.bannerDefaultOptions.animation, ...e.animation },
                    style: { ...t.bannerDefaultOptions.style, ...e.style },
                    lifecycle: { ...t.bannerDefaultOptions.lifecycle, ...e.lifecycle },
                    customPrivacyLinkUrl: e.customPrivacyLinkUrl || t.bannerDefaultOptions.customPrivacyLinkUrl,
                    customPrivacyPortalLinkUrl: e.customPrivacyPortalLinkUrl || t.bannerDefaultOptions.customPrivacyPortalLinkUrl,
                    tenant: e.tenant || t.bannerDefaultOptions.tenant,
                };
            }
        }
        (t.Options = o), (t.default = { bannerDefaultOptions: t.bannerDefaultOptions, Options: o });
    },
    function (e, t) {},
    ,
    function (e, t) {},
]).default;

