import{j as r}from"./index-B3MJ8ma8.js";import"./helperFunctions-BD_6K8Ns.js";import"./index-Dy3Fyuje.js";import"./svelte/svelte.js";const e="rgbdDecodePixelShader",o=`varying vec2 vUV;uniform sampler2D textureSampler;
#include<helperFunctions>
#define CUSTOM_FRAGMENT_DEFINITIONS
void main(void) 
{gl_FragColor=vec4(fromRGBD(texture2D(textureSampler,vUV)),1.0);}`;r.ShadersStore[e]||(r.ShadersStore[e]=o);const m={name:e,shader:o};export{m as rgbdDecodePixelShader};
//# sourceMappingURL=rgbdDecode.fragment-DI2dL5GQ.js.map
