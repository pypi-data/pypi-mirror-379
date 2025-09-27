import { defineComponent as m, useAttrs as h, useSlots as C, createBlock as p, openBlock as _, mergeProps as b, unref as a, createSlots as S, renderList as y, withCtx as v, renderSlot as D, normalizeProps as A, guardReactiveProps as x, computed as P, ref as $, resolveDynamicComponent as w } from "vue";
import * as d from "tdesign-vue-next";
function z(n) {
  const { container: t = ".insta-main" } = n;
  return t;
}
const k = /* @__PURE__ */ m({
  inheritAttrs: !1,
  __name: "Affix",
  setup(n) {
    const t = h(), s = C(), o = z(t);
    return (e, r) => (_(), p(d.Affix, b(a(t), { container: a(o) }), S({ _: 2 }, [
      y(a(s), (c, u) => ({
        name: u,
        fn: v((i) => [
          D(e.$slots, u, A(x(i)))
        ])
      }))
    ]), 1040, ["container"]));
  }
});
function T(n) {
  return P(() => {
    const { pagination: t, data: s = [] } = n;
    let o;
    if (typeof t == "boolean") {
      if (!t)
        return;
      o = {
        defaultPageSize: 10
      };
    }
    return typeof t == "number" && t > 0 && (o = {
      defaultPageSize: t
    }), typeof t == "object" && t !== null && (o = t), {
      defaultCurrent: 1,
      total: s.length,
      ...o
    };
  });
}
function I(n) {
  let t = $(n.sort);
  const s = $(n.data), o = P(() => {
    const { columns: e, data: r = [], ...c } = n, i = !e && r.length > 0 ? B(r) : e, {
      onSortChange: l,
      columns: f,
      multipleSort: g
    } = K({
      sort: t,
      tableData: s,
      columns: i
    });
    return {
      hover: !0,
      bordered: !0,
      tableLayout: "auto",
      columns: f,
      onSortChange: l,
      multipleSort: g,
      showSortColumnBgColor: !0,
      ...c
    };
  });
  return {
    sort: t,
    tableData: s,
    bindAttrs: o
  };
}
function B(n) {
  const t = n[0];
  return Object.keys(t).map((o) => ({
    colKey: o,
    title: o,
    sorter: !0
  }));
}
function j(n) {
  const t = n.colKey;
  return (s, o) => {
    const e = s[t], r = o[t];
    return e == null && r == null ? 0 : e == null ? 1 : r == null ? -1 : typeof e == "number" && typeof r == "number" ? e - r : e instanceof Date && r instanceof Date ? e.getTime() - r.getTime() : typeof e == "string" && typeof r == "string" ? e.localeCompare(r, void 0, { numeric: !0 }) : String(e).localeCompare(String(r), void 0, { numeric: !0 });
  };
}
function K(n) {
  const { tableData: t, sort: s, columns: o } = n;
  let e = !1, r = 0;
  const c = o?.map((i) => i.sorter === !0 ? (e = !0, r++, {
    ...i,
    sorter: j(i)
  }) : i);
  return {
    onSortChange: e ? (i, l) => {
      s.value = i, t.value = l.currentDataSource;
    } : void 0,
    columns: c,
    multipleSort: r > 1
  };
}
const L = /* @__PURE__ */ m({
  inheritAttrs: !1,
  __name: "Table",
  setup(n) {
    const t = h(), s = T(t), { sort: o, bindAttrs: e, tableData: r } = I(t), c = C();
    return (u, i) => (_(), p(d.Table, b(a(e), {
      pagination: a(s),
      sort: a(o),
      data: a(r)
    }), S({ _: 2 }, [
      y(a(c), (l, f) => ({
        name: f,
        fn: v((g) => [
          D(u.$slots, f, A(x(g)))
        ])
      }))
    ]), 1040, ["pagination", "sort", "data"]));
  }
});
function R(n) {
  const { affixProps: t = {} } = n;
  return {
    container: ".insta-main",
    ...t
  };
}
function O(n) {
  const { container: t = ".insta-main" } = n;
  return t;
}
const W = /* @__PURE__ */ m({
  inheritAttrs: !1,
  __name: "Anchor",
  setup(n) {
    const t = h(), s = C(), o = R(t), e = O(t);
    return (r, c) => (_(), p(d.Anchor, b(a(t), {
      container: a(e),
      "affix-props": a(o)
    }), S({ _: 2 }, [
      y(a(s), (u, i) => ({
        name: i,
        fn: v((l) => [
          D(r.$slots, i, A(x(l)))
        ])
      }))
    ]), 1040, ["container", "affix-props"]));
  }
}), q = /* @__PURE__ */ m({
  __name: "Icon",
  props: {
    name: {},
    size: {},
    color: {},
    prefix: {}
  },
  setup(n) {
    const t = n, s = P(() => {
      const [o, e] = t.name.split(":");
      return e ? t.name : `${t.prefix || "tdesign"}:${t.name}`;
    });
    return (o, e) => (_(), p(w("icon"), {
      class: "t-icon",
      icon: s.value,
      size: o.size,
      color: o.color
    }, null, 8, ["icon", "size", "color"]));
  }
});
function F(n) {
  n.use(d), n.component("t-table", L), n.component("t-affix", k), n.component("t-anchor", W), n.component("t-icon", q);
}
export {
  F as install
};
