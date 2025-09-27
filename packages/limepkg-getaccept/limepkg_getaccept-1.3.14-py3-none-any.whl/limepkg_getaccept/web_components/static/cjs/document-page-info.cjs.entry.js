'use strict';

Object.defineProperty(exports, '__esModule', { value: true });

const index = require('./index-1129c609.js');

const documentPageInfoCss = ".page-info-container{display:flex}.page-info-container .page-number{display:inline-flex;align-items:center;justify-content:center;height:1.5rem;width:1.5rem;margin-right:1rem;border-radius:50%;-webkit-border-radius:50%;-moz-border-radius:50%;-ms-border-radius:50%;-o-border-radius:50%;background-color:#f49132;color:#fff}.page-info-container .page-thumb{width:4rem;height:6rem;background-color:#ccc;object-fit:contain}.page-info-container .page-time-spent{margin-left:1rem}.page-info-container .page-time-spent .page-time-spent-text{display:block;font-size:0.6rem;font-weight:bold;text-transform:uppercase}.page-info-percent{margin-bottom:1rem}";
const DocumentPageInfoStyle0 = documentPageInfoCss;

const DocumentPageInfo = class {
    constructor(hostRef) {
        index.registerInstance(this, hostRef);
        this.page = undefined;
        this.documentId = undefined;
        this.session = undefined;
        this.totalTime = 0;
        this.value = 0;
        this.valuePercent = 0;
    }
    componentWillLoad() {
        if (this.totalTime > 0 && this.page.page_time > 0) {
            this.value = this.page.page_time / this.totalTime;
            // eslint-disable-next-line @typescript-eslint/no-magic-numbers
            this.valuePercent = Math.round(this.value * 100);
        }
    }
    // private getThumbUrl(originalUrl = ''): string {
    //     const s3_credentials: string = originalUrl.split('?')[1];
    //     const bucket: string = this.getS3Bucket(originalUrl);
    //     return `getaccept/page_thumb_proxy/${bucket}/${
    //         this.session.entity_id
    //     }/${this.documentId}/${this.page.page_id}/${encodeURIComponent(
    //         s3_credentials
    //     )}`;
    // }
    // private getS3Bucket(originalUrl: string): string {
    //     return originalUrl.replace('https://', '').split('.s3.')[0] || '';
    // }
    render() {
        return [
            index.h("div", { key: '4a608fd8219aa5c4bc300536bb65fde9ebe283b1', class: "page-info-container" }, index.h("div", { key: 'e592bb8c1b57795a3b513626e3d2eb711d092831', class: "page-number" }, this.page.page_num), index.h("img", { key: '3a533a7518f0a183e499fd3bc1bfadb828b7bb47', class: "page-thumb", src: this.page.thumb_url }), index.h("div", { key: 'b08d16455463f8c93b1a92f63eb4e08a3068b22c', class: "page-time-spent" }, index.h("span", { key: 'e95ddf966db942cfd2e5829f408c558229a8844c', class: "page-time-spent-text" }, "Time spent"), index.h("span", { key: '3b6081da291050844918eede3fc32421052c8252' }, this.page.page_time, "s"))),
            index.h("div", { key: 'd478698c64396cf4252662cc7a9fb53ef22a0ac2', class: "page-info-percent" }, index.h("span", { key: '26e089fd5d7a369d0e411a3d12bf7adf593b7492' }, this.valuePercent, "%"), index.h("limel-linear-progress", { key: '1eae9129114997f03dc76c87b609c1e97d05eac9', value: this.value })),
        ];
    }
};
DocumentPageInfo.style = DocumentPageInfoStyle0;

exports.document_page_info = DocumentPageInfo;

//# sourceMappingURL=document-page-info.cjs.entry.js.map