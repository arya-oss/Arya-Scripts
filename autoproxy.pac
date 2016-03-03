/**
 * Auto Proxy Configuration Script for Web Browsers
 * find best proxy for your website write RegEx for website and respective proxy.
 * @return default proxy
 * 
 * $ cat autoproxy.pac | base64 > encode.txt
 * preped encode.txt file
 * write -> data:;base64,
 * ---- How to ----
 * goto proxy settings for browsers and paste content of encode.txt
 * in auto config url field
 */

function FindProxyForURL(url, host) {
	if (shExpMatch(url, "*youtube*")) return 'PROXY 172.20.0.96:8080';
	if (shExpMatch(url, "*.facebook.com/*") || shExpMatch(url, "*://facebook.com/*")) return 'PROXY 172.30.0.9:3128';
	if (shExpMatch(url, "*pagead*")) return 'DIRECT';
	if (shExpMatch(url, "*doubleclick*")) return 'DIRECT';
	if (shExpMatch(url, "*fbstatic*")) return 'PROXY 172.30.0.11:3128';
	if (shExpMatch(url, "*fbcdn*")) return 'PROXY 172.30.0.11:3128';
	if (shExpMatch(url, "*.gmail.*") || shExpMatch(url, "*://gmail.*")) return 'PROXY 172.30.0.9:3128';
	if (shExpMatch(url, "*google.com*")) return 'PROXY 172.30.0.9:3128';
	if (shExpMatch(url, "*gstatic*")) return 'PROXY 172.30.0.21:3128';
	if (shExpMatch(url, "*googlevideo*")) return 'PROXY 172.30.0.19:3128';
	if(shExpMatch(host, 'localhost')) return 'DIRECT';
	if(shExpMatch(host, '127.0.0.1')) return 'DIRECT';
	if(shExpMatch(host, '<local>')) return 'DIRECT';
	return 'PROXY 172.30.0.11:3128';
}