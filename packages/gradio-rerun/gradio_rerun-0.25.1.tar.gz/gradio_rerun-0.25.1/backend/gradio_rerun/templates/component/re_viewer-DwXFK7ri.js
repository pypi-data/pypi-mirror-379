function Ne() {
  const M = {};
  typeof document < "u" && document.currentScript !== null && new URL(document.currentScript.src, location.href).toString();
  let b;
  function g(n) {
    return n == null;
  }
  function l(n) {
    const e = b.__externref_table_alloc();
    return b.__wbindgen_export_1.set(e, n), e;
  }
  const j = typeof TextDecoder < "u" ? new TextDecoder("utf-8", { ignoreBOM: !0, fatal: !0 }) : { decode: () => {
    throw Error("TextDecoder not available");
  } };
  typeof TextDecoder < "u" && j.decode();
  let T = null;
  function D() {
    return (T === null || T.byteLength === 0) && (T = new Uint8Array(b.memory.buffer)), T;
  }
  function u(n, e) {
    return n = n >>> 0, j.decode(D().subarray(n, n + e));
  }
  function a(n, e) {
    try {
      return n.apply(this, e);
    } catch (t) {
      const _ = l(t);
      b.__wbindgen_exn_store(_);
    }
  }
  let P = null;
  function ne() {
    return (P === null || P.byteLength === 0) && (P = new Float32Array(b.memory.buffer)), P;
  }
  function h(n, e) {
    return n = n >>> 0, ne().subarray(n / 4, n / 4 + e);
  }
  let B = null;
  function _e() {
    return (B === null || B.byteLength === 0) && (B = new Int32Array(b.memory.buffer)), B;
  }
  function I(n, e) {
    return n = n >>> 0, _e().subarray(n / 4, n / 4 + e);
  }
  let F = null;
  function re() {
    return (F === null || F.byteLength === 0) && (F = new Uint32Array(b.memory.buffer)), F;
  }
  function R(n, e) {
    return n = n >>> 0, re().subarray(n / 4, n / 4 + e);
  }
  let d = 0;
  const E = typeof TextEncoder < "u" ? new TextEncoder("utf-8") : { encode: () => {
    throw Error("TextEncoder not available");
  } }, ce = typeof E.encodeInto == "function" ? function(n, e) {
    return E.encodeInto(n, e);
  } : function(n, e) {
    const t = E.encode(n);
    return e.set(t), {
      read: n.length,
      written: t.length
    };
  };
  function m(n, e, t) {
    if (t === void 0) {
      const f = E.encode(n), i = e(f.length, 1) >>> 0;
      return D().subarray(i, i + f.length).set(f), d = f.length, i;
    }
    let _ = n.length, r = e(_, 1) >>> 0;
    const c = D();
    let o = 0;
    for (; o < _; o++) {
      const f = n.charCodeAt(o);
      if (f > 127)
        break;
      c[r + o] = f;
    }
    if (o !== _) {
      o !== 0 && (n = n.slice(o)), r = t(r, _, _ = o + n.length * 3, 1) >>> 0;
      const f = D().subarray(r + o, r + _), i = ce(n, f);
      o += i.written, r = t(r, _, o, 1) >>> 0;
    }
    return d = o, r;
  }
  let v = null;
  function w() {
    return (v === null || v.buffer.detached === !0 || v.buffer.detached === void 0 && v.buffer !== b.memory.buffer) && (v = new DataView(b.memory.buffer)), v;
  }
  function H(n, e) {
    return n = n >>> 0, D().subarray(n / 1, n / 1 + e);
  }
  const K = typeof FinalizationRegistry > "u" ? { register: () => {
  }, unregister: () => {
  } } : new FinalizationRegistry((n) => {
    b == null || b.__wbindgen_export_6.get(n.dtor)(n.a, n.b);
  });
  function S(n, e, t, _) {
    const r = { a: n, b: e, cnt: 1, dtor: t }, c = (...o) => {
      r.cnt++;
      const f = r.a;
      r.a = 0;
      try {
        return _(f, r.b, ...o);
      } finally {
        --r.cnt === 0 ? (b.__wbindgen_export_6.get(r.dtor)(f, r.b), K.unregister(r)) : r.a = f;
      }
    };
    return c.original = r, K.register(c, r, r), c;
  }
  function C(n) {
    const e = typeof n;
    if (e == "number" || e == "boolean" || n == null)
      return `${n}`;
    if (e == "string")
      return `"${n}"`;
    if (e == "symbol") {
      const r = n.description;
      return r == null ? "Symbol" : `Symbol(${r})`;
    }
    if (e == "function") {
      const r = n.name;
      return typeof r == "string" && r.length > 0 ? `Function(${r})` : "Function";
    }
    if (Array.isArray(n)) {
      const r = n.length;
      let c = "[";
      r > 0 && (c += C(n[0]));
      for (let o = 1; o < r; o++)
        c += ", " + C(n[o]);
      return c += "]", c;
    }
    const t = /\[object ([^\]]+)\]/.exec(toString.call(n));
    let _;
    if (t && t.length > 1)
      _ = t[1];
    else
      return toString.call(n);
    if (_ == "Object")
      try {
        return "Object(" + JSON.stringify(n) + ")";
      } catch {
        return "Object";
      }
    return n instanceof Error ? `${n.name}: ${n.message}
${n.stack}` : _;
  }
  function k(n) {
    const e = b.__wbindgen_export_1.get(n);
    return b.__externref_table_dealloc(n), e;
  }
  function N(n, e) {
    const t = e(n.length * 1, 1) >>> 0;
    return D().set(n, t / 1), d = n.length, t;
  }
  function be(n, e, t) {
    const _ = b.closure12_externref_shim_multivalue_shim(n, e, t);
    if (_[1])
      throw k(_[0]);
  }
  function oe(n, e) {
    b._dyn_core__ops__function__FnMut_____Output___R_as_wasm_bindgen__closure__WasmClosure___describe__invoke__h80698ba6f867db8e(n, e);
  }
  function ae(n, e) {
    b._dyn_core__ops__function__FnMut_____Output___R_as_wasm_bindgen__closure__WasmClosure___describe__invoke__h62243419debf4837(n, e);
  }
  function Q(n, e, t) {
    b.closure18200_externref_shim(n, e, t);
  }
  function fe(n, e) {
    const t = b._dyn_core__ops__function__FnMut_____Output___R_as_wasm_bindgen__closure__WasmClosure___describe__invoke__h765ec94171c42581_multivalue_shim(n, e);
    if (t[1])
      throw k(t[0]);
  }
  function ue(n, e, t) {
    b.closure18725_externref_shim(n, e, t);
  }
  function X(n, e, t) {
    b.closure22217_externref_shim(n, e, t);
  }
  function ie(n, e, t) {
    b.closure22812_externref_shim(n, e, t);
  }
  function ge(n, e, t, _) {
    b.closure26656_externref_shim(n, e, t, _);
  }
  const we = ["key", "delta"], L = ["clamp-to-edge", "repeat", "mirror-repeat"], Y = ["zero", "one", "src", "one-minus-src", "src-alpha", "one-minus-src-alpha", "dst", "one-minus-dst", "dst-alpha", "one-minus-dst-alpha", "src-alpha-saturated", "constant", "one-minus-constant", "src1", "one-minus-src1", "src1-alpha", "one-minus-src1-alpha"], se = ["add", "subtract", "reverse-subtract", "min", "max"], de = ["uniform", "storage", "read-only-storage"], le = ["opaque", "premultiplied"], O = ["never", "less", "equal", "less-equal", "greater", "not-equal", "greater-equal", "always"], me = ["none", "front", "back"], pe = ["validation", "out-of-memory", "internal"], $ = ["nearest", "linear"], ye = ["ccw", "cw"], z = ["uint16", "uint32"], G = ["load", "clear"], he = ["nearest", "linear"], xe = ["low-power", "high-performance"], Se = ["point-list", "line-list", "line-strip", "triangle-list", "triangle-strip"], ve = ["filtering", "non-filtering", "comparison"], W = ["keep", "zero", "replace", "invert", "increment-clamp", "decrement-clamp", "increment-wrap", "decrement-wrap"], Ie = ["write-only", "read-only", "read-write"], V = ["store", "discard"], J = ["all", "stencil-only", "depth-only"], Ae = ["1d", "2d", "3d"], A = ["r8unorm", "r8snorm", "r8uint", "r8sint", "r16uint", "r16sint", "r16float", "rg8unorm", "rg8snorm", "rg8uint", "rg8sint", "r32uint", "r32sint", "r32float", "rg16uint", "rg16sint", "rg16float", "rgba8unorm", "rgba8unorm-srgb", "rgba8snorm", "rgba8uint", "rgba8sint", "bgra8unorm", "bgra8unorm-srgb", "rgb9e5ufloat", "rgb10a2uint", "rgb10a2unorm", "rg11b10ufloat", "rg32uint", "rg32sint", "rg32float", "rgba16uint", "rgba16sint", "rgba16float", "rgba32uint", "rgba32sint", "rgba32float", "stencil8", "depth16unorm", "depth24plus", "depth24plus-stencil8", "depth32float", "depth32float-stencil8", "bc1-rgba-unorm", "bc1-rgba-unorm-srgb", "bc2-rgba-unorm", "bc2-rgba-unorm-srgb", "bc3-rgba-unorm", "bc3-rgba-unorm-srgb", "bc4-r-unorm", "bc4-r-snorm", "bc5-rg-unorm", "bc5-rg-snorm", "bc6h-rgb-ufloat", "bc6h-rgb-float", "bc7-rgba-unorm", "bc7-rgba-unorm-srgb", "etc2-rgb8unorm", "etc2-rgb8unorm-srgb", "etc2-rgb8a1unorm", "etc2-rgb8a1unorm-srgb", "etc2-rgba8unorm", "etc2-rgba8unorm-srgb", "eac-r11unorm", "eac-r11snorm", "eac-rg11unorm", "eac-rg11snorm", "astc-4x4-unorm", "astc-4x4-unorm-srgb", "astc-5x4-unorm", "astc-5x4-unorm-srgb", "astc-5x5-unorm", "astc-5x5-unorm-srgb", "astc-6x5-unorm", "astc-6x5-unorm-srgb", "astc-6x6-unorm", "astc-6x6-unorm-srgb", "astc-8x5-unorm", "astc-8x5-unorm-srgb", "astc-8x6-unorm", "astc-8x6-unorm-srgb", "astc-8x8-unorm", "astc-8x8-unorm-srgb", "astc-10x5-unorm", "astc-10x5-unorm-srgb", "astc-10x6-unorm", "astc-10x6-unorm-srgb", "astc-10x8-unorm", "astc-10x8-unorm-srgb", "astc-10x10-unorm", "astc-10x10-unorm-srgb", "astc-12x10-unorm", "astc-12x10-unorm-srgb", "astc-12x12-unorm", "astc-12x12-unorm-srgb"], Te = ["float", "unfilterable-float", "depth", "sint", "uint"], q = ["1d", "2d", "2d-array", "cube", "cube-array", "3d"], De = ["uint8", "uint8x2", "uint8x4", "sint8", "sint8x2", "sint8x4", "unorm8", "unorm8x2", "unorm8x4", "snorm8", "snorm8x2", "snorm8x4", "uint16", "uint16x2", "uint16x4", "sint16", "sint16x2", "sint16x4", "unorm16", "unorm16x2", "unorm16x4", "snorm16", "snorm16x2", "snorm16x4", "float16", "float16x2", "float16x4", "float32", "float32x2", "float32x3", "float32x4", "uint32", "uint32x2", "uint32x3", "uint32x4", "sint32", "sint32x2", "sint32x3", "sint32x4", "unorm10-10-10-2", "unorm8x4-bgra"], Pe = ["vertex", "instance"], Be = ["no-preference", "prefer-hardware", "prefer-software"], Fe = ["bytes"], Me = ["", "no-referrer", "no-referrer-when-downgrade", "origin", "origin-when-cross-origin", "unsafe-url", "same-origin", "strict-origin", "strict-origin-when-cross-origin"], Re = ["default", "no-store", "reload", "no-cache", "force-cache", "only-if-cached"], Ee = ["omit", "same-origin", "include"], ke = ["same-origin", "no-cors", "cors", "navigate"], Ce = ["follow", "error", "manual"], Le = ["border-box", "content-box", "device-pixel-content-box"], Oe = typeof FinalizationRegistry > "u" ? { register: () => {
  }, unregister: () => {
  } } : new FinalizationRegistry((n) => b.__wbg_intounderlyingbytesource_free(n >>> 0, 1));
  class ze {
    __destroy_into_raw() {
      const e = this.__wbg_ptr;
      return this.__wbg_ptr = 0, Oe.unregister(this), e;
    }
    free() {
      const e = this.__destroy_into_raw();
      b.__wbg_intounderlyingbytesource_free(e, 0);
    }
    /**
     * @returns {ReadableStreamType}
     */
    get type() {
      const e = b.intounderlyingbytesource_type(this.__wbg_ptr);
      return Fe[e];
    }
    /**
     * @returns {number}
     */
    get autoAllocateChunkSize() {
      return b.intounderlyingbytesource_autoAllocateChunkSize(this.__wbg_ptr) >>> 0;
    }
    /**
     * @param {ReadableByteStreamController} controller
     */
    start(e) {
      b.intounderlyingbytesource_start(this.__wbg_ptr, e);
    }
    /**
     * @param {ReadableByteStreamController} controller
     * @returns {Promise<any>}
     */
    pull(e) {
      return b.intounderlyingbytesource_pull(this.__wbg_ptr, e);
    }
    cancel() {
      const e = this.__destroy_into_raw();
      b.intounderlyingbytesource_cancel(e);
    }
  }
  M.IntoUnderlyingByteSource = ze;
  const Ge = typeof FinalizationRegistry > "u" ? { register: () => {
  }, unregister: () => {
  } } : new FinalizationRegistry((n) => b.__wbg_intounderlyingsink_free(n >>> 0, 1));
  class We {
    __destroy_into_raw() {
      const e = this.__wbg_ptr;
      return this.__wbg_ptr = 0, Ge.unregister(this), e;
    }
    free() {
      const e = this.__destroy_into_raw();
      b.__wbg_intounderlyingsink_free(e, 0);
    }
    /**
     * @param {any} chunk
     * @returns {Promise<any>}
     */
    write(e) {
      return b.intounderlyingsink_write(this.__wbg_ptr, e);
    }
    /**
     * @returns {Promise<any>}
     */
    close() {
      const e = this.__destroy_into_raw();
      return b.intounderlyingsink_close(e);
    }
    /**
     * @param {any} reason
     * @returns {Promise<any>}
     */
    abort(e) {
      const t = this.__destroy_into_raw();
      return b.intounderlyingsink_abort(t, e);
    }
  }
  M.IntoUnderlyingSink = We;
  const Ve = typeof FinalizationRegistry > "u" ? { register: () => {
  }, unregister: () => {
  } } : new FinalizationRegistry((n) => b.__wbg_intounderlyingsource_free(n >>> 0, 1));
  class qe {
    __destroy_into_raw() {
      const e = this.__wbg_ptr;
      return this.__wbg_ptr = 0, Ve.unregister(this), e;
    }
    free() {
      const e = this.__destroy_into_raw();
      b.__wbg_intounderlyingsource_free(e, 0);
    }
    /**
     * @param {ReadableStreamDefaultController} controller
     * @returns {Promise<any>}
     */
    pull(e) {
      return b.intounderlyingsource_pull(this.__wbg_ptr, e);
    }
    cancel() {
      const e = this.__destroy_into_raw();
      b.intounderlyingsource_cancel(e);
    }
  }
  M.IntoUnderlyingSource = qe;
  const Z = typeof FinalizationRegistry > "u" ? { register: () => {
  }, unregister: () => {
  } } : new FinalizationRegistry((n) => b.__wbg_webhandle_free(n >>> 0, 1));
  class Ue {
    __destroy_into_raw() {
      const e = this.__wbg_ptr;
      return this.__wbg_ptr = 0, Z.unregister(this), e;
    }
    free() {
      const e = this.__destroy_into_raw();
      b.__wbg_webhandle_free(e, 0);
    }
    /**
     * @param {any} app_options
     */
    constructor(e) {
      const t = b.webhandle_new(e);
      if (t[2])
        throw k(t[1]);
      return this.__wbg_ptr = t[0] >>> 0, Z.register(this, this.__wbg_ptr, this), this;
    }
    /**
     * @param {any} canvas
     * @returns {Promise<void>}
     */
    start(e) {
      return b.webhandle_start(this.__wbg_ptr, e);
    }
    /**
     * @param {boolean | null} [value]
     */
    toggle_panel_overrides(e) {
      b.webhandle_toggle_panel_overrides(this.__wbg_ptr, g(e) ? 16777215 : e ? 1 : 0);
    }
    /**
     * @param {string} panel
     * @param {string | null} [state]
     */
    override_panel_state(e, t) {
      const _ = m(e, b.__wbindgen_malloc, b.__wbindgen_realloc), r = d;
      var c = g(t) ? 0 : m(t, b.__wbindgen_malloc, b.__wbindgen_realloc), o = d;
      const f = b.webhandle_override_panel_state(this.__wbg_ptr, _, r, c, o);
      if (f[1])
        throw k(f[0]);
    }
    destroy() {
      b.webhandle_destroy(this.__wbg_ptr);
    }
    /**
     * @returns {boolean}
     */
    has_panicked() {
      return b.webhandle_has_panicked(this.__wbg_ptr) !== 0;
    }
    /**
     * @returns {string | undefined}
     */
    panic_message() {
      const e = b.webhandle_panic_message(this.__wbg_ptr);
      let t;
      return e[0] !== 0 && (t = u(e[0], e[1]).slice(), b.__wbindgen_free(e[0], e[1] * 1, 1)), t;
    }
    /**
     * @returns {string | undefined}
     */
    panic_callstack() {
      const e = b.webhandle_panic_callstack(this.__wbg_ptr);
      let t;
      return e[0] !== 0 && (t = u(e[0], e[1]).slice(), b.__wbindgen_free(e[0], e[1] * 1, 1)), t;
    }
    /**
     * Add a new receiver streaming data from the given url.
     *
     * If `follow_if_http` is `true`, and the url is an HTTP source, the viewer will open the stream
     * in `Following` mode rather than `Playing` mode.
     *
     * Websocket streams are always opened in `Following` mode.
     *
     * It is an error to open a channel twice with the same id.
     * @param {string} url
     * @param {boolean | null} [follow_if_http]
     */
    add_receiver(e, t) {
      const _ = m(e, b.__wbindgen_malloc, b.__wbindgen_realloc), r = d;
      b.webhandle_add_receiver(this.__wbg_ptr, _, r, g(t) ? 16777215 : t ? 1 : 0);
    }
    /**
     * @param {string} url
     */
    remove_receiver(e) {
      const t = m(e, b.__wbindgen_malloc, b.__wbindgen_realloc), _ = d;
      b.webhandle_remove_receiver(this.__wbg_ptr, t, _);
    }
    /**
     * Open a new channel for streaming data.
     *
     * It is an error to open a channel twice with the same id.
     * @param {string} id
     * @param {string} channel_name
     */
    open_channel(e, t) {
      const _ = m(e, b.__wbindgen_malloc, b.__wbindgen_realloc), r = d, c = m(t, b.__wbindgen_malloc, b.__wbindgen_realloc), o = d;
      b.webhandle_open_channel(this.__wbg_ptr, _, r, c, o);
    }
    /**
     * Close an existing channel for streaming data.
     *
     * No-op if the channel is already closed.
     * @param {string} id
     */
    close_channel(e) {
      const t = m(e, b.__wbindgen_malloc, b.__wbindgen_realloc), _ = d;
      b.webhandle_close_channel(this.__wbg_ptr, t, _);
    }
    /**
     * Add an rrd to the viewer directly from a byte array.
     * @param {string} id
     * @param {Uint8Array} data
     */
    send_rrd_to_channel(e, t) {
      const _ = m(e, b.__wbindgen_malloc, b.__wbindgen_realloc), r = d, c = N(t, b.__wbindgen_malloc), o = d;
      b.webhandle_send_rrd_to_channel(this.__wbg_ptr, _, r, c, o);
    }
    /**
     * @param {string} id
     * @param {Uint8Array} data
     */
    send_table_to_channel(e, t) {
      const _ = m(e, b.__wbindgen_malloc, b.__wbindgen_realloc), r = d, c = N(t, b.__wbindgen_malloc), o = d;
      b.webhandle_send_table_to_channel(this.__wbg_ptr, _, r, c, o);
    }
    /**
     * @returns {string | undefined}
     */
    get_active_recording_id() {
      const e = b.webhandle_get_active_recording_id(this.__wbg_ptr);
      let t;
      return e[0] !== 0 && (t = u(e[0], e[1]).slice(), b.__wbindgen_free(e[0], e[1] * 1, 1)), t;
    }
    /**
     * @param {string} recording_id
     */
    set_active_recording_id(e) {
      const t = m(e, b.__wbindgen_malloc, b.__wbindgen_realloc), _ = d;
      b.webhandle_set_active_recording_id(this.__wbg_ptr, t, _);
    }
    /**
     * @param {string} recording_id
     * @returns {string | undefined}
     */
    get_active_timeline(e) {
      const t = m(e, b.__wbindgen_malloc, b.__wbindgen_realloc), _ = d, r = b.webhandle_get_active_timeline(this.__wbg_ptr, t, _);
      let c;
      return r[0] !== 0 && (c = u(r[0], r[1]).slice(), b.__wbindgen_free(r[0], r[1] * 1, 1)), c;
    }
    /**
     * Set the active timeline.
     *
     * This does nothing if the timeline can't be found.
     * @param {string} recording_id
     * @param {string} timeline_name
     */
    set_active_timeline(e, t) {
      const _ = m(e, b.__wbindgen_malloc, b.__wbindgen_realloc), r = d, c = m(t, b.__wbindgen_malloc, b.__wbindgen_realloc), o = d;
      b.webhandle_set_active_timeline(this.__wbg_ptr, _, r, c, o);
    }
    /**
     * @param {string} recording_id
     * @param {string} timeline_name
     * @returns {number | undefined}
     */
    get_time_for_timeline(e, t) {
      const _ = m(e, b.__wbindgen_malloc, b.__wbindgen_realloc), r = d, c = m(t, b.__wbindgen_malloc, b.__wbindgen_realloc), o = d, f = b.webhandle_get_time_for_timeline(this.__wbg_ptr, _, r, c, o);
      return f[0] === 0 ? void 0 : f[1];
    }
    /**
     * @param {string} recording_id
     * @param {string} timeline_name
     * @param {number} time
     */
    set_time_for_timeline(e, t, _) {
      const r = m(e, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d, o = m(t, b.__wbindgen_malloc, b.__wbindgen_realloc), f = d;
      b.webhandle_set_time_for_timeline(this.__wbg_ptr, r, c, o, f, _);
    }
    /**
     * @param {string} recording_id
     * @param {string} timeline_name
     * @returns {any}
     */
    get_timeline_time_range(e, t) {
      const _ = m(e, b.__wbindgen_malloc, b.__wbindgen_realloc), r = d, c = m(t, b.__wbindgen_malloc, b.__wbindgen_realloc), o = d;
      return b.webhandle_get_timeline_time_range(this.__wbg_ptr, _, r, c, o);
    }
    /**
     * @param {string} recording_id
     * @returns {boolean | undefined}
     */
    get_playing(e) {
      const t = m(e, b.__wbindgen_malloc, b.__wbindgen_realloc), _ = d, r = b.webhandle_get_playing(this.__wbg_ptr, t, _);
      return r === 16777215 ? void 0 : r !== 0;
    }
    /**
     * @param {string} recording_id
     * @param {boolean} value
     */
    set_playing(e, t) {
      const _ = m(e, b.__wbindgen_malloc, b.__wbindgen_realloc), r = d;
      b.webhandle_set_playing(this.__wbg_ptr, _, r, t);
    }
  }
  M.WebHandle = Ue;
  async function je(n, e) {
    if (typeof Response == "function" && n instanceof Response) {
      if (typeof WebAssembly.instantiateStreaming == "function")
        try {
          return await WebAssembly.instantiateStreaming(n, e);
        } catch (_) {
          if (n.headers.get("Content-Type") != "application/wasm")
            console.warn("`WebAssembly.instantiateStreaming` failed because your server does not serve Wasm with `application/wasm` MIME type. Falling back to `WebAssembly.instantiate` which is slower. Original error:\n", _);
          else
            throw _;
        }
      const t = await n.arrayBuffer();
      return await WebAssembly.instantiate(t, e);
    } else {
      const t = await WebAssembly.instantiate(n, e);
      return t instanceof WebAssembly.Instance ? { instance: t, module: n } : t;
    }
  }
  function ee() {
    const n = {};
    return n.wbg = {}, n.wbg.__wbg_Window_9e7ea8667e28eb00 = function(e) {
      return e.Window;
    }, n.wbg.__wbg_WorkerGlobalScope_0169ffb9adb5f5ef = function(e) {
      return e.WorkerGlobalScope;
    }, n.wbg.__wbg_abort_410ec47a64ac6117 = function(e, t) {
      e.abort(t);
    }, n.wbg.__wbg_abort_775ef1d17fc65868 = function(e) {
      e.abort();
    }, n.wbg.__wbg_activeElement_367599fdfa7ad115 = function(e) {
      const t = e.activeElement;
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_activeElement_7cabba30de7b6b67 = function(e) {
      const t = e.activeElement;
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_activeTexture_0f19d8acfa0a14c2 = function(e, t) {
      e.activeTexture(t >>> 0);
    }, n.wbg.__wbg_activeTexture_460f2e367e813fb0 = function(e, t) {
      e.activeTexture(t >>> 0);
    }, n.wbg.__wbg_addEventListener_84ae3eac6e15480a = function() {
      return a(function(e, t, _, r, c) {
        e.addEventListener(u(t, _), r, c);
      }, arguments);
    }, n.wbg.__wbg_addEventListener_90e553fdce254421 = function() {
      return a(function(e, t, _, r) {
        e.addEventListener(u(t, _), r);
      }, arguments);
    }, n.wbg.__wbg_altKey_c33c03aed82e4275 = function(e) {
      return e.altKey;
    }, n.wbg.__wbg_altKey_d7495666df921121 = function(e) {
      return e.altKey;
    }, n.wbg.__wbg_appendChild_8204974b7328bf98 = function() {
      return a(function(e, t) {
        return e.appendChild(t);
      }, arguments);
    }, n.wbg.__wbg_append_8c7dd8d641a5f01b = function() {
      return a(function(e, t, _, r, c) {
        e.append(u(t, _), u(r, c));
      }, arguments);
    }, n.wbg.__wbg_append_e297e93346ee40b4 = function(e, t, _, r, c) {
      e.append(u(t, _), u(r, c));
    }, n.wbg.__wbg_arrayBuffer_d1b44c4390db422f = function() {
      return a(function(e) {
        return e.arrayBuffer();
      }, arguments);
    }, n.wbg.__wbg_arrayBuffer_f18c144cd0125f07 = function(e) {
      return e.arrayBuffer();
    }, n.wbg.__wbg_assign_276730d240c7d534 = function() {
      return a(function(e, t, _) {
        e.assign(u(t, _));
      }, arguments);
    }, n.wbg.__wbg_at_7d852dd9f194d43e = function(e, t) {
      return e.at(t);
    }, n.wbg.__wbg_attachShader_3d4eb6af9e3e7bd1 = function(e, t, _) {
      e.attachShader(t, _);
    }, n.wbg.__wbg_attachShader_94e758c8b5283eb2 = function(e, t, _) {
      e.attachShader(t, _);
    }, n.wbg.__wbg_back_2ed2050faebe67d8 = function() {
      return a(function(e) {
        e.back();
      }, arguments);
    }, n.wbg.__wbg_beginQuery_6af0b28414b16c07 = function(e, t, _) {
      e.beginQuery(t >>> 0, _);
    }, n.wbg.__wbg_beginRenderPass_aefd0d9681a1f010 = function() {
      return a(function(e, t) {
        return e.beginRenderPass(t);
      }, arguments);
    }, n.wbg.__wbg_bindAttribLocation_40da4b3e84cc7bd5 = function(e, t, _, r, c) {
      e.bindAttribLocation(t, _ >>> 0, u(r, c));
    }, n.wbg.__wbg_bindAttribLocation_ce2730e29976d230 = function(e, t, _, r, c) {
      e.bindAttribLocation(t, _ >>> 0, u(r, c));
    }, n.wbg.__wbg_bindBufferRange_454f90f2b1781982 = function(e, t, _, r, c, o) {
      e.bindBufferRange(t >>> 0, _ >>> 0, r, c, o);
    }, n.wbg.__wbg_bindBuffer_309c9a6c21826cf5 = function(e, t, _) {
      e.bindBuffer(t >>> 0, _);
    }, n.wbg.__wbg_bindBuffer_f32f587f1c2962a7 = function(e, t, _) {
      e.bindBuffer(t >>> 0, _);
    }, n.wbg.__wbg_bindFramebuffer_bd02c8cc707d670f = function(e, t, _) {
      e.bindFramebuffer(t >>> 0, _);
    }, n.wbg.__wbg_bindFramebuffer_e48e83c0f973944d = function(e, t, _) {
      e.bindFramebuffer(t >>> 0, _);
    }, n.wbg.__wbg_bindRenderbuffer_53eedd88e52b4cb5 = function(e, t, _) {
      e.bindRenderbuffer(t >>> 0, _);
    }, n.wbg.__wbg_bindRenderbuffer_55e205fecfddbb8c = function(e, t, _) {
      e.bindRenderbuffer(t >>> 0, _);
    }, n.wbg.__wbg_bindSampler_9f59cf2eaa22eee0 = function(e, t, _) {
      e.bindSampler(t >>> 0, _);
    }, n.wbg.__wbg_bindTexture_a6e795697f49ebd1 = function(e, t, _) {
      e.bindTexture(t >>> 0, _);
    }, n.wbg.__wbg_bindTexture_bc8eb316247f739d = function(e, t, _) {
      e.bindTexture(t >>> 0, _);
    }, n.wbg.__wbg_bindVertexArrayOES_da8e7059b789629e = function(e, t) {
      e.bindVertexArrayOES(t);
    }, n.wbg.__wbg_bindVertexArray_6b4b88581064b71f = function(e, t) {
      e.bindVertexArray(t);
    }, n.wbg.__wbg_blendColor_15ba1eff44560932 = function(e, t, _, r, c) {
      e.blendColor(t, _, r, c);
    }, n.wbg.__wbg_blendColor_6446fba673f64ff0 = function(e, t, _, r, c) {
      e.blendColor(t, _, r, c);
    }, n.wbg.__wbg_blendEquationSeparate_c1aa26a9a5c5267e = function(e, t, _) {
      e.blendEquationSeparate(t >>> 0, _ >>> 0);
    }, n.wbg.__wbg_blendEquationSeparate_f3d422e981d86339 = function(e, t, _) {
      e.blendEquationSeparate(t >>> 0, _ >>> 0);
    }, n.wbg.__wbg_blendEquation_c23d111ad6d268ff = function(e, t) {
      e.blendEquation(t >>> 0);
    }, n.wbg.__wbg_blendEquation_cec7bc41f3e5704c = function(e, t) {
      e.blendEquation(t >>> 0);
    }, n.wbg.__wbg_blendFuncSeparate_483be8d4dd635340 = function(e, t, _, r, c) {
      e.blendFuncSeparate(t >>> 0, _ >>> 0, r >>> 0, c >>> 0);
    }, n.wbg.__wbg_blendFuncSeparate_dafeabfc1680b2ee = function(e, t, _, r, c) {
      e.blendFuncSeparate(t >>> 0, _ >>> 0, r >>> 0, c >>> 0);
    }, n.wbg.__wbg_blendFunc_9454884a3cfd2911 = function(e, t, _) {
      e.blendFunc(t >>> 0, _ >>> 0);
    }, n.wbg.__wbg_blendFunc_c3b74be5a39c665f = function(e, t, _) {
      e.blendFunc(t >>> 0, _ >>> 0);
    }, n.wbg.__wbg_blitFramebuffer_7303bdff77cfe967 = function(e, t, _, r, c, o, f, i, s, p, y) {
      e.blitFramebuffer(t, _, r, c, o, f, i, s, p >>> 0, y >>> 0);
    }, n.wbg.__wbg_blockSize_1490803190b57a34 = function(e) {
      return e.blockSize;
    }, n.wbg.__wbg_blur_c2ad8cc71bac3974 = function() {
      return a(function(e) {
        e.blur();
      }, arguments);
    }, n.wbg.__wbg_body_0b8fd1fe671660df = function(e) {
      const t = e.body;
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_body_942ea927546a04ba = function(e) {
      const t = e.body;
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_bottom_79b03e9c3d6f4e1e = function(e) {
      return e.bottom;
    }, n.wbg.__wbg_bufferData_3261d3e1dd6fc903 = function(e, t, _, r) {
      e.bufferData(t >>> 0, _, r >>> 0);
    }, n.wbg.__wbg_bufferData_33c59bf909ea6fd3 = function(e, t, _, r) {
      e.bufferData(t >>> 0, _, r >>> 0);
    }, n.wbg.__wbg_bufferData_463178757784fcac = function(e, t, _, r) {
      e.bufferData(t >>> 0, _, r >>> 0);
    }, n.wbg.__wbg_bufferData_d99b6b4eb5283f20 = function(e, t, _, r) {
      e.bufferData(t >>> 0, _, r >>> 0);
    }, n.wbg.__wbg_bufferSubData_4e973eefe9236d04 = function(e, t, _, r) {
      e.bufferSubData(t >>> 0, _, r);
    }, n.wbg.__wbg_bufferSubData_dcd4d16031a60345 = function(e, t, _, r) {
      e.bufferSubData(t >>> 0, _, r);
    }, n.wbg.__wbg_buffer_09165b52af8c5237 = function(e) {
      return e.buffer;
    }, n.wbg.__wbg_buffer_609cc3eee51ed158 = function(e) {
      return e.buffer;
    }, n.wbg.__wbg_button_f75c56aec440ea04 = function(e) {
      return e.button;
    }, n.wbg.__wbg_byobRequest_77d9adf63337edfb = function(e) {
      const t = e.byobRequest;
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_byteLength_e674b853d9c77e1d = function(e) {
      return e.byteLength;
    }, n.wbg.__wbg_byteOffset_fd862df290ef848d = function(e) {
      return e.byteOffset;
    }, n.wbg.__wbg_call_672a4d21634d4a24 = function() {
      return a(function(e, t) {
        return e.call(t);
      }, arguments);
    }, n.wbg.__wbg_call_7cccdd69e0791ae2 = function() {
      return a(function(e, t, _) {
        return e.call(t, _);
      }, arguments);
    }, n.wbg.__wbg_cancelAnimationFrame_089b48301c362fde = function() {
      return a(function(e, t) {
        e.cancelAnimationFrame(t);
      }, arguments);
    }, n.wbg.__wbg_cancel_8a308660caa6cadf = function(e) {
      return e.cancel();
    }, n.wbg.__wbg_catch_a6e601879b2610e9 = function(e, t) {
      return e.catch(t);
    }, n.wbg.__wbg_changedTouches_3654bea4294f2e86 = function(e) {
      return e.changedTouches;
    }, n.wbg.__wbg_clearBufferfv_65ea413f7f2554a2 = function(e, t, _, r, c) {
      e.clearBufferfv(t >>> 0, _, h(r, c));
    }, n.wbg.__wbg_clearBufferiv_c003c27b77a0245b = function(e, t, _, r, c) {
      e.clearBufferiv(t >>> 0, _, I(r, c));
    }, n.wbg.__wbg_clearBufferuiv_8c285072f2026a37 = function(e, t, _, r, c) {
      e.clearBufferuiv(t >>> 0, _, R(r, c));
    }, n.wbg.__wbg_clearDepth_17cfee5be8476fae = function(e, t) {
      e.clearDepth(t);
    }, n.wbg.__wbg_clearDepth_670d19914a501259 = function(e, t) {
      e.clearDepth(t);
    }, n.wbg.__wbg_clearInterval_ad2594253cc39c4b = function(e, t) {
      e.clearInterval(t);
    }, n.wbg.__wbg_clearStencil_4323424f1acca0df = function(e, t) {
      e.clearStencil(t);
    }, n.wbg.__wbg_clearStencil_7addd3b330b56b27 = function(e, t) {
      e.clearStencil(t);
    }, n.wbg.__wbg_clearTimeout_0b53d391c1b94dda = function(e) {
      return clearTimeout(e);
    }, n.wbg.__wbg_clear_62b9037b892f6988 = function(e, t) {
      e.clear(t >>> 0);
    }, n.wbg.__wbg_clear_f8d5f3c348d37d95 = function(e, t) {
      e.clear(t >>> 0);
    }, n.wbg.__wbg_clientWaitSync_6930890a42bd44c0 = function(e, t, _, r) {
      return e.clientWaitSync(t, _ >>> 0, r >>> 0);
    }, n.wbg.__wbg_clientX_5eb380a5f1fec6fd = function(e) {
      return e.clientX;
    }, n.wbg.__wbg_clientX_687c1a16e03e1f58 = function(e) {
      return e.clientX;
    }, n.wbg.__wbg_clientY_78d0605ac74642c2 = function(e) {
      return e.clientY;
    }, n.wbg.__wbg_clientY_d8b9c7f0c4e2e677 = function(e) {
      return e.clientY;
    }, n.wbg.__wbg_clipboardData_04bd9c1b0935d7e6 = function(e) {
      const t = e.clipboardData;
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_clipboard_93f8aa8cc426db44 = function(e) {
      return e.clipboard;
    }, n.wbg.__wbg_close_162e826d20a642ba = function(e) {
      e.close();
    }, n.wbg.__wbg_close_304cc1fef3466669 = function() {
      return a(function(e) {
        e.close();
      }, arguments);
    }, n.wbg.__wbg_close_5ce03e29be453811 = function() {
      return a(function(e) {
        e.close();
      }, arguments);
    }, n.wbg.__wbg_close_c97927f6f9d86747 = function() {
      return a(function(e) {
        e.close();
      }, arguments);
    }, n.wbg.__wbg_code_cfd8f6868bdaed9b = function(e) {
      return e.code;
    }, n.wbg.__wbg_colorMask_5e7c60b9c7a57a2e = function(e, t, _, r, c) {
      e.colorMask(t !== 0, _ !== 0, r !== 0, c !== 0);
    }, n.wbg.__wbg_colorMask_6dac12039c7145ae = function(e, t, _, r, c) {
      e.colorMask(t !== 0, _ !== 0, r !== 0, c !== 0);
    }, n.wbg.__wbg_compileShader_0ad770bbdbb9de21 = function(e, t) {
      e.compileShader(t);
    }, n.wbg.__wbg_compileShader_2307c9d370717dd5 = function(e, t) {
      e.compileShader(t);
    }, n.wbg.__wbg_compressedTexSubImage2D_71877eec950ca069 = function(e, t, _, r, c, o, f, i, s, p) {
      e.compressedTexSubImage2D(t >>> 0, _, r, c, o, f, i >>> 0, s, p);
    }, n.wbg.__wbg_compressedTexSubImage2D_99abf4cfdb7c3fd8 = function(e, t, _, r, c, o, f, i, s) {
      e.compressedTexSubImage2D(t >>> 0, _, r, c, o, f, i >>> 0, s);
    }, n.wbg.__wbg_compressedTexSubImage2D_d66dcfcb2422e703 = function(e, t, _, r, c, o, f, i, s) {
      e.compressedTexSubImage2D(t >>> 0, _, r, c, o, f, i >>> 0, s);
    }, n.wbg.__wbg_compressedTexSubImage3D_58506392da46b927 = function(e, t, _, r, c, o, f, i, s, p, y) {
      e.compressedTexSubImage3D(t >>> 0, _, r, c, o, f, i, s, p >>> 0, y);
    }, n.wbg.__wbg_compressedTexSubImage3D_81477746675a4017 = function(e, t, _, r, c, o, f, i, s, p, y, x) {
      e.compressedTexSubImage3D(t >>> 0, _, r, c, o, f, i, s, p >>> 0, y, x);
    }, n.wbg.__wbg_configure_69aea2f2c91d2049 = function() {
      return a(function(e, t) {
        e.configure(t);
      }, arguments);
    }, n.wbg.__wbg_configure_86dd92dde48d105a = function() {
      return a(function(e, t) {
        e.configure(t);
      }, arguments);
    }, n.wbg.__wbg_contentBoxSize_638692469db816f2 = function(e) {
      return e.contentBoxSize;
    }, n.wbg.__wbg_contentRect_81407eb60e52248f = function(e) {
      return e.contentRect;
    }, n.wbg.__wbg_copyBufferSubData_9469a965478e33b5 = function(e, t, _, r, c, o) {
      e.copyBufferSubData(t >>> 0, _ >>> 0, r, c, o);
    }, n.wbg.__wbg_copyBufferToBuffer_0d141e7111b0b6ab = function() {
      return a(function(e, t, _, r, c, o) {
        e.copyBufferToBuffer(t, _, r, c, o);
      }, arguments);
    }, n.wbg.__wbg_copyBufferToTexture_722a7aa47b5d891b = function() {
      return a(function(e, t, _, r) {
        e.copyBufferToTexture(t, _, r);
      }, arguments);
    }, n.wbg.__wbg_copyExternalImageToTexture_a2037621913ee52d = function() {
      return a(function(e, t, _, r) {
        e.copyExternalImageToTexture(t, _, r);
      }, arguments);
    }, n.wbg.__wbg_copyTexSubImage2D_05e7e8df6814a705 = function(e, t, _, r, c, o, f, i, s) {
      e.copyTexSubImage2D(t >>> 0, _, r, c, o, f, i, s);
    }, n.wbg.__wbg_copyTexSubImage2D_607ad28606952982 = function(e, t, _, r, c, o, f, i, s) {
      e.copyTexSubImage2D(t >>> 0, _, r, c, o, f, i, s);
    }, n.wbg.__wbg_copyTexSubImage3D_32e92c94044e58ca = function(e, t, _, r, c, o, f, i, s, p) {
      e.copyTexSubImage3D(t >>> 0, _, r, c, o, f, i, s, p);
    }, n.wbg.__wbg_copyTextureToBuffer_bb350c95b19e5999 = function() {
      return a(function(e, t, _, r) {
        e.copyTextureToBuffer(t, _, r);
      }, arguments);
    }, n.wbg.__wbg_createBindGroupLayout_f0635625a1a82bea = function() {
      return a(function(e, t) {
        return e.createBindGroupLayout(t);
      }, arguments);
    }, n.wbg.__wbg_createBindGroup_043b06d20124f91e = function(e, t) {
      return e.createBindGroup(t);
    }, n.wbg.__wbg_createBuffer_086a8bb05ced884a = function() {
      return a(function(e, t) {
        return e.createBuffer(t);
      }, arguments);
    }, n.wbg.__wbg_createBuffer_7a9ec3d654073660 = function(e) {
      const t = e.createBuffer();
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_createBuffer_9886e84a67b68c89 = function(e) {
      const t = e.createBuffer();
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_createCommandEncoder_aa9ae9d445bb7abf = function(e, t) {
      return e.createCommandEncoder(t);
    }, n.wbg.__wbg_createElement_8c9931a732ee2fea = function() {
      return a(function(e, t, _) {
        return e.createElement(u(t, _));
      }, arguments);
    }, n.wbg.__wbg_createFramebuffer_7824f69bba778885 = function(e) {
      const t = e.createFramebuffer();
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_createFramebuffer_c8d70ebc4858051e = function(e) {
      const t = e.createFramebuffer();
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_createObjectURL_6e98d2f9c7bd9764 = function() {
      return a(function(e, t) {
        const _ = URL.createObjectURL(t), r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
        w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
      }, arguments);
    }, n.wbg.__wbg_createPipelineLayout_5cc7e994e46201c7 = function(e, t) {
      return e.createPipelineLayout(t);
    }, n.wbg.__wbg_createProgram_8ff56c485f3233d0 = function(e) {
      const t = e.createProgram();
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_createProgram_da203074cafb1038 = function(e) {
      const t = e.createProgram();
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_createQuery_5ed5e770ec1009c1 = function(e) {
      const t = e.createQuery();
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_createRenderPipeline_47152f2f57b11194 = function() {
      return a(function(e, t) {
        return e.createRenderPipeline(t);
      }, arguments);
    }, n.wbg.__wbg_createRenderbuffer_d88aa9403faa38ea = function(e) {
      const t = e.createRenderbuffer();
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_createRenderbuffer_fd347ae14f262eaa = function(e) {
      const t = e.createRenderbuffer();
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_createSampler_f3970b77a6f36963 = function(e, t) {
      return e.createSampler(t);
    }, n.wbg.__wbg_createSampler_f76e29d7522bec9e = function(e) {
      const t = e.createSampler();
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_createShaderModule_9ec201507fe4949e = function(e, t) {
      return e.createShaderModule(t);
    }, n.wbg.__wbg_createShader_4a256a8cc9c1ce4f = function(e, t) {
      const _ = e.createShader(t >>> 0);
      return g(_) ? 0 : l(_);
    }, n.wbg.__wbg_createShader_983150fb1243ee56 = function(e, t) {
      const _ = e.createShader(t >>> 0);
      return g(_) ? 0 : l(_);
    }, n.wbg.__wbg_createTexture_09f18232c5ad6e69 = function() {
      return a(function(e, t) {
        return e.createTexture(t);
      }, arguments);
    }, n.wbg.__wbg_createTexture_9c536c79b635fdef = function(e) {
      const t = e.createTexture();
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_createTexture_bfaa54c0cd22e367 = function(e) {
      const t = e.createTexture();
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_createVertexArrayOES_991b44f100f93329 = function(e) {
      const t = e.createVertexArrayOES();
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_createVertexArray_e435029ae2660efd = function(e) {
      const t = e.createVertexArray();
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_createView_f7cd0a0356a46f3b = function() {
      return a(function(e, t) {
        return e.createView(t);
      }, arguments);
    }, n.wbg.__wbg_crypto_574e78ad8b13b65f = function(e) {
      return e.crypto;
    }, n.wbg.__wbg_ctrlKey_1e826e468105ac11 = function(e) {
      return e.ctrlKey;
    }, n.wbg.__wbg_ctrlKey_cdbe8154dfb00d1f = function(e) {
      return e.ctrlKey;
    }, n.wbg.__wbg_cullFace_187079e6e20a464d = function(e, t) {
      e.cullFace(t >>> 0);
    }, n.wbg.__wbg_cullFace_fbae6dd4d5e61ba4 = function(e, t) {
      e.cullFace(t >>> 0);
    }, n.wbg.__wbg_dataTransfer_86283b0702a1aff1 = function(e) {
      const t = e.dataTransfer;
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_data_432d9c3df2630942 = function(e) {
      return e.data;
    }, n.wbg.__wbg_data_e77bd5c125ecc8a8 = function(e, t) {
      const _ = t.data;
      var r = g(_) ? 0 : m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
      w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
    }, n.wbg.__wbg_debug_ac23b449350db4e1 = function(e, t) {
      console.debug(u(e, t));
    }, n.wbg.__wbg_decode_6c36f113295ffd87 = function() {
      return a(function(e, t) {
        e.decode(t);
      }, arguments);
    }, n.wbg.__wbg_deleteBuffer_7ed96e1bf7c02e87 = function(e, t) {
      e.deleteBuffer(t);
    }, n.wbg.__wbg_deleteBuffer_a7822433fc95dfb8 = function(e, t) {
      e.deleteBuffer(t);
    }, n.wbg.__wbg_deleteFramebuffer_66853fb7101488cb = function(e, t) {
      e.deleteFramebuffer(t);
    }, n.wbg.__wbg_deleteFramebuffer_cd3285ee5a702a7a = function(e, t) {
      e.deleteFramebuffer(t);
    }, n.wbg.__wbg_deleteProgram_3fa626bbc0001eb7 = function(e, t) {
      e.deleteProgram(t);
    }, n.wbg.__wbg_deleteProgram_71a133c6d053e272 = function(e, t) {
      e.deleteProgram(t);
    }, n.wbg.__wbg_deleteQuery_6a2b7cd30074b20b = function(e, t) {
      e.deleteQuery(t);
    }, n.wbg.__wbg_deleteRenderbuffer_59f4369653485031 = function(e, t) {
      e.deleteRenderbuffer(t);
    }, n.wbg.__wbg_deleteRenderbuffer_8808192853211567 = function(e, t) {
      e.deleteRenderbuffer(t);
    }, n.wbg.__wbg_deleteSampler_7f02bb003ba547f0 = function(e, t) {
      e.deleteSampler(t);
    }, n.wbg.__wbg_deleteShader_8d42f169deda58ac = function(e, t) {
      e.deleteShader(t);
    }, n.wbg.__wbg_deleteShader_c65a44796c5004d8 = function(e, t) {
      e.deleteShader(t);
    }, n.wbg.__wbg_deleteSync_5a3fbe5d6b742398 = function(e, t) {
      e.deleteSync(t);
    }, n.wbg.__wbg_deleteTexture_a30f5ca0163c4110 = function(e, t) {
      e.deleteTexture(t);
    }, n.wbg.__wbg_deleteTexture_bb82c9fec34372ba = function(e, t) {
      e.deleteTexture(t);
    }, n.wbg.__wbg_deleteVertexArrayOES_1ee7a06a4b23ec8c = function(e, t) {
      e.deleteVertexArrayOES(t);
    }, n.wbg.__wbg_deleteVertexArray_77fe73664a3332ae = function(e, t) {
      e.deleteVertexArray(t);
    }, n.wbg.__wbg_delete_5ffea89592972463 = function() {
      return a(function(e, t, _) {
        delete e[u(t, _)];
      }, arguments);
    }, n.wbg.__wbg_deltaMode_9bfd9fe3f6b4b240 = function(e) {
      return e.deltaMode;
    }, n.wbg.__wbg_deltaX_5c1121715746e4b7 = function(e) {
      return e.deltaX;
    }, n.wbg.__wbg_deltaY_f9318542caea0c36 = function(e) {
      return e.deltaY;
    }, n.wbg.__wbg_depthFunc_2906916f4536d5d7 = function(e, t) {
      e.depthFunc(t >>> 0);
    }, n.wbg.__wbg_depthFunc_f34449ae87cc4e3e = function(e, t) {
      e.depthFunc(t >>> 0);
    }, n.wbg.__wbg_depthMask_5fe84e2801488eda = function(e, t) {
      e.depthMask(t !== 0);
    }, n.wbg.__wbg_depthMask_76688a8638b2f321 = function(e, t) {
      e.depthMask(t !== 0);
    }, n.wbg.__wbg_depthRange_3cd6b4dc961d9116 = function(e, t, _) {
      e.depthRange(t, _);
    }, n.wbg.__wbg_depthRange_f9c084ff3d81fd7b = function(e, t, _) {
      e.depthRange(t, _);
    }, n.wbg.__wbg_destroy_0252d01ac8a09285 = function(e) {
      e.destroy();
    }, n.wbg.__wbg_destroy_c8cba128dc1a0e2d = function(e) {
      e.destroy();
    }, n.wbg.__wbg_devicePixelContentBoxSize_a6de82cb30d70825 = function(e) {
      return e.devicePixelContentBoxSize;
    }, n.wbg.__wbg_devicePixelRatio_68c391265f05d093 = function(e) {
      return e.devicePixelRatio;
    }, n.wbg.__wbg_disableVertexAttribArray_452cc9815fced7e4 = function(e, t) {
      e.disableVertexAttribArray(t >>> 0);
    }, n.wbg.__wbg_disableVertexAttribArray_afd097fb465dc100 = function(e, t) {
      e.disableVertexAttribArray(t >>> 0);
    }, n.wbg.__wbg_disable_2702df5b5da5dd21 = function(e, t) {
      e.disable(t >>> 0);
    }, n.wbg.__wbg_disable_8b53998501a7a85b = function(e, t) {
      e.disable(t >>> 0);
    }, n.wbg.__wbg_disconnect_ac3f4ba550970c76 = function(e) {
      e.disconnect();
    }, n.wbg.__wbg_displayHeight_a6ff7964b6182d84 = function(e) {
      return e.displayHeight;
    }, n.wbg.__wbg_displayWidth_d82e7b620f6f4189 = function(e) {
      return e.displayWidth;
    }, n.wbg.__wbg_document_d249400bd7bd996d = function(e) {
      const t = e.document;
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_done_769e5ede4b31c67b = function(e) {
      return e.done;
    }, n.wbg.__wbg_drawArraysInstancedANGLE_342ee6b5236d9702 = function(e, t, _, r, c) {
      e.drawArraysInstancedANGLE(t >>> 0, _, r, c);
    }, n.wbg.__wbg_drawArraysInstanced_622ea9f149b0b80c = function(e, t, _, r, c) {
      e.drawArraysInstanced(t >>> 0, _, r, c);
    }, n.wbg.__wbg_drawArrays_6acaa2669c105f3a = function(e, t, _, r) {
      e.drawArrays(t >>> 0, _, r);
    }, n.wbg.__wbg_drawArrays_6d29ea2ebc0c72a2 = function(e, t, _, r) {
      e.drawArrays(t >>> 0, _, r);
    }, n.wbg.__wbg_drawBuffersWEBGL_9fdbdf3d4cbd3aae = function(e, t) {
      e.drawBuffersWEBGL(t);
    }, n.wbg.__wbg_drawBuffers_e729b75c5a50d760 = function(e, t) {
      e.drawBuffers(t);
    }, n.wbg.__wbg_drawElementsInstancedANGLE_096b48ab8686c5cf = function(e, t, _, r, c, o) {
      e.drawElementsInstancedANGLE(t >>> 0, _, r >>> 0, c, o);
    }, n.wbg.__wbg_drawElementsInstanced_f874e87d0b4e95e9 = function(e, t, _, r, c, o) {
      e.drawElementsInstanced(t >>> 0, _, r >>> 0, c, o);
    }, n.wbg.__wbg_drawIndexed_322c2f9f038d7b23 = function(e, t, _, r, c, o) {
      e.drawIndexed(t >>> 0, _ >>> 0, r >>> 0, c, o >>> 0);
    }, n.wbg.__wbg_draw_d38c9207eb049f56 = function(e, t, _, r, c) {
      e.draw(t >>> 0, _ >>> 0, r >>> 0, c >>> 0);
    }, n.wbg.__wbg_elementFromPoint_be6286b8ec1ae1a2 = function(e, t, _) {
      const r = e.elementFromPoint(t, _);
      return g(r) ? 0 : l(r);
    }, n.wbg.__wbg_elementFromPoint_e788840a5168e09e = function(e, t, _) {
      const r = e.elementFromPoint(t, _);
      return g(r) ? 0 : l(r);
    }, n.wbg.__wbg_enableVertexAttribArray_607be07574298e5e = function(e, t) {
      e.enableVertexAttribArray(t >>> 0);
    }, n.wbg.__wbg_enableVertexAttribArray_93c3d406a41ad6c7 = function(e, t) {
      e.enableVertexAttribArray(t >>> 0);
    }, n.wbg.__wbg_enable_51114837e05ee280 = function(e, t) {
      e.enable(t >>> 0);
    }, n.wbg.__wbg_enable_d183fef39258803f = function(e, t) {
      e.enable(t >>> 0);
    }, n.wbg.__wbg_endQuery_17aac36532ca7d47 = function(e, t) {
      e.endQuery(t >>> 0);
    }, n.wbg.__wbg_end_d54348baf0bf3b70 = function(e) {
      e.end();
    }, n.wbg.__wbg_enqueue_bb16ba72f537dc9e = function() {
      return a(function(e, t) {
        e.enqueue(t);
      }, arguments);
    }, n.wbg.__wbg_entries_3265d4158b33e5dc = function(e) {
      return Object.entries(e);
    }, n.wbg.__wbg_error_4dd933556fcdce70 = function(e, t) {
      let _, r;
      try {
        _ = e, r = t, console.error(u(e, t));
      } finally {
        b.__wbindgen_free(_, r, 1);
      }
    }, n.wbg.__wbg_error_524f506f44df1645 = function(e) {
      console.error(e);
    }, n.wbg.__wbg_error_53172b72ea901998 = function(e) {
      return e.error;
    }, n.wbg.__wbg_features_a4866072bcfdb3fb = function(e) {
      return e.features;
    }, n.wbg.__wbg_fenceSync_02d142d21e315da6 = function(e, t, _) {
      const r = e.fenceSync(t >>> 0, _ >>> 0);
      return g(r) ? 0 : l(r);
    }, n.wbg.__wbg_fetch_07cd86dd296a5a63 = function(e, t, _) {
      return e.fetch(t, _);
    }, n.wbg.__wbg_fetch_11bff8299d0ecd2b = function(e) {
      return fetch(e);
    }, n.wbg.__wbg_fetch_509096533071c657 = function(e, t) {
      return e.fetch(t);
    }, n.wbg.__wbg_fetch_b7bf320f681242d2 = function(e, t) {
      return e.fetch(t);
    }, n.wbg.__wbg_fetch_f083e6da40cefe09 = function(e, t) {
      return fetch(e, t);
    }, n.wbg.__wbg_files_5f07ac9b6f9116a7 = function(e) {
      const t = e.files;
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_files_790cda07a2445fac = function(e) {
      const t = e.files;
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_finish_db34a19c90c07af7 = function(e) {
      return e.finish();
    }, n.wbg.__wbg_finish_e2d3808af76b422a = function(e, t) {
      return e.finish(t);
    }, n.wbg.__wbg_flush_4150080f65c49208 = function(e) {
      e.flush();
    }, n.wbg.__wbg_flush_66529217e53a99ff = function(e) {
      return e.flush();
    }, n.wbg.__wbg_flush_987c35de09e06fd6 = function(e) {
      e.flush();
    }, n.wbg.__wbg_focus_7d08b55eba7b368d = function() {
      return a(function(e) {
        e.focus();
      }, arguments);
    }, n.wbg.__wbg_force_6e5acfdea2af0a4f = function(e) {
      return e.force;
    }, n.wbg.__wbg_forward_9cb3721c72abe28a = function() {
      return a(function(e) {
        e.forward();
      }, arguments);
    }, n.wbg.__wbg_framebufferRenderbuffer_2fdd12e89ad81eb9 = function(e, t, _, r, c) {
      e.framebufferRenderbuffer(t >>> 0, _ >>> 0, r >>> 0, c);
    }, n.wbg.__wbg_framebufferRenderbuffer_8b88592753b54715 = function(e, t, _, r, c) {
      e.framebufferRenderbuffer(t >>> 0, _ >>> 0, r >>> 0, c);
    }, n.wbg.__wbg_framebufferTexture2D_81a565732bd5d8fe = function(e, t, _, r, c, o) {
      e.framebufferTexture2D(t >>> 0, _ >>> 0, r >>> 0, c, o);
    }, n.wbg.__wbg_framebufferTexture2D_ed855d0b097c557a = function(e, t, _, r, c, o) {
      e.framebufferTexture2D(t >>> 0, _ >>> 0, r >>> 0, c, o);
    }, n.wbg.__wbg_framebufferTextureLayer_5e6bd1b0cb45d815 = function(e, t, _, r, c, o) {
      e.framebufferTextureLayer(t >>> 0, _ >>> 0, r, c, o);
    }, n.wbg.__wbg_framebufferTextureMultiviewOVR_e54f936c3cc382cb = function(e, t, _, r, c, o, f) {
      e.framebufferTextureMultiviewOVR(t >>> 0, _ >>> 0, r, c, o, f);
    }, n.wbg.__wbg_frontFace_289c9d7a8569c4f2 = function(e, t) {
      e.frontFace(t >>> 0);
    }, n.wbg.__wbg_frontFace_4d4936cfaeb8b7df = function(e, t) {
      e.frontFace(t >>> 0);
    }, n.wbg.__wbg_getBindGroupLayout_2c3c6eeaf8ec7b50 = function(e, t) {
      return e.getBindGroupLayout(t >>> 0);
    }, n.wbg.__wbg_getBoundingClientRect_9073b0ff7574d76b = function(e) {
      return e.getBoundingClientRect();
    }, n.wbg.__wbg_getBufferSubData_8ab2dcc5fcf5770f = function(e, t, _, r) {
      e.getBufferSubData(t >>> 0, _, r);
    }, n.wbg.__wbg_getComputedStyle_046dd6472f8e7f1d = function() {
      return a(function(e, t) {
        const _ = e.getComputedStyle(t);
        return g(_) ? 0 : l(_);
      }, arguments);
    }, n.wbg.__wbg_getContext_3ae09aaa73194801 = function() {
      return a(function(e, t, _, r) {
        const c = e.getContext(u(t, _), r);
        return g(c) ? 0 : l(c);
      }, arguments);
    }, n.wbg.__wbg_getContext_e9cf379449413580 = function() {
      return a(function(e, t, _) {
        const r = e.getContext(u(t, _));
        return g(r) ? 0 : l(r);
      }, arguments);
    }, n.wbg.__wbg_getContext_f65a0debd1e8f8e8 = function() {
      return a(function(e, t, _) {
        const r = e.getContext(u(t, _));
        return g(r) ? 0 : l(r);
      }, arguments);
    }, n.wbg.__wbg_getContext_fc19859df6331073 = function() {
      return a(function(e, t, _, r) {
        const c = e.getContext(u(t, _), r);
        return g(c) ? 0 : l(c);
      }, arguments);
    }, n.wbg.__wbg_getCurrentTexture_6ee19b05d6ba43ba = function() {
      return a(function(e) {
        return e.getCurrentTexture();
      }, arguments);
    }, n.wbg.__wbg_getData_84cc441a50843727 = function() {
      return a(function(e, t, _, r) {
        const c = t.getData(u(_, r)), o = m(c, b.__wbindgen_malloc, b.__wbindgen_realloc), f = d;
        w().setInt32(e + 4 * 1, f, !0), w().setInt32(e + 4 * 0, o, !0);
      }, arguments);
    }, n.wbg.__wbg_getElementById_f827f0d6648718a8 = function(e, t, _) {
      const r = e.getElementById(u(t, _));
      return g(r) ? 0 : l(r);
    }, n.wbg.__wbg_getExtension_ff0fb1398bcf28c3 = function() {
      return a(function(e, t, _) {
        const r = e.getExtension(u(t, _));
        return g(r) ? 0 : l(r);
      }, arguments);
    }, n.wbg.__wbg_getIndexedParameter_f9211edc36533919 = function() {
      return a(function(e, t, _) {
        return e.getIndexedParameter(t >>> 0, _ >>> 0);
      }, arguments);
    }, n.wbg.__wbg_getItem_17f98dee3b43fa7e = function() {
      return a(function(e, t, _, r) {
        const c = t.getItem(u(_, r));
        var o = g(c) ? 0 : m(c, b.__wbindgen_malloc, b.__wbindgen_realloc), f = d;
        w().setInt32(e + 4 * 1, f, !0), w().setInt32(e + 4 * 0, o, !0);
      }, arguments);
    }, n.wbg.__wbg_getMappedRange_b986a889b6b53379 = function() {
      return a(function(e, t, _) {
        return e.getMappedRange(t, _);
      }, arguments);
    }, n.wbg.__wbg_getParameter_1f0887a2b88e6d19 = function() {
      return a(function(e, t) {
        return e.getParameter(t >>> 0);
      }, arguments);
    }, n.wbg.__wbg_getParameter_e3429f024018310f = function() {
      return a(function(e, t) {
        return e.getParameter(t >>> 0);
      }, arguments);
    }, n.wbg.__wbg_getPreferredCanvasFormat_c56b5a9a243fe942 = function(e) {
      const t = e.getPreferredCanvasFormat();
      return (A.indexOf(t) + 1 || 96) - 1;
    }, n.wbg.__wbg_getProgramInfoLog_631c180b1b21c8ed = function(e, t, _) {
      const r = t.getProgramInfoLog(_);
      var c = g(r) ? 0 : m(r, b.__wbindgen_malloc, b.__wbindgen_realloc), o = d;
      w().setInt32(e + 4 * 1, o, !0), w().setInt32(e + 4 * 0, c, !0);
    }, n.wbg.__wbg_getProgramInfoLog_a998105a680059db = function(e, t, _) {
      const r = t.getProgramInfoLog(_);
      var c = g(r) ? 0 : m(r, b.__wbindgen_malloc, b.__wbindgen_realloc), o = d;
      w().setInt32(e + 4 * 1, o, !0), w().setInt32(e + 4 * 0, c, !0);
    }, n.wbg.__wbg_getProgramParameter_0c411f0cd4185c5b = function(e, t, _) {
      return e.getProgramParameter(t, _ >>> 0);
    }, n.wbg.__wbg_getProgramParameter_360f95ff07ac068d = function(e, t, _) {
      return e.getProgramParameter(t, _ >>> 0);
    }, n.wbg.__wbg_getPropertyValue_e623c23a05dfb30c = function() {
      return a(function(e, t, _, r) {
        const c = t.getPropertyValue(u(_, r)), o = m(c, b.__wbindgen_malloc, b.__wbindgen_realloc), f = d;
        w().setInt32(e + 4 * 1, f, !0), w().setInt32(e + 4 * 0, o, !0);
      }, arguments);
    }, n.wbg.__wbg_getQueryParameter_8921497e1d1561c1 = function(e, t, _) {
      return e.getQueryParameter(t, _ >>> 0);
    }, n.wbg.__wbg_getRandomValues_38097e921c2494c3 = function() {
      return a(function(e, t) {
        globalThis.crypto.getRandomValues(H(e, t));
      }, arguments);
    }, n.wbg.__wbg_getRandomValues_3c9c0d586e575a16 = function() {
      return a(function(e, t) {
        globalThis.crypto.getRandomValues(H(e, t));
      }, arguments);
    }, n.wbg.__wbg_getRandomValues_b8f5dbd5f3995a9e = function() {
      return a(function(e, t) {
        e.getRandomValues(t);
      }, arguments);
    }, n.wbg.__wbg_getReader_48e00749fe3f6089 = function() {
      return a(function(e) {
        return e.getReader();
      }, arguments);
    }, n.wbg.__wbg_getRootNode_f59bcfa355239af5 = function(e) {
      return e.getRootNode();
    }, n.wbg.__wbg_getShaderInfoLog_7e7b38fb910ec534 = function(e, t, _) {
      const r = t.getShaderInfoLog(_);
      var c = g(r) ? 0 : m(r, b.__wbindgen_malloc, b.__wbindgen_realloc), o = d;
      w().setInt32(e + 4 * 1, o, !0), w().setInt32(e + 4 * 0, c, !0);
    }, n.wbg.__wbg_getShaderInfoLog_f59c3112acc6e039 = function(e, t, _) {
      const r = t.getShaderInfoLog(_);
      var c = g(r) ? 0 : m(r, b.__wbindgen_malloc, b.__wbindgen_realloc), o = d;
      w().setInt32(e + 4 * 1, o, !0), w().setInt32(e + 4 * 0, c, !0);
    }, n.wbg.__wbg_getShaderParameter_511b5f929074fa31 = function(e, t, _) {
      return e.getShaderParameter(t, _ >>> 0);
    }, n.wbg.__wbg_getShaderParameter_6dbe0b8558dc41fd = function(e, t, _) {
      return e.getShaderParameter(t, _ >>> 0);
    }, n.wbg.__wbg_getSupportedExtensions_8c007dbb54905635 = function(e) {
      const t = e.getSupportedExtensions();
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_getSupportedProfiles_10d2a4d32a128384 = function(e) {
      const t = e.getSupportedProfiles();
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_getSyncParameter_7cb8461f5891606c = function(e, t, _) {
      return e.getSyncParameter(t, _ >>> 0);
    }, n.wbg.__wbg_getTime_46267b1c24877e30 = function(e) {
      return e.getTime();
    }, n.wbg.__wbg_getUniformBlockIndex_288fdc31528171ca = function(e, t, _, r) {
      return e.getUniformBlockIndex(t, u(_, r));
    }, n.wbg.__wbg_getUniformLocation_657a2b6d102bd126 = function(e, t, _, r) {
      const c = e.getUniformLocation(t, u(_, r));
      return g(c) ? 0 : l(c);
    }, n.wbg.__wbg_getUniformLocation_838363001c74dc21 = function(e, t, _, r) {
      const c = e.getUniformLocation(t, u(_, r));
      return g(c) ? 0 : l(c);
    }, n.wbg.__wbg_get_3091cb4339203d1a = function(e, t) {
      const _ = e[t >>> 0];
      return g(_) ? 0 : l(_);
    }, n.wbg.__wbg_get_4095561f3d5ec806 = function(e, t) {
      const _ = e[t >>> 0];
      return g(_) ? 0 : l(_);
    }, n.wbg.__wbg_get_67b2ba62fc30de12 = function() {
      return a(function(e, t) {
        return Reflect.get(e, t);
      }, arguments);
    }, n.wbg.__wbg_get_8edd839202d9f4db = function(e, t) {
      const _ = e[t >>> 0];
      return g(_) ? 0 : l(_);
    }, n.wbg.__wbg_get_b9b93047fe3cf45b = function(e, t) {
      return e[t >>> 0];
    }, n.wbg.__wbg_get_e27dfaeb6f46bd45 = function(e, t) {
      const _ = e[t >>> 0];
      return g(_) ? 0 : l(_);
    }, n.wbg.__wbg_getdone_d47073731acd3e74 = function(e) {
      const t = e.done;
      return g(t) ? 16777215 : t ? 1 : 0;
    }, n.wbg.__wbg_getvalue_009dcd63692bee1f = function(e) {
      return e.value;
    }, n.wbg.__wbg_getwithrefkey_1dc361bd10053bfe = function(e, t) {
      return e[t];
    }, n.wbg.__wbg_gpu_1b22165b67dd5a59 = function(e) {
      return e.gpu;
    }, n.wbg.__wbg_hasOwnProperty_eb9a168e9990a716 = function(e, t) {
      return e.hasOwnProperty(t);
    }, n.wbg.__wbg_has_a5ea9117f258a0ec = function() {
      return a(function(e, t) {
        return Reflect.has(e, t);
      }, arguments);
    }, n.wbg.__wbg_has_c563a404388202f5 = function(e, t, _) {
      return e.has(u(t, _));
    }, n.wbg.__wbg_hash_dd4b49269c385c8a = function() {
      return a(function(e, t) {
        const _ = t.hash, r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
        w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
      }, arguments);
    }, n.wbg.__wbg_headers_7852a8ea641c1379 = function(e) {
      return e.headers;
    }, n.wbg.__wbg_headers_9cb51cfd2ac780a4 = function(e) {
      return e.headers;
    }, n.wbg.__wbg_height_1d93eb7f5e355d97 = function(e) {
      return e.height;
    }, n.wbg.__wbg_height_1f8226c8f6875110 = function(e) {
      return e.height;
    }, n.wbg.__wbg_height_838cee19ba8597db = function(e) {
      return e.height;
    }, n.wbg.__wbg_height_d3f39e12f0f62121 = function(e) {
      return e.height;
    }, n.wbg.__wbg_height_df1aa98dfbbe11ad = function(e) {
      return e.height;
    }, n.wbg.__wbg_height_e3c322f23d99ad2f = function(e) {
      return e.height;
    }, n.wbg.__wbg_hidden_d5c02c79a2b77bb6 = function(e) {
      return e.hidden;
    }, n.wbg.__wbg_history_b8221edd09c17656 = function() {
      return a(function(e) {
        return e.history;
      }, arguments);
    }, n.wbg.__wbg_host_9bd7b5dc07c48606 = function() {
      return a(function(e, t) {
        const _ = t.host, r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
        w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
      }, arguments);
    }, n.wbg.__wbg_hostname_8d7204884eb7378b = function() {
      return a(function(e, t) {
        const _ = t.hostname, r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
        w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
      }, arguments);
    }, n.wbg.__wbg_href_87d60a783a012377 = function() {
      return a(function(e, t) {
        const _ = t.href, r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
        w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
      }, arguments);
    }, n.wbg.__wbg_href_e36b397abf414828 = function(e, t) {
      const _ = t.href, r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
      w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
    }, n.wbg.__wbg_identifier_59e0705aef81ff93 = function(e) {
      return e.identifier;
    }, n.wbg.__wbg_includes_937486a108ec147b = function(e, t, _) {
      return e.includes(t, _);
    }, n.wbg.__wbg_info_2d6110670c6c7e63 = function(e, t) {
      console.info(u(e, t));
    }, n.wbg.__wbg_inlineSize_8ff96b3ec1b24423 = function(e) {
      return e.inlineSize;
    }, n.wbg.__wbg_instanceof_ArrayBuffer_e14585432e3737fc = function(e) {
      let t;
      try {
        t = e instanceof ArrayBuffer;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_Document_917b7ac52e42682e = function(e) {
      let t;
      try {
        t = e instanceof Document;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_DomException_ed1ccb7aaf39034c = function(e) {
      let t;
      try {
        t = e instanceof DOMException;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_Element_0af65443936d5154 = function(e) {
      let t;
      try {
        t = e instanceof Element;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_Error_4d54113b22d20306 = function(e) {
      let t;
      try {
        t = e instanceof Error;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_GpuAdapter_331cc7dcda68de8c = function(e) {
      let t;
      try {
        t = e instanceof GPUAdapter;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_GpuCanvasContext_4ea475a10f693c29 = function(e) {
      let t;
      try {
        t = e instanceof GPUCanvasContext;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_GpuOutOfMemoryError_37ed19bdb2cf4ac4 = function(e) {
      let t;
      try {
        t = e instanceof GPUOutOfMemoryError;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_GpuValidationError_6dca0186e4a231ce = function(e) {
      let t;
      try {
        t = e instanceof GPUValidationError;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_HtmlAnchorElement_1ff926b551076f86 = function(e) {
      let t;
      try {
        t = e instanceof HTMLAnchorElement;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_HtmlButtonElement_0def6a01e66b1942 = function(e) {
      let t;
      try {
        t = e instanceof HTMLButtonElement;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_HtmlCanvasElement_2ea67072a7624ac5 = function(e) {
      let t;
      try {
        t = e instanceof HTMLCanvasElement;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_HtmlElement_51378c201250b16c = function(e) {
      let t;
      try {
        t = e instanceof HTMLElement;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_HtmlInputElement_12d71bf2d15dd19e = function(e) {
      let t;
      try {
        t = e instanceof HTMLInputElement;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_MessageEvent_2e467ced55f682c9 = function(e) {
      let t;
      try {
        t = e instanceof MessageEvent;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_Object_7f2dcef8f78644a4 = function(e) {
      let t;
      try {
        t = e instanceof Object;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_ReadableStream_87eac785b90f3611 = function(e) {
      let t;
      try {
        t = e instanceof ReadableStream;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_ResizeObserverEntry_cb85a268a84783ba = function(e) {
      let t;
      try {
        t = e instanceof ResizeObserverEntry;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_ResizeObserverSize_4138fd53d59e1653 = function(e) {
      let t;
      try {
        t = e instanceof ResizeObserverSize;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_Response_f2cc20d9f7dfd644 = function(e) {
      let t;
      try {
        t = e instanceof Response;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_ShadowRoot_726578bcd7fa418a = function(e) {
      let t;
      try {
        t = e instanceof ShadowRoot;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_TypeError_896f9e5789610ec3 = function(e) {
      let t;
      try {
        t = e instanceof TypeError;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_Uint8Array_17156bcf118086a9 = function(e) {
      let t;
      try {
        t = e instanceof Uint8Array;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_WebGl2RenderingContext_2b6045efeb76568d = function(e) {
      let t;
      try {
        t = e instanceof WebGL2RenderingContext;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_instanceof_Window_def73ea0955fc569 = function(e) {
      let t;
      try {
        t = e instanceof Window;
      } catch {
        t = !1;
      }
      return t;
    }, n.wbg.__wbg_invalidateFramebuffer_83f643d2a4936456 = function() {
      return a(function(e, t, _) {
        e.invalidateFramebuffer(t >>> 0, _);
      }, arguments);
    }, n.wbg.__wbg_isArray_a1eab7e0d067391b = function(e) {
      return Array.isArray(e);
    }, n.wbg.__wbg_isComposing_36511555ff1869a4 = function(e) {
      return e.isComposing;
    }, n.wbg.__wbg_isComposing_6e36768c82fd5a4f = function(e) {
      return e.isComposing;
    }, n.wbg.__wbg_isSafeInteger_343e2beeeece1bb0 = function(e) {
      return Number.isSafeInteger(e);
    }, n.wbg.__wbg_isSecureContext_aedcf3816338189a = function(e) {
      return e.isSecureContext;
    }, n.wbg.__wbg_is_c7481c65e7e5df9e = function(e, t) {
      return Object.is(e, t);
    }, n.wbg.__wbg_item_aea4b8432b5457be = function(e, t) {
      const _ = e.item(t >>> 0);
      return g(_) ? 0 : l(_);
    }, n.wbg.__wbg_items_89c2afbece3a5d13 = function(e) {
      return e.items;
    }, n.wbg.__wbg_iterator_9a24c88df860dc65 = function() {
      return Symbol.iterator;
    }, n.wbg.__wbg_keyCode_237a8d1a040910b8 = function(e) {
      return e.keyCode;
    }, n.wbg.__wbg_key_7b5c6cb539be8e13 = function(e, t) {
      const _ = t.key, r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
      w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
    }, n.wbg.__wbg_label_7045a786095b1bab = function(e, t) {
      const _ = t.label, r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
      w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
    }, n.wbg.__wbg_lastModified_7a9e61b3961224b8 = function(e) {
      return e.lastModified;
    }, n.wbg.__wbg_left_e46801720267b66d = function(e) {
      return e.left;
    }, n.wbg.__wbg_length_1d5c829e9b2319d6 = function(e) {
      return e.length;
    }, n.wbg.__wbg_length_802483321c8130cf = function(e) {
      return e.length;
    }, n.wbg.__wbg_length_a446193dc22c12f8 = function(e) {
      return e.length;
    }, n.wbg.__wbg_length_cfc862ec0ccc7ca0 = function(e) {
      return e.length;
    }, n.wbg.__wbg_length_e2d2a49132c1b256 = function(e) {
      return e.length;
    }, n.wbg.__wbg_limits_563f98195b4aab75 = function(e) {
      return e.limits;
    }, n.wbg.__wbg_limits_6e5836ab03ee64b4 = function(e) {
      return e.limits;
    }, n.wbg.__wbg_linkProgram_067ee06739bdde81 = function(e, t) {
      e.linkProgram(t);
    }, n.wbg.__wbg_linkProgram_e002979fe36e5b2a = function(e, t) {
      e.linkProgram(t);
    }, n.wbg.__wbg_localStorage_1406c99c39728187 = function() {
      return a(function(e) {
        const t = e.localStorage;
        return g(t) ? 0 : l(t);
      }, arguments);
    }, n.wbg.__wbg_location_350d99456c2f3693 = function(e) {
      return e.location;
    }, n.wbg.__wbg_mapAsync_61fd3c4dd9f60c6d = function(e, t, _, r) {
      return e.mapAsync(t >>> 0, _, r);
    }, n.wbg.__wbg_matchMedia_bf8807a841d930c1 = function() {
      return a(function(e, t, _) {
        const r = e.matchMedia(u(t, _));
        return g(r) ? 0 : l(r);
      }, arguments);
    }, n.wbg.__wbg_matches_e9ca73fbf8a3a104 = function(e) {
      return e.matches;
    }, n.wbg.__wbg_maxBindGroups_30d01da76ad53580 = function(e) {
      return e.maxBindGroups;
    }, n.wbg.__wbg_maxBindingsPerBindGroup_3dcdeb4a7de67a4a = function(e) {
      return e.maxBindingsPerBindGroup;
    }, n.wbg.__wbg_maxBufferSize_a3c3e79851bb49a7 = function(e) {
      return e.maxBufferSize;
    }, n.wbg.__wbg_maxColorAttachmentBytesPerSample_61daf47ae1b88dc2 = function(e) {
      return e.maxColorAttachmentBytesPerSample;
    }, n.wbg.__wbg_maxColorAttachments_f8f65390ed7c3dcd = function(e) {
      return e.maxColorAttachments;
    }, n.wbg.__wbg_maxComputeInvocationsPerWorkgroup_dbfa932a2c3d9ca0 = function(e) {
      return e.maxComputeInvocationsPerWorkgroup;
    }, n.wbg.__wbg_maxComputeWorkgroupSizeX_2a7fdde2d850eb69 = function(e) {
      return e.maxComputeWorkgroupSizeX;
    }, n.wbg.__wbg_maxComputeWorkgroupSizeY_ae6eb3af592e045d = function(e) {
      return e.maxComputeWorkgroupSizeY;
    }, n.wbg.__wbg_maxComputeWorkgroupSizeZ_df6389c6ad61aa20 = function(e) {
      return e.maxComputeWorkgroupSizeZ;
    }, n.wbg.__wbg_maxComputeWorkgroupStorageSize_d090d78935189091 = function(e) {
      return e.maxComputeWorkgroupStorageSize;
    }, n.wbg.__wbg_maxComputeWorkgroupsPerDimension_5d5d832c21854769 = function(e) {
      return e.maxComputeWorkgroupsPerDimension;
    }, n.wbg.__wbg_maxDynamicStorageBuffersPerPipelineLayout_0d5102fd812fe086 = function(e) {
      return e.maxDynamicStorageBuffersPerPipelineLayout;
    }, n.wbg.__wbg_maxDynamicUniformBuffersPerPipelineLayout_fd6efab6fa18099a = function(e) {
      return e.maxDynamicUniformBuffersPerPipelineLayout;
    }, n.wbg.__wbg_maxSampledTexturesPerShaderStage_4ffa7a7339d366d7 = function(e) {
      return e.maxSampledTexturesPerShaderStage;
    }, n.wbg.__wbg_maxSamplersPerShaderStage_776dbf5a1fdc58b1 = function(e) {
      return e.maxSamplersPerShaderStage;
    }, n.wbg.__wbg_maxStorageBufferBindingSize_4a81009504bfcacd = function(e) {
      return e.maxStorageBufferBindingSize;
    }, n.wbg.__wbg_maxStorageBuffersPerShaderStage_772149c39281f13c = function(e) {
      return e.maxStorageBuffersPerShaderStage;
    }, n.wbg.__wbg_maxStorageTexturesPerShaderStage_181856fa7bd31bd2 = function(e) {
      return e.maxStorageTexturesPerShaderStage;
    }, n.wbg.__wbg_maxTextureArrayLayers_c50110b7591a08e7 = function(e) {
      return e.maxTextureArrayLayers;
    }, n.wbg.__wbg_maxTextureDimension1D_8886fff72f64818a = function(e) {
      return e.maxTextureDimension1D;
    }, n.wbg.__wbg_maxTextureDimension2D_0e30b1b618696302 = function(e) {
      return e.maxTextureDimension2D;
    }, n.wbg.__wbg_maxTextureDimension3D_2f567b561a18a953 = function(e) {
      return e.maxTextureDimension3D;
    }, n.wbg.__wbg_maxUniformBufferBindingSize_50a7723e932bbd63 = function(e) {
      return e.maxUniformBufferBindingSize;
    }, n.wbg.__wbg_maxUniformBuffersPerShaderStage_cfac0560ee2b33a2 = function(e) {
      return e.maxUniformBuffersPerShaderStage;
    }, n.wbg.__wbg_maxVertexAttributes_6bd060b2025920cc = function(e) {
      return e.maxVertexAttributes;
    }, n.wbg.__wbg_maxVertexBufferArrayStride_b3c77c1ff836be9f = function(e) {
      return e.maxVertexBufferArrayStride;
    }, n.wbg.__wbg_maxVertexBuffers_b4635256105b2915 = function(e) {
      return e.maxVertexBuffers;
    }, n.wbg.__wbg_message_49299ab153a3b589 = function(e, t) {
      const _ = t.message, r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
      w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
    }, n.wbg.__wbg_metaKey_0b25f7848e014cc8 = function(e) {
      return e.metaKey;
    }, n.wbg.__wbg_metaKey_e1dd47d709a80ce5 = function(e) {
      return e.metaKey;
    }, n.wbg.__wbg_minStorageBufferOffsetAlignment_989812b5a6a4b5e7 = function(e) {
      return e.minStorageBufferOffsetAlignment;
    }, n.wbg.__wbg_minUniformBufferOffsetAlignment_ff7899c34a8303e7 = function(e) {
      return e.minUniformBufferOffsetAlignment;
    }, n.wbg.__wbg_msCrypto_a61aeb35a24c1329 = function(e) {
      return e.msCrypto;
    }, n.wbg.__wbg_name_28c43f147574bf08 = function(e, t) {
      const _ = t.name, r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
      w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
    }, n.wbg.__wbg_navigator_0a9bf1120e24fec2 = function(e) {
      return e.navigator;
    }, n.wbg.__wbg_navigator_1577371c070c8947 = function(e) {
      return e.navigator;
    }, n.wbg.__wbg_new0_f788a2397c7ca929 = function() {
      return /* @__PURE__ */ new Date();
    }, n.wbg.__wbg_new_018dcc2d6c8c2f6a = function() {
      return a(function() {
        return new Headers();
      }, arguments);
    }, n.wbg.__wbg_new_23a2665fac83c611 = function(e, t) {
      try {
        var _ = { a: e, b: t }, r = (o, f) => {
          const i = _.a;
          _.a = 0;
          try {
            return ge(i, _.b, o, f);
          } finally {
            _.a = i;
          }
        };
        return new Promise(r);
      } finally {
        _.a = _.b = 0;
      }
    }, n.wbg.__wbg_new_405e22f390576ce2 = function() {
      return new Object();
    }, n.wbg.__wbg_new_46e8134c3341d05a = function() {
      return a(function() {
        return new FileReader();
      }, arguments);
    }, n.wbg.__wbg_new_49bbf669d24a0662 = function() {
      return a(function(e) {
        return new EncodedVideoChunk(e);
      }, arguments);
    }, n.wbg.__wbg_new_55df07bfefe09dd7 = function() {
      return new Error();
    }, n.wbg.__wbg_new_59a6be6d80c4dcbb = function() {
      return a(function(e) {
        return new VideoDecoder(e);
      }, arguments);
    }, n.wbg.__wbg_new_5f34cc0c99fcc488 = function() {
      return a(function(e) {
        return new ResizeObserver(e);
      }, arguments);
    }, n.wbg.__wbg_new_78feb108b6472713 = function() {
      return new Array();
    }, n.wbg.__wbg_new_80bf4ee74f41ff92 = function() {
      return a(function() {
        return new URLSearchParams();
      }, arguments);
    }, n.wbg.__wbg_new_9ffbe0a71eff35e3 = function() {
      return a(function(e, t) {
        return new URL(u(e, t));
      }, arguments);
    }, n.wbg.__wbg_new_a12002a7f91c75be = function(e) {
      return new Uint8Array(e);
    }, n.wbg.__wbg_new_a84b4fa486a621ad = function(e, t) {
      return new Intl.DateTimeFormat(e, t);
    }, n.wbg.__wbg_new_b08a00743b8ae2f3 = function(e, t) {
      return new TypeError(u(e, t));
    }, n.wbg.__wbg_new_c68d7209be747379 = function(e, t) {
      return new Error(u(e, t));
    }, n.wbg.__wbg_new_e25e5aab09ff45db = function() {
      return a(function() {
        return new AbortController();
      }, arguments);
    }, n.wbg.__wbg_new_ede6abc8359c5376 = function() {
      return new Error();
    }, n.wbg.__wbg_newnoargs_105ed471475aaf50 = function(e, t) {
      return new Function(u(e, t));
    }, n.wbg.__wbg_newwithbyteoffsetandlength_840f3c038856d4e9 = function(e, t, _) {
      return new Int8Array(e, t >>> 0, _ >>> 0);
    }, n.wbg.__wbg_newwithbyteoffsetandlength_999332a180064b59 = function(e, t, _) {
      return new Int32Array(e, t >>> 0, _ >>> 0);
    }, n.wbg.__wbg_newwithbyteoffsetandlength_d4a86622320ea258 = function(e, t, _) {
      return new Uint16Array(e, t >>> 0, _ >>> 0);
    }, n.wbg.__wbg_newwithbyteoffsetandlength_d97e637ebe145a9a = function(e, t, _) {
      return new Uint8Array(e, t >>> 0, _ >>> 0);
    }, n.wbg.__wbg_newwithbyteoffsetandlength_e6b7e69acd4c7354 = function(e, t, _) {
      return new Float32Array(e, t >>> 0, _ >>> 0);
    }, n.wbg.__wbg_newwithbyteoffsetandlength_f1dead44d1fc7212 = function(e, t, _) {
      return new Uint32Array(e, t >>> 0, _ >>> 0);
    }, n.wbg.__wbg_newwithbyteoffsetandlength_f254047f7e80e7ff = function(e, t, _) {
      return new Int16Array(e, t >>> 0, _ >>> 0);
    }, n.wbg.__wbg_newwithlength_a381634e90c276d4 = function(e) {
      return new Uint8Array(e >>> 0);
    }, n.wbg.__wbg_newwithrecordfromstrtoblobpromise_53d3e3611a048f1e = function() {
      return a(function(e) {
        return new ClipboardItem(e);
      }, arguments);
    }, n.wbg.__wbg_newwithstrandinit_06c535e0a867c635 = function() {
      return a(function(e, t, _) {
        return new Request(u(e, t), _);
      }, arguments);
    }, n.wbg.__wbg_newwithu8arraysequenceandoptions_068570c487f69127 = function() {
      return a(function(e, t) {
        return new Blob(e, t);
      }, arguments);
    }, n.wbg.__wbg_next_25feadfc0913fea9 = function(e) {
      return e.next;
    }, n.wbg.__wbg_next_6574e1a8a62d1055 = function() {
      return a(function(e) {
        return e.next();
      }, arguments);
    }, n.wbg.__wbg_node_905d3e251edff8a2 = function(e) {
      return e.node;
    }, n.wbg.__wbg_now_2c95c9de01293173 = function(e) {
      return e.now();
    }, n.wbg.__wbg_now_807e54c39636c349 = function() {
      return Date.now();
    }, n.wbg.__wbg_now_d18023d54d4e5500 = function(e) {
      return e.now();
    }, n.wbg.__wbg_observe_ed4adb1c245103c5 = function(e, t, _) {
      e.observe(t, _);
    }, n.wbg.__wbg_of_2eaf5a02d443ef03 = function(e) {
      return Array.of(e);
    }, n.wbg.__wbg_offsetTop_de8d0722bd1b211d = function(e) {
      return e.offsetTop;
    }, n.wbg.__wbg_ok_3aaf32d069979723 = function(e) {
      return e.ok;
    }, n.wbg.__wbg_open_6c3f5ef5a0204c5d = function() {
      return a(function(e, t, _, r, c) {
        const o = e.open(u(t, _), u(r, c));
        return g(o) ? 0 : l(o);
      }, arguments);
    }, n.wbg.__wbg_origin_7c5d649acdace3ea = function() {
      return a(function(e, t) {
        const _ = t.origin, r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
        w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
      }, arguments);
    }, n.wbg.__wbg_performance_7a3ffd0b17f663ad = function(e) {
      return e.performance;
    }, n.wbg.__wbg_performance_c185c0cdc2766575 = function(e) {
      const t = e.performance;
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_pixelStorei_6aba5d04cdcaeaf6 = function(e, t, _) {
      e.pixelStorei(t >>> 0, _);
    }, n.wbg.__wbg_pixelStorei_c8520e4b46f4a973 = function(e, t, _) {
      e.pixelStorei(t >>> 0, _);
    }, n.wbg.__wbg_polygonOffset_773fe0017b2c8f51 = function(e, t, _) {
      e.polygonOffset(t, _);
    }, n.wbg.__wbg_polygonOffset_8c11c066486216c4 = function(e, t, _) {
      e.polygonOffset(t, _);
    }, n.wbg.__wbg_popErrorScope_4e8ec39111c15bed = function(e) {
      return e.popErrorScope();
    }, n.wbg.__wbg_port_008e0061f421df1d = function() {
      return a(function(e, t) {
        const _ = t.port, r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
        w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
      }, arguments);
    }, n.wbg.__wbg_preventDefault_c2314fd813c02b3c = function(e) {
      e.preventDefault();
    }, n.wbg.__wbg_process_dc0fbacc7c1c06f7 = function(e) {
      return e.process;
    }, n.wbg.__wbg_protocol_faa0494a9b2554cb = function() {
      return a(function(e, t) {
        const _ = t.protocol, r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
        w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
      }, arguments);
    }, n.wbg.__wbg_pushErrorScope_506d26ea9c804e6f = function(e, t) {
      e.pushErrorScope(pe[t]);
    }, n.wbg.__wbg_pushState_d132f15566570786 = function() {
      return a(function(e, t, _, r, c, o) {
        e.pushState(t, u(_, r), c === 0 ? void 0 : u(c, o));
      }, arguments);
    }, n.wbg.__wbg_push_737cfc8c1432c2c6 = function(e, t) {
      return e.push(t);
    }, n.wbg.__wbg_queryCounterEXT_7aed85645b7ec1da = function(e, t, _) {
      e.queryCounterEXT(t, _ >>> 0);
    }, n.wbg.__wbg_querySelectorAll_40998fd748f057ef = function() {
      return a(function(e, t, _) {
        return e.querySelectorAll(u(t, _));
      }, arguments);
    }, n.wbg.__wbg_querySelector_c69f8b573958906b = function() {
      return a(function(e, t, _) {
        const r = e.querySelector(u(t, _));
        return g(r) ? 0 : l(r);
      }, arguments);
    }, n.wbg.__wbg_queueMicrotask_97d92b4fcc8a61c5 = function(e) {
      queueMicrotask(e);
    }, n.wbg.__wbg_queueMicrotask_d3219def82552485 = function(e) {
      return e.queueMicrotask;
    }, n.wbg.__wbg_queue_0ffbb97537a0c4ed = function(e) {
      return e.queue;
    }, n.wbg.__wbg_randomFillSync_ac0988aba3254290 = function() {
      return a(function(e, t) {
        e.randomFillSync(t);
      }, arguments);
    }, n.wbg.__wbg_readAsArrayBuffer_e51cb3c4fcc962de = function() {
      return a(function(e, t) {
        e.readAsArrayBuffer(t);
      }, arguments);
    }, n.wbg.__wbg_readBuffer_1c35b1e4939f881d = function(e, t) {
      e.readBuffer(t >>> 0);
    }, n.wbg.__wbg_readPixels_51a0c02cdee207a5 = function() {
      return a(function(e, t, _, r, c, o, f, i) {
        e.readPixels(t, _, r, c, o >>> 0, f >>> 0, i);
      }, arguments);
    }, n.wbg.__wbg_readPixels_a6cbb21794452142 = function() {
      return a(function(e, t, _, r, c, o, f, i) {
        e.readPixels(t, _, r, c, o >>> 0, f >>> 0, i);
      }, arguments);
    }, n.wbg.__wbg_readPixels_cd64c5a7b0343355 = function() {
      return a(function(e, t, _, r, c, o, f, i) {
        e.readPixels(t, _, r, c, o >>> 0, f >>> 0, i);
      }, arguments);
    }, n.wbg.__wbg_read_a2434af1186cb56c = function(e) {
      return e.read();
    }, n.wbg.__wbg_releaseLock_091899af97991d2e = function(e) {
      e.releaseLock();
    }, n.wbg.__wbg_removeEventListener_056dfe8c3d6c58f9 = function() {
      return a(function(e, t, _, r) {
        e.removeEventListener(u(t, _), r);
      }, arguments);
    }, n.wbg.__wbg_remove_e2d2659f3128c045 = function(e) {
      e.remove();
    }, n.wbg.__wbg_renderbufferStorageMultisample_13fbd5e58900c6fe = function(e, t, _, r, c, o) {
      e.renderbufferStorageMultisample(t >>> 0, _, r >>> 0, c, o);
    }, n.wbg.__wbg_renderbufferStorage_73e01ea83b8afab4 = function(e, t, _, r, c) {
      e.renderbufferStorage(t >>> 0, _ >>> 0, r, c);
    }, n.wbg.__wbg_renderbufferStorage_f010012bd3566942 = function(e, t, _, r, c) {
      e.renderbufferStorage(t >>> 0, _ >>> 0, r, c);
    }, n.wbg.__wbg_replaceState_79f3b896be12c919 = function() {
      return a(function(e, t, _, r, c, o) {
        e.replaceState(t, u(_, r), c === 0 ? void 0 : u(c, o));
      }, arguments);
    }, n.wbg.__wbg_requestAdapter_85a0526011ba069a = function(e) {
      return e.requestAdapter();
    }, n.wbg.__wbg_requestAdapter_f09d28b3f37de26c = function(e, t) {
      return e.requestAdapter(t);
    }, n.wbg.__wbg_requestAnimationFrame_d7fd890aaefc3246 = function() {
      return a(function(e, t) {
        return e.requestAnimationFrame(t);
      }, arguments);
    }, n.wbg.__wbg_requestDevice_51509dadc50b2e9d = function(e, t) {
      return e.requestDevice(t);
    }, n.wbg.__wbg_require_60cc747a6bc5215a = function() {
      return a(function() {
        return module.require;
      }, arguments);
    }, n.wbg.__wbg_reset_09739ecbd10cf8be = function() {
      return a(function(e) {
        e.reset();
      }, arguments);
    }, n.wbg.__wbg_resolve_4851785c9c5f573d = function(e) {
      return Promise.resolve(e);
    }, n.wbg.__wbg_resolvedOptions_d495c21c27a8f865 = function(e) {
      return e.resolvedOptions();
    }, n.wbg.__wbg_respond_1f279fa9f8edcb1c = function() {
      return a(function(e, t) {
        e.respond(t >>> 0);
      }, arguments);
    }, n.wbg.__wbg_result_dadbdcc801180072 = function() {
      return a(function(e) {
        return e.result;
      }, arguments);
    }, n.wbg.__wbg_right_54416a875852cab1 = function(e) {
      return e.right;
    }, n.wbg.__wbg_samplerParameterf_909baf50360c94d4 = function(e, t, _, r) {
      e.samplerParameterf(t, _ >>> 0, r);
    }, n.wbg.__wbg_samplerParameteri_d5c292172718da63 = function(e, t, _, r) {
      e.samplerParameteri(t, _ >>> 0, r);
    }, n.wbg.__wbg_scissor_e917a332f67a5d30 = function(e, t, _, r, c) {
      e.scissor(t, _, r, c);
    }, n.wbg.__wbg_scissor_eb177ca33bf24a44 = function(e, t, _, r, c) {
      e.scissor(t, _, r, c);
    }, n.wbg.__wbg_searchParams_da316d96d88b6d30 = function(e) {
      return e.searchParams;
    }, n.wbg.__wbg_search_c1c3bfbeadd96c47 = function() {
      return a(function(e, t) {
        const _ = t.search, r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
        w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
      }, arguments);
    }, n.wbg.__wbg_setAttribute_2704501201f15687 = function() {
      return a(function(e, t, _, r, c) {
        e.setAttribute(u(t, _), u(r, c));
      }, arguments);
    }, n.wbg.__wbg_setBindGroup_a81ce7b3934585bf = function(e, t, _) {
      e.setBindGroup(t >>> 0, _);
    }, n.wbg.__wbg_setBindGroup_bb0c2c05b7c49401 = function() {
      return a(function(e, t, _, r, c, o, f) {
        e.setBindGroup(t >>> 0, _, R(r, c), o, f >>> 0);
      }, arguments);
    }, n.wbg.__wbg_setIndexBuffer_0487a271efcfe0ac = function(e, t, _, r) {
      e.setIndexBuffer(t, z[_], r);
    }, n.wbg.__wbg_setIndexBuffer_97fb24e7cc5b24c0 = function(e, t, _, r, c) {
      e.setIndexBuffer(t, z[_], r, c);
    }, n.wbg.__wbg_setItem_212ecc915942ab0a = function() {
      return a(function(e, t, _, r, c) {
        e.setItem(u(t, _), u(r, c));
      }, arguments);
    }, n.wbg.__wbg_setPipeline_78f8f6d440dddd25 = function(e, t) {
      e.setPipeline(t);
    }, n.wbg.__wbg_setProperty_f2cf326652b9a713 = function() {
      return a(function(e, t, _, r, c) {
        e.setProperty(u(t, _), u(r, c));
      }, arguments);
    }, n.wbg.__wbg_setScissorRect_4db4ebbc562e249e = function(e, t, _, r, c) {
      e.setScissorRect(t >>> 0, _ >>> 0, r >>> 0, c >>> 0);
    }, n.wbg.__wbg_setTimeout_73ce8df12de4f2f2 = function(e, t) {
      return setTimeout(e, t);
    }, n.wbg.__wbg_setTimeout_f2fe5af8e3debeb3 = function() {
      return a(function(e, t, _) {
        return e.setTimeout(t, _);
      }, arguments);
    }, n.wbg.__wbg_setVertexBuffer_b0d3128a04bfd766 = function(e, t, _, r, c) {
      e.setVertexBuffer(t >>> 0, _, r, c);
    }, n.wbg.__wbg_setVertexBuffer_edbff6ddb5055174 = function(e, t, _, r) {
      e.setVertexBuffer(t >>> 0, _, r);
    }, n.wbg.__wbg_setViewport_b84ead683cd03d3e = function(e, t, _, r, c, o, f) {
      e.setViewport(t, _, r, c, o, f);
    }, n.wbg.__wbg_set_11cd83f45504cedf = function() {
      return a(function(e, t, _, r, c) {
        e.set(u(t, _), u(r, c));
      }, arguments);
    }, n.wbg.__wbg_set_3f1d0b984ed272ed = function(e, t, _) {
      e[t] = _;
    }, n.wbg.__wbg_set_65595bdd868b3009 = function(e, t, _) {
      e.set(t, _ >>> 0);
    }, n.wbg.__wbg_set_bb8cecf6a62b9f46 = function() {
      return a(function(e, t, _) {
        return Reflect.set(e, t, _);
      }, arguments);
    }, n.wbg.__wbg_set_d254161c469cf8d7 = function(e, t, _, r, c) {
      e.set(u(t, _), u(r, c));
    }, n.wbg.__wbg_seta_721deab95e136b71 = function(e, t) {
      e.a = t;
    }, n.wbg.__wbg_setaccept_ff32b9ffcfbd061d = function(e, t, _) {
      e.accept = u(t, _);
    }, n.wbg.__wbg_setaccess_b20bfa3ec6b65d05 = function(e, t) {
      e.access = Ie[t];
    }, n.wbg.__wbg_setaddressmodeu_9c0b2104a94d10f3 = function(e, t) {
      e.addressModeU = L[t];
    }, n.wbg.__wbg_setaddressmodev_a9bedc188ff29608 = function(e, t) {
      e.addressModeV = L[t];
    }, n.wbg.__wbg_setaddressmodew_5774889145ce3789 = function(e, t) {
      e.addressModeW = L[t];
    }, n.wbg.__wbg_setalpha_2c7bdc9da833b6c2 = function(e, t) {
      e.alpha = t;
    }, n.wbg.__wbg_setalphamode_fc3528d234b1fefa = function(e, t) {
      e.alphaMode = le[t];
    }, n.wbg.__wbg_setalphatocoverageenabled_314ce1ca1759b395 = function(e, t) {
      e.alphaToCoverageEnabled = t !== 0;
    }, n.wbg.__wbg_setarraylayercount_3c7942d623042874 = function(e, t) {
      e.arrayLayerCount = t >>> 0;
    }, n.wbg.__wbg_setarraystride_4b36d0822dea74a8 = function(e, t) {
      e.arrayStride = t;
    }, n.wbg.__wbg_setaspect_48152f4e4f8231ae = function(e, t) {
      e.aspect = J[t];
    }, n.wbg.__wbg_setaspect_f06e234d0aacd1a6 = function(e, t) {
      e.aspect = J[t];
    }, n.wbg.__wbg_setattributes_382cc084e6792c33 = function(e, t) {
      e.attributes = t;
    }, n.wbg.__wbg_setautofocus_6ca6f0ab5a566c21 = function() {
      return a(function(e, t) {
        e.autofocus = t !== 0;
      }, arguments);
    }, n.wbg.__wbg_setb_f53c2f10173c804f = function(e, t) {
      e.b = t;
    }, n.wbg.__wbg_setbasearraylayer_a5b968338c5c56b6 = function(e, t) {
      e.baseArrayLayer = t >>> 0;
    }, n.wbg.__wbg_setbasemiplevel_e3288c2d851da708 = function(e, t) {
      e.baseMipLevel = t >>> 0;
    }, n.wbg.__wbg_setbeginningofpasswriteindex_35dcbf135e4f9d61 = function(e, t) {
      e.beginningOfPassWriteIndex = t >>> 0;
    }, n.wbg.__wbg_setbindgrouplayouts_8de6e109dd34a448 = function(e, t) {
      e.bindGroupLayouts = t;
    }, n.wbg.__wbg_setbinding_5276d6202fceba46 = function(e, t) {
      e.binding = t >>> 0;
    }, n.wbg.__wbg_setbinding_9e9ed8b6e1418176 = function(e, t) {
      e.binding = t >>> 0;
    }, n.wbg.__wbg_setblend_6828ff186670f414 = function(e, t) {
      e.blend = t;
    }, n.wbg.__wbg_setbody_5923b78a95eedf29 = function(e, t) {
      e.body = t;
    }, n.wbg.__wbg_setbox_2786f3ccea97cac4 = function(e, t) {
      e.box = Le[t];
    }, n.wbg.__wbg_setbuffer_1acdac44d9638973 = function(e, t) {
      e.buffer = t;
    }, n.wbg.__wbg_setbuffer_1d16f319d6410e50 = function(e, t) {
      e.buffer = t;
    }, n.wbg.__wbg_setbuffer_74b7b0adf855cf1a = function(e, t) {
      e.buffer = t;
    }, n.wbg.__wbg_setbuffers_53e83b7c7a5c95aa = function(e, t) {
      e.buffers = t;
    }, n.wbg.__wbg_setbytesperrow_9249690c44f83135 = function(e, t) {
      e.bytesPerRow = t >>> 0;
    }, n.wbg.__wbg_setbytesperrow_ffe6655e20551429 = function(e, t) {
      e.bytesPerRow = t >>> 0;
    }, n.wbg.__wbg_setcache_12f17c3a980650e4 = function(e, t) {
      e.cache = Re[t];
    }, n.wbg.__wbg_setclearvalue_f82fff01ed0b5c35 = function(e, t) {
      e.clearValue = t;
    }, n.wbg.__wbg_setcode_6b6ad02fc1705aa2 = function(e, t, _) {
      e.code = u(t, _);
    }, n.wbg.__wbg_setcodec_4711d15b4dc250aa = function(e, t, _) {
      e.codec = u(t, _);
    }, n.wbg.__wbg_setcodedheight_ece3ee60aa2f36d0 = function(e, t) {
      e.codedHeight = t >>> 0;
    }, n.wbg.__wbg_setcodedwidth_54996c33ecba05cf = function(e, t) {
      e.codedWidth = t >>> 0;
    }, n.wbg.__wbg_setcolor_0df2c5f47a951ac1 = function(e, t) {
      e.color = t;
    }, n.wbg.__wbg_setcolorattachments_de625dd9a4850a13 = function(e, t) {
      e.colorAttachments = t;
    }, n.wbg.__wbg_setcompare_1b67d8112d05628e = function(e, t) {
      e.compare = O[t];
    }, n.wbg.__wbg_setcompare_8fbddcdd4781f49a = function(e, t) {
      e.compare = O[t];
    }, n.wbg.__wbg_setcount_e8b681b1185cf5da = function(e, t) {
      e.count = t >>> 0;
    }, n.wbg.__wbg_setcredentials_c3a22f1cd105a2c6 = function(e, t) {
      e.credentials = Ee[t];
    }, n.wbg.__wbg_setcullmode_74bc6eaab528c94b = function(e, t) {
      e.cullMode = me[t];
    }, n.wbg.__wbg_setdata_5aa9939c8f2f7291 = function(e, t) {
      e.data = t;
    }, n.wbg.__wbg_setdepthbias_cdcc35c6971d19cd = function(e, t) {
      e.depthBias = t;
    }, n.wbg.__wbg_setdepthbiasclamp_57801e26f66496d9 = function(e, t) {
      e.depthBiasClamp = t;
    }, n.wbg.__wbg_setdepthbiasslopescale_81699f807bd5a647 = function(e, t) {
      e.depthBiasSlopeScale = t;
    }, n.wbg.__wbg_setdepthclearvalue_9801aa9eff7645df = function(e, t) {
      e.depthClearValue = t;
    }, n.wbg.__wbg_setdepthcompare_53d249a136855bd8 = function(e, t) {
      e.depthCompare = O[t];
    }, n.wbg.__wbg_setdepthfailop_2e4767995acd4c0a = function(e, t) {
      e.depthFailOp = W[t];
    }, n.wbg.__wbg_setdepthloadop_af0b0f05e83f6571 = function(e, t) {
      e.depthLoadOp = G[t];
    }, n.wbg.__wbg_setdepthorarraylayers_5d480fc05509ea0c = function(e, t) {
      e.depthOrArrayLayers = t >>> 0;
    }, n.wbg.__wbg_setdepthreadonly_a7b7224074e024d3 = function(e, t) {
      e.depthReadOnly = t !== 0;
    }, n.wbg.__wbg_setdepthstencil_2bb2fcea55783858 = function(e, t) {
      e.depthStencil = t;
    }, n.wbg.__wbg_setdepthstencilattachment_dcbd5b74e4350e16 = function(e, t) {
      e.depthStencilAttachment = t;
    }, n.wbg.__wbg_setdepthstoreop_40dfd99c7e42f894 = function(e, t) {
      e.depthStoreOp = V[t];
    }, n.wbg.__wbg_setdepthwriteenabled_4368a2fe5d258cb0 = function(e, t) {
      e.depthWriteEnabled = t !== 0;
    }, n.wbg.__wbg_setdescription_d1194da3c0c55b20 = function(e, t) {
      e.description = t;
    }, n.wbg.__wbg_setdevice_d372d6aa06f20cae = function(e, t) {
      e.device = t;
    }, n.wbg.__wbg_setdimension_268b2b7bfc3e2bb8 = function(e, t) {
      e.dimension = Ae[t];
    }, n.wbg.__wbg_setdimension_359b229ea1b67a77 = function(e, t) {
      e.dimension = q[t];
    }, n.wbg.__wbg_setdownload_2af133b91eb04665 = function(e, t, _) {
      e.download = u(t, _);
    }, n.wbg.__wbg_setdstfactor_96e73b9eaedeb23e = function(e, t) {
      e.dstFactor = Y[t];
    }, n.wbg.__wbg_setduration_f91e800f7c5f3e7b = function(e, t) {
      e.duration = t;
    }, n.wbg.__wbg_setendofpasswriteindex_71e7659a9d2a9d60 = function(e, t) {
      e.endOfPassWriteIndex = t >>> 0;
    }, n.wbg.__wbg_setentries_5941f16619f54d42 = function(e, t) {
      e.entries = t;
    }, n.wbg.__wbg_setentries_97a6ad10aa7fa4d1 = function(e, t) {
      e.entries = t;
    }, n.wbg.__wbg_setentrypoint_a858879f63ec2236 = function(e, t, _) {
      e.entryPoint = u(t, _);
    }, n.wbg.__wbg_setentrypoint_a8ce0b22c20548b0 = function(e, t, _) {
      e.entryPoint = u(t, _);
    }, n.wbg.__wbg_seterror_4ce8a2ad7ee75507 = function(e, t) {
      e.error = t;
    }, n.wbg.__wbg_setfailop_d55bda42958efa98 = function(e, t) {
      e.failOp = W[t];
    }, n.wbg.__wbg_setflipy_bd2d5ada3a89715f = function(e, t) {
      e.flipY = t !== 0;
    }, n.wbg.__wbg_setformat_69ba449c0e080708 = function(e, t) {
      e.format = A[t];
    }, n.wbg.__wbg_setformat_713b9e90b13df6aa = function(e, t) {
      e.format = De[t];
    }, n.wbg.__wbg_setformat_76bcf93126fcdc9d = function(e, t) {
      e.format = A[t];
    }, n.wbg.__wbg_setformat_970299d3f84a8f20 = function(e, t) {
      e.format = A[t];
    }, n.wbg.__wbg_setformat_a8a60feb127f0971 = function(e, t) {
      e.format = A[t];
    }, n.wbg.__wbg_setformat_beb33029aea4cf8e = function(e, t) {
      e.format = A[t];
    }, n.wbg.__wbg_setformat_f6ec428901712514 = function(e, t) {
      e.format = A[t];
    }, n.wbg.__wbg_setfragment_0f23dfb67b3e84ab = function(e, t) {
      e.fragment = t;
    }, n.wbg.__wbg_setfrontface_c80337acd997f8c6 = function(e, t) {
      e.frontFace = ye[t];
    }, n.wbg.__wbg_setg_7eb6b5e67456a09e = function(e, t) {
      e.g = t;
    }, n.wbg.__wbg_sethardwareacceleration_15f40e3173e2e8b7 = function(e, t) {
      e.hardwareAcceleration = Be[t];
    }, n.wbg.__wbg_sethasdynamicoffset_b34dfdba692a7959 = function(e, t) {
      e.hasDynamicOffset = t !== 0;
    }, n.wbg.__wbg_setheaders_834c0bdb6a8949ad = function(e, t) {
      e.headers = t;
    }, n.wbg.__wbg_setheight_433680330c9420c3 = function(e, t) {
      e.height = t >>> 0;
    }, n.wbg.__wbg_setheight_a7439239ff109215 = function(e, t) {
      e.height = t >>> 0;
    }, n.wbg.__wbg_setheight_da683a33fa99843c = function(e, t) {
      e.height = t >>> 0;
    }, n.wbg.__wbg_sethref_5d8095525d8737d4 = function(e, t, _) {
      e.href = u(t, _);
    }, n.wbg.__wbg_setid_d1300d55a412791b = function(e, t, _) {
      e.id = u(t, _);
    }, n.wbg.__wbg_setinnerHTML_31bde41f835786f7 = function(e, t, _) {
      e.innerHTML = u(t, _);
    }, n.wbg.__wbg_setinnerText_b11978b8158639c4 = function(e, t, _) {
      e.innerText = u(t, _);
    }, n.wbg.__wbg_setintegrity_564a2397cf837760 = function(e, t, _) {
      e.integrity = u(t, _);
    }, n.wbg.__wbg_setlabel_1df8805b2aad72d7 = function(e, t, _) {
      e.label = u(t, _);
    }, n.wbg.__wbg_setlabel_460a52030d604dd7 = function(e, t, _) {
      e.label = u(t, _);
    }, n.wbg.__wbg_setlabel_57008c2e11276b5e = function(e, t, _) {
      e.label = u(t, _);
    }, n.wbg.__wbg_setlabel_66db708c47a585b2 = function(e, t, _) {
      e.label = u(t, _);
    }, n.wbg.__wbg_setlabel_68cd87490e02e1de = function(e, t, _) {
      e.label = u(t, _);
    }, n.wbg.__wbg_setlabel_76b058f0224eb49e = function(e, t, _) {
      e.label = u(t, _);
    }, n.wbg.__wbg_setlabel_89c327fa94d8076b = function(e, t, _) {
      e.label = u(t, _);
    }, n.wbg.__wbg_setlabel_969d6f8279c74456 = function(e, t, _) {
      e.label = u(t, _);
    }, n.wbg.__wbg_setlabel_a0c41069e355431e = function(e, t, _) {
      e.label = u(t, _);
    }, n.wbg.__wbg_setlabel_c14214ffbf6e5c4a = function(e, t, _) {
      e.label = u(t, _);
    }, n.wbg.__wbg_setlabel_ca2c132e2b646244 = function(e, t, _) {
      e.label = u(t, _);
    }, n.wbg.__wbg_setlabel_e6fab993e10f1dd3 = function(e, t, _) {
      e.label = u(t, _);
    }, n.wbg.__wbg_setlabel_f9a45e9ef445b781 = function(e, t, _) {
      e.label = u(t, _);
    }, n.wbg.__wbg_setlayout_67a29edc6247c437 = function(e, t) {
      e.layout = t;
    }, n.wbg.__wbg_setlayout_758d30edbd6ea91c = function(e, t) {
      e.layout = t;
    }, n.wbg.__wbg_setloadop_5644a3bf70f4f76c = function(e, t) {
      e.loadOp = G[t];
    }, n.wbg.__wbg_setlodmaxclamp_d80060a9922f9fe3 = function(e, t) {
      e.lodMaxClamp = t;
    }, n.wbg.__wbg_setlodminclamp_bee469ae69d038f0 = function(e, t) {
      e.lodMinClamp = t;
    }, n.wbg.__wbg_setmagfilter_f50646cfdc01700d = function(e, t) {
      e.magFilter = $[t];
    }, n.wbg.__wbg_setmappedatcreation_0dc5796d4e90ab4b = function(e, t) {
      e.mappedAtCreation = t !== 0;
    }, n.wbg.__wbg_setmask_800b15ad78613be8 = function(e, t) {
      e.mask = t >>> 0;
    }, n.wbg.__wbg_setmaxanisotropy_83ac2a8bef9f9ec8 = function(e, t) {
      e.maxAnisotropy = t;
    }, n.wbg.__wbg_setmethod_3c5280fe5d890842 = function(e, t, _) {
      e.method = u(t, _);
    }, n.wbg.__wbg_setminbindingsize_20ca594cd6d93818 = function(e, t) {
      e.minBindingSize = t;
    }, n.wbg.__wbg_setminfilter_8ffc9e1ac6b4149f = function(e, t) {
      e.minFilter = $[t];
    }, n.wbg.__wbg_setmiplevel_4e2a9d8b9b47208e = function(e, t) {
      e.mipLevel = t >>> 0;
    }, n.wbg.__wbg_setmiplevel_6f507098915add77 = function(e, t) {
      e.mipLevel = t >>> 0;
    }, n.wbg.__wbg_setmiplevelcount_5e59806cbcf116e9 = function(e, t) {
      e.mipLevelCount = t >>> 0;
    }, n.wbg.__wbg_setmiplevelcount_f896fe8cbb669df2 = function(e, t) {
      e.mipLevelCount = t >>> 0;
    }, n.wbg.__wbg_setmipmapfilter_037575f2e647f024 = function(e, t) {
      e.mipmapFilter = he[t];
    }, n.wbg.__wbg_setmode_5dc300b865044b65 = function(e, t) {
      e.mode = ke[t];
    }, n.wbg.__wbg_setmodule_4c73bb35cb0beb0b = function(e, t) {
      e.module = t;
    }, n.wbg.__wbg_setmodule_ca21130b3f66ea5d = function(e, t) {
      e.module = t;
    }, n.wbg.__wbg_setmultiple_1b3b3f243cda56b2 = function(e, t) {
      e.multiple = t !== 0;
    }, n.wbg.__wbg_setmultisample_4f57dcaa4144a62f = function(e, t) {
      e.multisample = t;
    }, n.wbg.__wbg_setmultisampled_0bb9fc1b577bf11a = function(e, t) {
      e.multisampled = t !== 0;
    }, n.wbg.__wbg_setoffset_67ee100819c122f2 = function(e, t) {
      e.offset = t;
    }, n.wbg.__wbg_setoffset_721180fefc9711a9 = function(e, t) {
      e.offset = t;
    }, n.wbg.__wbg_setoffset_a8194a4fcfff8910 = function(e, t) {
      e.offset = t;
    }, n.wbg.__wbg_setoffset_d37e5fa34e9ded2e = function(e, t) {
      e.offset = t;
    }, n.wbg.__wbg_setonce_0cb80aea26303a35 = function(e, t) {
      e.once = t !== 0;
    }, n.wbg.__wbg_setonclick_d0c6e25a994463d9 = function(e, t) {
      e.onclick = t;
    }, n.wbg.__wbg_setonload_1302417ca59f658b = function(e, t) {
      e.onload = t;
    }, n.wbg.__wbg_setonuncapturederror_3449cdb695f16431 = function(e, t) {
      e.onuncapturederror = t;
    }, n.wbg.__wbg_setoperation_173958551af7f4f2 = function(e, t) {
      e.operation = se[t];
    }, n.wbg.__wbg_setoptimizeforlatency_0bccf9d26e3e2224 = function(e, t) {
      e.optimizeForLatency = t !== 0;
    }, n.wbg.__wbg_setorigin_13b56d848aada680 = function(e, t) {
      e.origin = t;
    }, n.wbg.__wbg_setorigin_e26b73e77b3e275d = function(e, t) {
      e.origin = t;
    }, n.wbg.__wbg_setorigin_f72dc9fdb8a63f0c = function(e, t) {
      e.origin = t;
    }, n.wbg.__wbg_setoutput_ff9dc597ad64d749 = function(e, t) {
      e.output = t;
    }, n.wbg.__wbg_setpassop_070547fd6160a00d = function(e, t) {
      e.passOp = W[t];
    }, n.wbg.__wbg_setpowerpreference_1f3351e5d2acf765 = function(e, t) {
      e.powerPreference = xe[t];
    }, n.wbg.__wbg_setpremultipliedalpha_de7d1cc1ae4ca1a8 = function(e, t) {
      e.premultipliedAlpha = t !== 0;
    }, n.wbg.__wbg_setprimitive_ee18492ab93953bc = function(e, t) {
      e.primitive = t;
    }, n.wbg.__wbg_setqueryset_3b14f95f9bd114db = function(e, t) {
      e.querySet = t;
    }, n.wbg.__wbg_setr_a4e2f60e3466da86 = function(e, t) {
      e.r = t;
    }, n.wbg.__wbg_setredirect_40e6a7f717a2f86a = function(e, t) {
      e.redirect = Ce[t];
    }, n.wbg.__wbg_setreferrer_fea46c1230e5e29a = function(e, t, _) {
      e.referrer = u(t, _);
    }, n.wbg.__wbg_setreferrerpolicy_b73612479f761b6f = function(e, t) {
      e.referrerPolicy = Me[t];
    }, n.wbg.__wbg_setrequiredfeatures_fc44bc3433300ee3 = function(e, t) {
      e.requiredFeatures = t;
    }, n.wbg.__wbg_setresolvetarget_c4b519cab7eb42b7 = function(e, t) {
      e.resolveTarget = t;
    }, n.wbg.__wbg_setresource_1659f5a29a2e0541 = function(e, t) {
      e.resource = t;
    }, n.wbg.__wbg_setrowsperimage_53ed2c633b1adfcc = function(e, t) {
      e.rowsPerImage = t >>> 0;
    }, n.wbg.__wbg_setrowsperimage_b16fc77b3e7f5230 = function(e, t) {
      e.rowsPerImage = t >>> 0;
    }, n.wbg.__wbg_setsamplecount_e88d044f067a2241 = function(e, t) {
      e.sampleCount = t >>> 0;
    }, n.wbg.__wbg_setsampler_a778272f31d31ce5 = function(e, t) {
      e.sampler = t;
    }, n.wbg.__wbg_setsampletype_c0e25b966db74174 = function(e, t) {
      e.sampleType = Te[t];
    }, n.wbg.__wbg_setshaderlocation_985046f48e76573f = function(e, t) {
      e.shaderLocation = t >>> 0;
    }, n.wbg.__wbg_setsignal_75b21ef3a81de905 = function(e, t) {
      e.signal = t;
    }, n.wbg.__wbg_setsize_23676383c9c0732f = function(e, t) {
      e.size = t;
    }, n.wbg.__wbg_setsize_51616eaf8209c58b = function(e, t) {
      e.size = t;
    }, n.wbg.__wbg_setsize_5878aadcd23673cf = function(e, t) {
      e.size = t;
    }, n.wbg.__wbg_setsource_b1e66b73aa8a4ebc = function(e, t) {
      e.source = t;
    }, n.wbg.__wbg_setsrcfactor_04ce8874f1bff5a8 = function(e, t) {
      e.srcFactor = Y[t];
    }, n.wbg.__wbg_setstencilback_4b20ecfcd4c4816a = function(e, t) {
      e.stencilBack = t;
    }, n.wbg.__wbg_setstencilclearvalue_7ba82e1993788f37 = function(e, t) {
      e.stencilClearValue = t >>> 0;
    }, n.wbg.__wbg_setstencilfront_1ca3b695f7c42f6a = function(e, t) {
      e.stencilFront = t;
    }, n.wbg.__wbg_setstencilloadop_b65c60a0077315cd = function(e, t) {
      e.stencilLoadOp = G[t];
    }, n.wbg.__wbg_setstencilreadmask_4f5b98747141e796 = function(e, t) {
      e.stencilReadMask = t >>> 0;
    }, n.wbg.__wbg_setstencilreadonly_9006a99a91d198e9 = function(e, t) {
      e.stencilReadOnly = t !== 0;
    }, n.wbg.__wbg_setstencilstoreop_4f00c5eca345c145 = function(e, t) {
      e.stencilStoreOp = V[t];
    }, n.wbg.__wbg_setstencilwritemask_e37a7214d84ace99 = function(e, t) {
      e.stencilWriteMask = t >>> 0;
    }, n.wbg.__wbg_setstepmode_7d58d75e6547a7a6 = function(e, t) {
      e.stepMode = Pe[t];
    }, n.wbg.__wbg_setstoragetexture_2987339fec972d54 = function(e, t) {
      e.storageTexture = t;
    }, n.wbg.__wbg_setstoreop_c62dd050b5806095 = function(e, t) {
      e.storeOp = V[t];
    }, n.wbg.__wbg_setstripindexformat_3e4893749b3f00b0 = function(e, t) {
      e.stripIndexFormat = z[t];
    }, n.wbg.__wbg_settabIndex_31adfec3c7eafbce = function(e, t) {
      e.tabIndex = t;
    }, n.wbg.__wbg_settargets_0ef1de33af7253a6 = function(e, t) {
      e.targets = t;
    }, n.wbg.__wbg_settexture_2553e9c3ae6f7687 = function(e, t) {
      e.texture = t;
    }, n.wbg.__wbg_settexture_28ef6c52713faba9 = function(e, t) {
      e.texture = t;
    }, n.wbg.__wbg_settexture_f62859f817324dd1 = function(e, t) {
      e.texture = t;
    }, n.wbg.__wbg_settimestamp_fea9915c542831dc = function(e, t) {
      e.timestamp = t;
    }, n.wbg.__wbg_settimestampwrites_1995524c3a31cb8f = function(e, t) {
      e.timestampWrites = t;
    }, n.wbg.__wbg_settopology_3d9b2f0ffe2e350c = function(e, t) {
      e.topology = Se[t];
    }, n.wbg.__wbg_settype_0b59dd5f4721c490 = function(e, t) {
      e.type = ve[t];
    }, n.wbg.__wbg_settype_2a902a4a235bb64a = function(e, t, _) {
      e.type = u(t, _);
    }, n.wbg.__wbg_settype_39ed370d3edd403c = function(e, t, _) {
      e.type = u(t, _);
    }, n.wbg.__wbg_settype_4982e42c05ec7507 = function(e, t) {
      e.type = we[t];
    }, n.wbg.__wbg_settype_8c8bbfab4cf7e32e = function(e, t) {
      e.type = de[t];
    }, n.wbg.__wbg_setusage_44ebc3b496e60ff4 = function(e, t) {
      e.usage = t >>> 0;
    }, n.wbg.__wbg_setusage_4cf7b16df5617a46 = function(e, t) {
      e.usage = t >>> 0;
    }, n.wbg.__wbg_setusage_c45cca4a5b9f8376 = function(e, t) {
      e.usage = t >>> 0;
    }, n.wbg.__wbg_setusage_e58b3c3ce83fbbda = function(e, t) {
      e.usage = t >>> 0;
    }, n.wbg.__wbg_setvalue_6ad9ef6c692ea746 = function(e, t, _) {
      e.value = u(t, _);
    }, n.wbg.__wbg_setvertex_6144c56d98e2314a = function(e, t) {
      e.vertex = t;
    }, n.wbg.__wbg_setview_4bc3dfcbfc8a58ba = function(e, t) {
      e.view = t;
    }, n.wbg.__wbg_setview_8d0b0055b6ef07e3 = function(e, t) {
      e.view = t;
    }, n.wbg.__wbg_setviewdimension_afac48443b8fb565 = function(e, t) {
      e.viewDimension = q[t];
    }, n.wbg.__wbg_setviewdimension_f5d4b5336a27d302 = function(e, t) {
      e.viewDimension = q[t];
    }, n.wbg.__wbg_setviewformats_0cfe174ac882efaf = function(e, t) {
      e.viewFormats = t;
    }, n.wbg.__wbg_setviewformats_c566feb1da7b1925 = function(e, t) {
      e.viewFormats = t;
    }, n.wbg.__wbg_setvisibility_7245f1acbedb4ff4 = function(e, t) {
      e.visibility = t >>> 0;
    }, n.wbg.__wbg_setwidth_056381a7176ba440 = function(e, t) {
      e.width = t >>> 0;
    }, n.wbg.__wbg_setwidth_660ca581e3fbe279 = function(e, t) {
      e.width = t >>> 0;
    }, n.wbg.__wbg_setwidth_c5fed9f5e7f0b406 = function(e, t) {
      e.width = t >>> 0;
    }, n.wbg.__wbg_setwritemask_c381ff702509999c = function(e, t) {
      e.writeMask = t >>> 0;
    }, n.wbg.__wbg_setx_6e550cba86f408f0 = function(e, t) {
      e.x = t >>> 0;
    }, n.wbg.__wbg_setx_941ab227b0ea435d = function(e, t) {
      e.x = t >>> 0;
    }, n.wbg.__wbg_sety_16ff3ff771600f8c = function(e, t) {
      e.y = t >>> 0;
    }, n.wbg.__wbg_sety_e9ed0be0aad66dd7 = function(e, t) {
      e.y = t >>> 0;
    }, n.wbg.__wbg_setz_b2c09b24c996ee06 = function(e, t) {
      e.z = t >>> 0;
    }, n.wbg.__wbg_shaderSource_72d3e8597ef85b67 = function(e, t, _, r) {
      e.shaderSource(t, u(_, r));
    }, n.wbg.__wbg_shaderSource_ad0087e637a35191 = function(e, t, _, r) {
      e.shaderSource(t, u(_, r));
    }, n.wbg.__wbg_shiftKey_2bebb3b703254f47 = function(e) {
      return e.shiftKey;
    }, n.wbg.__wbg_shiftKey_86e737105bab1a54 = function(e) {
      return e.shiftKey;
    }, n.wbg.__wbg_signal_aaf9ad74119f20a4 = function(e) {
      return e.signal;
    }, n.wbg.__wbg_size_3808d41635a9c259 = function(e) {
      return e.size;
    }, n.wbg.__wbg_size_73bdfb6d5ffd9c4b = function(e) {
      return e.size;
    }, n.wbg.__wbg_stack_beab7d471979a9a5 = function(e, t) {
      const _ = t.stack, r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
      w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
    }, n.wbg.__wbg_stack_ce508d4881a78479 = function(e, t) {
      const _ = t.stack, r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
      w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
    }, n.wbg.__wbg_state_16d8f531272cd08b = function() {
      return a(function(e) {
        return e.state;
      }, arguments);
    }, n.wbg.__wbg_state_2cfec7c4f22f2b49 = function(e) {
      return e.state;
    }, n.wbg.__wbg_static_accessor_GLOBAL_88a902d13a557d07 = function() {
      const e = typeof global > "u" ? null : global;
      return g(e) ? 0 : l(e);
    }, n.wbg.__wbg_static_accessor_GLOBAL_THIS_56578be7e9f832b0 = function() {
      const e = typeof globalThis > "u" ? null : globalThis;
      return g(e) ? 0 : l(e);
    }, n.wbg.__wbg_static_accessor_SELF_37c5d418e4bf5819 = function() {
      const e = typeof self > "u" ? null : self;
      return g(e) ? 0 : l(e);
    }, n.wbg.__wbg_static_accessor_WINDOW_5de37043a91a9c40 = function() {
      const e = typeof window > "u" ? null : window;
      return g(e) ? 0 : l(e);
    }, n.wbg.__wbg_statusText_207754230b39e67c = function(e, t) {
      const _ = t.statusText, r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
      w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
    }, n.wbg.__wbg_status_f6360336ca686bf0 = function(e) {
      return e.status;
    }, n.wbg.__wbg_stencilFuncSeparate_91700dcf367ae07e = function(e, t, _, r, c) {
      e.stencilFuncSeparate(t >>> 0, _ >>> 0, r, c >>> 0);
    }, n.wbg.__wbg_stencilFuncSeparate_c1a6fa2005ca0aaf = function(e, t, _, r, c) {
      e.stencilFuncSeparate(t >>> 0, _ >>> 0, r, c >>> 0);
    }, n.wbg.__wbg_stencilMaskSeparate_4f1a2defc8c10956 = function(e, t, _) {
      e.stencilMaskSeparate(t >>> 0, _ >>> 0);
    }, n.wbg.__wbg_stencilMaskSeparate_f8a0cfb5c2994d4a = function(e, t, _) {
      e.stencilMaskSeparate(t >>> 0, _ >>> 0);
    }, n.wbg.__wbg_stencilMask_1e602ef63f5b4144 = function(e, t) {
      e.stencilMask(t >>> 0);
    }, n.wbg.__wbg_stencilMask_cd8ca0a55817e599 = function(e, t) {
      e.stencilMask(t >>> 0);
    }, n.wbg.__wbg_stencilOpSeparate_1fa08985e79e1627 = function(e, t, _, r, c) {
      e.stencilOpSeparate(t >>> 0, _ >>> 0, r >>> 0, c >>> 0);
    }, n.wbg.__wbg_stencilOpSeparate_ff6683bbe3838ae6 = function(e, t, _, r, c) {
      e.stencilOpSeparate(t >>> 0, _ >>> 0, r >>> 0, c >>> 0);
    }, n.wbg.__wbg_stopPropagation_11d220a858e5e0fb = function(e) {
      e.stopPropagation();
    }, n.wbg.__wbg_stringify_f7ed6987935b4a24 = function() {
      return a(function(e) {
        return JSON.stringify(e);
      }, arguments);
    }, n.wbg.__wbg_structuredClone_50d8218aa4c8173d = function() {
      return a(function(e) {
        return window.structuredClone(e);
      }, arguments);
    }, n.wbg.__wbg_style_fb30c14e5815805c = function(e) {
      return e.style;
    }, n.wbg.__wbg_subarray_aa9065fa9dc5df96 = function(e, t, _) {
      return e.subarray(t >>> 0, _ >>> 0);
    }, n.wbg.__wbg_submit_252766c4e0945cee = function(e, t) {
      e.submit(t);
    }, n.wbg.__wbg_texImage2D_57483314967bdd11 = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p) {
        e.texImage2D(t >>> 0, _, r, c, o, f, i >>> 0, s >>> 0, p);
      }, arguments);
    }, n.wbg.__wbg_texImage2D_5f2835f02b1d1077 = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p) {
        e.texImage2D(t >>> 0, _, r, c, o, f, i >>> 0, s >>> 0, p);
      }, arguments);
    }, n.wbg.__wbg_texImage2D_b8edcb5692f65f88 = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p) {
        e.texImage2D(t >>> 0, _, r, c, o, f, i >>> 0, s >>> 0, p);
      }, arguments);
    }, n.wbg.__wbg_texImage3D_921b54d09bf45af0 = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p, y) {
        e.texImage3D(t >>> 0, _, r, c, o, f, i, s >>> 0, p >>> 0, y);
      }, arguments);
    }, n.wbg.__wbg_texImage3D_a00b7a4df48cf757 = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p, y) {
        e.texImage3D(t >>> 0, _, r, c, o, f, i, s >>> 0, p >>> 0, y);
      }, arguments);
    }, n.wbg.__wbg_texParameteri_8112b26b3c360b7e = function(e, t, _, r) {
      e.texParameteri(t >>> 0, _ >>> 0, r);
    }, n.wbg.__wbg_texParameteri_ef50743cb94d507e = function(e, t, _, r) {
      e.texParameteri(t >>> 0, _ >>> 0, r);
    }, n.wbg.__wbg_texStorage2D_fbda848497f3674e = function(e, t, _, r, c, o) {
      e.texStorage2D(t >>> 0, _, r >>> 0, c, o);
    }, n.wbg.__wbg_texStorage3D_fd7a7ca30e7981d1 = function(e, t, _, r, c, o, f) {
      e.texStorage3D(t >>> 0, _, r >>> 0, c, o, f);
    }, n.wbg.__wbg_texSubImage2D_061605071aad9d2c = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p) {
        e.texSubImage2D(t >>> 0, _, r, c, o, f, i >>> 0, s >>> 0, p);
      }, arguments);
    }, n.wbg.__wbg_texSubImage2D_82670edc2c5acd35 = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p) {
        e.texSubImage2D(t >>> 0, _, r, c, o, f, i >>> 0, s >>> 0, p);
      }, arguments);
    }, n.wbg.__wbg_texSubImage2D_aa9a084093764796 = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p) {
        e.texSubImage2D(t >>> 0, _, r, c, o, f, i >>> 0, s >>> 0, p);
      }, arguments);
    }, n.wbg.__wbg_texSubImage2D_c7951ed97252bdff = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p) {
        e.texSubImage2D(t >>> 0, _, r, c, o, f, i >>> 0, s >>> 0, p);
      }, arguments);
    }, n.wbg.__wbg_texSubImage2D_d52d1a0d3654c60b = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p) {
        e.texSubImage2D(t >>> 0, _, r, c, o, f, i >>> 0, s >>> 0, p);
      }, arguments);
    }, n.wbg.__wbg_texSubImage2D_dd9cac68ad5fe0b6 = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p) {
        e.texSubImage2D(t >>> 0, _, r, c, o, f, i >>> 0, s >>> 0, p);
      }, arguments);
    }, n.wbg.__wbg_texSubImage2D_e6d34f5bb062e404 = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p) {
        e.texSubImage2D(t >>> 0, _, r, c, o, f, i >>> 0, s >>> 0, p);
      }, arguments);
    }, n.wbg.__wbg_texSubImage2D_f39ea52a2d4bd2f7 = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p) {
        e.texSubImage2D(t >>> 0, _, r, c, o, f, i >>> 0, s >>> 0, p);
      }, arguments);
    }, n.wbg.__wbg_texSubImage2D_fbdf91268228c757 = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p) {
        e.texSubImage2D(t >>> 0, _, r, c, o, f, i >>> 0, s >>> 0, p);
      }, arguments);
    }, n.wbg.__wbg_texSubImage3D_02bbdad14919acfc = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p, y, x) {
        e.texSubImage3D(t >>> 0, _, r, c, o, f, i, s, p >>> 0, y >>> 0, x);
      }, arguments);
    }, n.wbg.__wbg_texSubImage3D_04731251d7cecc83 = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p, y, x) {
        e.texSubImage3D(t >>> 0, _, r, c, o, f, i, s, p >>> 0, y >>> 0, x);
      }, arguments);
    }, n.wbg.__wbg_texSubImage3D_37f0045d16871670 = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p, y, x) {
        e.texSubImage3D(t >>> 0, _, r, c, o, f, i, s, p >>> 0, y >>> 0, x);
      }, arguments);
    }, n.wbg.__wbg_texSubImage3D_3a871f6405d2f183 = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p, y, x) {
        e.texSubImage3D(t >>> 0, _, r, c, o, f, i, s, p >>> 0, y >>> 0, x);
      }, arguments);
    }, n.wbg.__wbg_texSubImage3D_66acd67f56e3b214 = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p, y, x) {
        e.texSubImage3D(t >>> 0, _, r, c, o, f, i, s, p >>> 0, y >>> 0, x);
      }, arguments);
    }, n.wbg.__wbg_texSubImage3D_a051de089266fa1b = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p, y, x) {
        e.texSubImage3D(t >>> 0, _, r, c, o, f, i, s, p >>> 0, y >>> 0, x);
      }, arguments);
    }, n.wbg.__wbg_texSubImage3D_b28c55f839bbec41 = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p, y, x) {
        e.texSubImage3D(t >>> 0, _, r, c, o, f, i, s, p >>> 0, y >>> 0, x);
      }, arguments);
    }, n.wbg.__wbg_texSubImage3D_f18bf091cd48774c = function() {
      return a(function(e, t, _, r, c, o, f, i, s, p, y, x) {
        e.texSubImage3D(t >>> 0, _, r, c, o, f, i, s, p >>> 0, y >>> 0, x);
      }, arguments);
    }, n.wbg.__wbg_then_44b73946d2fb3e7d = function(e, t) {
      return e.then(t);
    }, n.wbg.__wbg_then_48b406749878a531 = function(e, t, _) {
      return e.then(t, _);
    }, n.wbg.__wbg_timestamp_5f0512a1aa9d6d32 = function(e, t) {
      const _ = t.timestamp;
      w().setFloat64(e + 8 * 1, g(_) ? 0 : _, !0), w().setInt32(e + 4 * 0, !g(_), !0);
    }, n.wbg.__wbg_toString_5285597960676b7b = function(e) {
      return e.toString();
    }, n.wbg.__wbg_toString_c813bbd34d063839 = function(e) {
      return e.toString();
    }, n.wbg.__wbg_top_ec9fceb1f030f2ea = function(e) {
      return e.top;
    }, n.wbg.__wbg_touches_6831ee0099511603 = function(e) {
      return e.touches;
    }, n.wbg.__wbg_trace_ec850a3dbadf664c = function(e, t) {
      console.trace(u(e, t));
    }, n.wbg.__wbg_type_00566e0d2e337e2e = function(e, t) {
      const _ = t.type, r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
      w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
    }, n.wbg.__wbg_type_20c7c49b2fbe0023 = function(e, t) {
      const _ = t.type, r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
      w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
    }, n.wbg.__wbg_uniform1f_21390b04609a9fa5 = function(e, t, _) {
      e.uniform1f(t, _);
    }, n.wbg.__wbg_uniform1f_dc009a0e7f7e5977 = function(e, t, _) {
      e.uniform1f(t, _);
    }, n.wbg.__wbg_uniform1i_5ddd9d8ccbd390bb = function(e, t, _) {
      e.uniform1i(t, _);
    }, n.wbg.__wbg_uniform1i_ed95b6129dce4d84 = function(e, t, _) {
      e.uniform1i(t, _);
    }, n.wbg.__wbg_uniform1ui_66e092b67a21c84d = function(e, t, _) {
      e.uniform1ui(t, _ >>> 0);
    }, n.wbg.__wbg_uniform2fv_656fce9525420996 = function(e, t, _, r) {
      e.uniform2fv(t, h(_, r));
    }, n.wbg.__wbg_uniform2fv_d8bd2a36da7ce440 = function(e, t, _, r) {
      e.uniform2fv(t, h(_, r));
    }, n.wbg.__wbg_uniform2iv_4d39fc5a26f03f55 = function(e, t, _, r) {
      e.uniform2iv(t, I(_, r));
    }, n.wbg.__wbg_uniform2iv_e967139a28017a99 = function(e, t, _, r) {
      e.uniform2iv(t, I(_, r));
    }, n.wbg.__wbg_uniform2uiv_4c340c9e8477bb07 = function(e, t, _, r) {
      e.uniform2uiv(t, R(_, r));
    }, n.wbg.__wbg_uniform3fv_7d828b7c4c91138e = function(e, t, _, r) {
      e.uniform3fv(t, h(_, r));
    }, n.wbg.__wbg_uniform3fv_8153c834ce667125 = function(e, t, _, r) {
      e.uniform3fv(t, h(_, r));
    }, n.wbg.__wbg_uniform3iv_58662d914661aa10 = function(e, t, _, r) {
      e.uniform3iv(t, I(_, r));
    }, n.wbg.__wbg_uniform3iv_f30d27ec224b4b24 = function(e, t, _, r) {
      e.uniform3iv(t, I(_, r));
    }, n.wbg.__wbg_uniform3uiv_38673b825dc755f6 = function(e, t, _, r) {
      e.uniform3uiv(t, R(_, r));
    }, n.wbg.__wbg_uniform4f_36b8f9be15064aa7 = function(e, t, _, r, c, o) {
      e.uniform4f(t, _, r, c, o);
    }, n.wbg.__wbg_uniform4f_f7ea07febf8b5108 = function(e, t, _, r, c, o) {
      e.uniform4f(t, _, r, c, o);
    }, n.wbg.__wbg_uniform4fv_8827081a7585145b = function(e, t, _, r) {
      e.uniform4fv(t, h(_, r));
    }, n.wbg.__wbg_uniform4fv_c01fbc6c022abac3 = function(e, t, _, r) {
      e.uniform4fv(t, h(_, r));
    }, n.wbg.__wbg_uniform4iv_7fe05be291899f06 = function(e, t, _, r) {
      e.uniform4iv(t, I(_, r));
    }, n.wbg.__wbg_uniform4iv_84fdf80745e7ff26 = function(e, t, _, r) {
      e.uniform4iv(t, I(_, r));
    }, n.wbg.__wbg_uniform4uiv_9de55998fbfef236 = function(e, t, _, r) {
      e.uniform4uiv(t, R(_, r));
    }, n.wbg.__wbg_uniformBlockBinding_18117f4bda07115b = function(e, t, _, r) {
      e.uniformBlockBinding(t, _ >>> 0, r >>> 0);
    }, n.wbg.__wbg_uniformMatrix2fv_98681e400347369c = function(e, t, _, r, c) {
      e.uniformMatrix2fv(t, _ !== 0, h(r, c));
    }, n.wbg.__wbg_uniformMatrix2fv_bc019eb4784a3b8c = function(e, t, _, r, c) {
      e.uniformMatrix2fv(t, _ !== 0, h(r, c));
    }, n.wbg.__wbg_uniformMatrix2x3fv_6421f8d6f7f4d144 = function(e, t, _, r, c) {
      e.uniformMatrix2x3fv(t, _ !== 0, h(r, c));
    }, n.wbg.__wbg_uniformMatrix2x4fv_27d807767d7aadc6 = function(e, t, _, r, c) {
      e.uniformMatrix2x4fv(t, _ !== 0, h(r, c));
    }, n.wbg.__wbg_uniformMatrix3fv_3d6ad3a1e0b0b5b6 = function(e, t, _, r, c) {
      e.uniformMatrix3fv(t, _ !== 0, h(r, c));
    }, n.wbg.__wbg_uniformMatrix3fv_3df529aab93cf902 = function(e, t, _, r, c) {
      e.uniformMatrix3fv(t, _ !== 0, h(r, c));
    }, n.wbg.__wbg_uniformMatrix3x2fv_79357317e9637d05 = function(e, t, _, r, c) {
      e.uniformMatrix3x2fv(t, _ !== 0, h(r, c));
    }, n.wbg.__wbg_uniformMatrix3x4fv_9d1a88b5abfbd64b = function(e, t, _, r, c) {
      e.uniformMatrix3x4fv(t, _ !== 0, h(r, c));
    }, n.wbg.__wbg_uniformMatrix4fv_da94083874f202ad = function(e, t, _, r, c) {
      e.uniformMatrix4fv(t, _ !== 0, h(r, c));
    }, n.wbg.__wbg_uniformMatrix4fv_e87383507ae75670 = function(e, t, _, r, c) {
      e.uniformMatrix4fv(t, _ !== 0, h(r, c));
    }, n.wbg.__wbg_uniformMatrix4x2fv_aa507d918a0b5a62 = function(e, t, _, r, c) {
      e.uniformMatrix4x2fv(t, _ !== 0, h(r, c));
    }, n.wbg.__wbg_uniformMatrix4x3fv_6712c7a3b4276fb4 = function(e, t, _, r, c) {
      e.uniformMatrix4x3fv(t, _ !== 0, h(r, c));
    }, n.wbg.__wbg_unmap_7b299155f31a9d79 = function(e) {
      e.unmap();
    }, n.wbg.__wbg_url_ae10c34ca209681d = function(e, t) {
      const _ = t.url, r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
      w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
    }, n.wbg.__wbg_usage_7d38adc6eaf96849 = function(e) {
      return e.usage;
    }, n.wbg.__wbg_useProgram_473bf913989b6089 = function(e, t) {
      e.useProgram(t);
    }, n.wbg.__wbg_useProgram_9b2660f7bb210471 = function(e, t) {
      e.useProgram(t);
    }, n.wbg.__wbg_userAgent_12e9d8e62297563f = function() {
      return a(function(e, t) {
        const _ = t.userAgent, r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
        w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
      }, arguments);
    }, n.wbg.__wbg_valueOf_39a18758c25e8b95 = function(e) {
      return e.valueOf();
    }, n.wbg.__wbg_value_91cbf0dd3ab84c1e = function(e, t) {
      const _ = t.value, r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
      w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
    }, n.wbg.__wbg_value_cd1ffa7b1ab794f1 = function(e) {
      return e.value;
    }, n.wbg.__wbg_versions_c01dfd4722a88165 = function(e) {
      return e.versions;
    }, n.wbg.__wbg_vertexAttribDivisorANGLE_11e909d332960413 = function(e, t, _) {
      e.vertexAttribDivisorANGLE(t >>> 0, _ >>> 0);
    }, n.wbg.__wbg_vertexAttribDivisor_4d361d77ffb6d3ff = function(e, t, _) {
      e.vertexAttribDivisor(t >>> 0, _ >>> 0);
    }, n.wbg.__wbg_vertexAttribIPointer_d0c67543348c90ce = function(e, t, _, r, c, o) {
      e.vertexAttribIPointer(t >>> 0, _, r >>> 0, c, o);
    }, n.wbg.__wbg_vertexAttribPointer_550dc34903e3d1ea = function(e, t, _, r, c, o, f) {
      e.vertexAttribPointer(t >>> 0, _, r >>> 0, c !== 0, o, f);
    }, n.wbg.__wbg_vertexAttribPointer_7a2a506cdbe3aebc = function(e, t, _, r, c, o, f) {
      e.vertexAttribPointer(t >>> 0, _, r >>> 0, c !== 0, o, f);
    }, n.wbg.__wbg_videoHeight_3a43327a766c1f03 = function(e) {
      return e.videoHeight;
    }, n.wbg.__wbg_videoWidth_4b400cf6f4744a4d = function(e) {
      return e.videoWidth;
    }, n.wbg.__wbg_view_fd8a56e8983f448d = function(e) {
      const t = e.view;
      return g(t) ? 0 : l(t);
    }, n.wbg.__wbg_viewport_a1b4d71297ba89af = function(e, t, _, r, c) {
      e.viewport(t, _, r, c);
    }, n.wbg.__wbg_viewport_e615e98f676f2d39 = function(e, t, _, r, c) {
      e.viewport(t, _, r, c);
    }, n.wbg.__wbg_warn_707b3830f261bb01 = function(e, t) {
      console.warn(u(e, t));
    }, n.wbg.__wbg_width_4f334fc47ef03de1 = function(e) {
      return e.width;
    }, n.wbg.__wbg_width_5dde457d606ba683 = function(e) {
      return e.width;
    }, n.wbg.__wbg_width_8fe4e8f77479c2a6 = function(e) {
      return e.width;
    }, n.wbg.__wbg_width_b0c1d9f437a95799 = function(e) {
      return e.width;
    }, n.wbg.__wbg_width_cdaf02311c1621d1 = function(e) {
      return e.width;
    }, n.wbg.__wbg_width_f54c7178d3c78f16 = function(e) {
      return e.width;
    }, n.wbg.__wbg_writeBuffer_3193eaacefdcf39a = function() {
      return a(function(e, t, _, r, c, o) {
        e.writeBuffer(t, _, r, c, o);
      }, arguments);
    }, n.wbg.__wbg_writeText_51c338e8ae4b85b9 = function(e, t, _) {
      return e.writeText(u(t, _));
    }, n.wbg.__wbg_writeTexture_cd7877c213ee5704 = function() {
      return a(function(e, t, _, r, c) {
        e.writeTexture(t, _, r, c);
      }, arguments);
    }, n.wbg.__wbg_write_e357400b06c0ccf5 = function(e, t) {
      return e.write(t);
    }, n.wbg.__wbindgen_as_number = function(e) {
      return +e;
    }, n.wbg.__wbindgen_boolean_get = function(e) {
      const t = e;
      return typeof t == "boolean" ? t ? 1 : 0 : 2;
    }, n.wbg.__wbindgen_cb_drop = function(e) {
      const t = e.original;
      return t.cnt-- == 1 ? (t.a = 0, !0) : !1;
    }, n.wbg.__wbindgen_closure_wrapper103929 = function(e, t, _) {
      return S(e, t, 22218, X);
    }, n.wbg.__wbindgen_closure_wrapper103931 = function(e, t, _) {
      return S(e, t, 22218, X);
    }, n.wbg.__wbindgen_closure_wrapper108112 = function(e, t, _) {
      return S(e, t, 22813, ie);
    }, n.wbg.__wbindgen_closure_wrapper1412 = function(e, t, _) {
      return S(e, t, 13, be);
    }, n.wbg.__wbindgen_closure_wrapper73201 = function(e, t, _) {
      return S(e, t, 17585, ae);
    }, n.wbg.__wbindgen_closure_wrapper7748 = function(e, t, _) {
      return S(e, t, 1342, oe);
    }, n.wbg.__wbindgen_closure_wrapper77884 = function(e, t, _) {
      return S(e, t, 18201, Q);
    }, n.wbg.__wbindgen_closure_wrapper77886 = function(e, t, _) {
      return S(e, t, 18201, Q);
    }, n.wbg.__wbindgen_closure_wrapper77888 = function(e, t, _) {
      return S(e, t, 18201, fe);
    }, n.wbg.__wbindgen_closure_wrapper81542 = function(e, t, _) {
      return S(e, t, 18726, ue);
    }, n.wbg.__wbindgen_debug_string = function(e, t) {
      const _ = C(t), r = m(_, b.__wbindgen_malloc, b.__wbindgen_realloc), c = d;
      w().setInt32(e + 4 * 1, c, !0), w().setInt32(e + 4 * 0, r, !0);
    }, n.wbg.__wbindgen_error_new = function(e, t) {
      return new Error(u(e, t));
    }, n.wbg.__wbindgen_in = function(e, t) {
      return e in t;
    }, n.wbg.__wbindgen_init_externref_table = function() {
      const e = b.__wbindgen_export_1, t = e.grow(4);
      e.set(0, void 0), e.set(t + 0, void 0), e.set(t + 1, null), e.set(t + 2, !0), e.set(t + 3, !1);
    }, n.wbg.__wbindgen_is_falsy = function(e) {
      return !e;
    }, n.wbg.__wbindgen_is_function = function(e) {
      return typeof e == "function";
    }, n.wbg.__wbindgen_is_null = function(e) {
      return e === null;
    }, n.wbg.__wbindgen_is_object = function(e) {
      const t = e;
      return typeof t == "object" && t !== null;
    }, n.wbg.__wbindgen_is_string = function(e) {
      return typeof e == "string";
    }, n.wbg.__wbindgen_is_undefined = function(e) {
      return e === void 0;
    }, n.wbg.__wbindgen_jsval_loose_eq = function(e, t) {
      return e == t;
    }, n.wbg.__wbindgen_memory = function() {
      return b.memory;
    }, n.wbg.__wbindgen_number_get = function(e, t) {
      const _ = t, r = typeof _ == "number" ? _ : void 0;
      w().setFloat64(e + 8 * 1, g(r) ? 0 : r, !0), w().setInt32(e + 4 * 0, !g(r), !0);
    }, n.wbg.__wbindgen_number_new = function(e) {
      return e;
    }, n.wbg.__wbindgen_string_get = function(e, t) {
      const _ = t, r = typeof _ == "string" ? _ : void 0;
      var c = g(r) ? 0 : m(r, b.__wbindgen_malloc, b.__wbindgen_realloc), o = d;
      w().setInt32(e + 4 * 1, o, !0), w().setInt32(e + 4 * 0, c, !0);
    }, n.wbg.__wbindgen_string_new = function(e, t) {
      return u(e, t);
    }, n.wbg.__wbindgen_throw = function(e, t) {
      throw new Error(u(e, t));
    }, n;
  }
  function te(n, e) {
    return b = n.exports, U.__wbindgen_wasm_module = e, v = null, P = null, B = null, F = null, T = null, b.__wbindgen_start(), b;
  }
  function He(n) {
    if (b !== void 0)
      return b;
    typeof n < "u" && (Object.getPrototypeOf(n) === Object.prototype ? { module: n } = n : console.warn("using deprecated parameters for `initSync()`; pass a single object instead"));
    const e = ee();
    n instanceof WebAssembly.Module || (n = new WebAssembly.Module(n));
    const t = new WebAssembly.Instance(n, e);
    return te(t, n);
  }
  async function U(n) {
    if (b !== void 0)
      return b;
    typeof n < "u" && (Object.getPrototypeOf(n) === Object.prototype ? { module_or_path: n } = n : console.warn("using deprecated parameters for the initialization function; pass a single object instead"));
    const e = ee();
    (typeof n == "string" || typeof Request == "function" && n instanceof Request || typeof URL == "function" && n instanceof URL) && (n = fetch(n));
    const { instance: t, module: _ } = await je(await n, e);
    return te(t, _);
  }
  function Ke() {
    U.__wbindgen_wasm_module = null, b = null, T = null, P = null, B = null, F = null, v = null;
  }
  return Object.assign(U, { initSync: He, deinit: Ke }, M);
}
export {
  Ne as default
};
