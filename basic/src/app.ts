// SPDX-License-Identifier: MIT

import { MediaQueryListener } from "./tools/media-query-listener";

import "./styles";
import "./effects";

new MediaQueryListener();

document.addEventListener(
  "DOMContentLoaded",
  () => {
    const path = window.location.pathname;

    if (globalThis.Mobile) {
      const html = document.getElementById("html");
      html!.classList.add("mobile");
    }

    switch (path) {
      case "/": {
        const lorem = document.getElementById("lorem");

        lorem!.classList.remove("hide");
        lorem!.classList.add("show");

        break;
      }
    }
  },
  false,
);
