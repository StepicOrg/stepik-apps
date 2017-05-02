import {$} from "../../imports/js/jquery";

let pluses = /\+/g;

function encode(s) {
    return cookie.raw ? s : encodeURIComponent(s);
}

function decode(s) {
    return cookie.raw ? s : decodeURIComponent(s);
}

function stringifyCookieValue(value) {
    return encode(cookie.json ? JSON.stringify(value) : String(value));
}

function parseCookieValue(s) {
    if (s.indexOf('"') === 0) {
        // This is a quoted cookie as according to RFC2068, unescape...
        s = s.slice(1, -1).replace(/\\"/g, '"').replace(/\\\\/g, '\\');
    }

    try {
        // Replace server-side written pluses with spaces.
        // If we can't decode the cookie, ignore it, it's unusable.
        // If we can't parse the cookie, ignore it, it's unusable.
        s = decodeURIComponent(s.replace(pluses, ' '));
        return cookie.json ? JSON.parse(s) : s;
    } catch (e) {
    }
}

function read(s, converter) {
    let value = cookie.raw ? s : parseCookieValue(s);
    return $.isFunction(converter) ? converter(value) : value;
}

export let cookie = $.cookie = function (key, value, options) {

    // Write

    if (value !== undefined && !$.isFunction(value)) {
        options = $.extend({}, cookie.defaults, options);

        if (typeof options.expires === 'number') {
            let days = options.expires, t = options.expires = new Date();
            t.setTime(+t + days * 864e+5);
        }

        return (document.cookie = [
            encode(key), '=', stringifyCookieValue(value),
            options['expires'] ? '; expires=' + options.expires.toUTCString() : '', // use expires attribute, max-age is not supported by IE
            options['path'] ? '; path=' + options.path : '',
            options['domain'] ? '; domain=' + options.domain : '',
            options['secure'] ? '; secure' : ''
        ].join(''));
    }

    // Read

    let result = key ? undefined : {};

    // To prevent the for loop in the first place assign an empty array
    // in case there are no cookies at all. Also prevents odd result when
    // calling $.cookie().
    let cookies = document.cookie ? document.cookie.split('; ') : [];

    for (let i = 0, l = cookies.length; i < l; i++) {
        let parts = cookies[i].split('=');
        let name = decode(parts.shift());
        let cookie = parts.join('=');

        if (key && key === name) {
            // If second argument (value) is a function it's a converter...
            result = read(cookie, value);
            break;
        }

        // Prevent storing a cookie that we couldn't decode.
        if (!key && (cookie = read(cookie)) !== undefined) {
            result[name] = cookie;
        }
    }

    return result;
};

cookie.defaults = {};

$.removeCookie = function (key, options) {
    if ($.cookie(key) === undefined) {
        return false;
    }

    // Must not alter options, thus extending a fresh object...
    $.cookie(key, '', $.extend({}, options, {expires: -1}));
    return !$.cookie(key);
};