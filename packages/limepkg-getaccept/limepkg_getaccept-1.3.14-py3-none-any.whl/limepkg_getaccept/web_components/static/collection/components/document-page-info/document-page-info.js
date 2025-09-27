import { h } from "@stencil/core";
export class DocumentPageInfo {
    constructor() {
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
            h("div", { key: '4a608fd8219aa5c4bc300536bb65fde9ebe283b1', class: "page-info-container" }, h("div", { key: 'e592bb8c1b57795a3b513626e3d2eb711d092831', class: "page-number" }, this.page.page_num), h("img", { key: '3a533a7518f0a183e499fd3bc1bfadb828b7bb47', class: "page-thumb", src: this.page.thumb_url }), h("div", { key: 'b08d16455463f8c93b1a92f63eb4e08a3068b22c', class: "page-time-spent" }, h("span", { key: 'e95ddf966db942cfd2e5829f408c558229a8844c', class: "page-time-spent-text" }, "Time spent"), h("span", { key: '3b6081da291050844918eede3fc32421052c8252' }, this.page.page_time, "s"))),
            h("div", { key: 'd478698c64396cf4252662cc7a9fb53ef22a0ac2', class: "page-info-percent" }, h("span", { key: '26e089fd5d7a369d0e411a3d12bf7adf593b7492' }, this.valuePercent, "%"), h("limel-linear-progress", { key: '1eae9129114997f03dc76c87b609c1e97d05eac9', value: this.value })),
        ];
    }
    static get is() { return "document-page-info"; }
    static get encapsulation() { return "shadow"; }
    static get originalStyleUrls() {
        return {
            "$": ["document-page-info.scss"]
        };
    }
    static get styleUrls() {
        return {
            "$": ["document-page-info.css"]
        };
    }
    static get properties() {
        return {
            "page": {
                "type": "unknown",
                "mutable": false,
                "complexType": {
                    "original": "IDocumentPage",
                    "resolved": "IDocumentPage",
                    "references": {
                        "IDocumentPage": {
                            "location": "import",
                            "path": "../../types/DocumentPage",
                            "id": "src/types/DocumentPage.ts::IDocumentPage"
                        }
                    }
                },
                "required": false,
                "optional": false,
                "docs": {
                    "tags": [],
                    "text": ""
                }
            },
            "documentId": {
                "type": "string",
                "mutable": false,
                "complexType": {
                    "original": "string",
                    "resolved": "string",
                    "references": {}
                },
                "required": false,
                "optional": false,
                "docs": {
                    "tags": [],
                    "text": ""
                },
                "attribute": "document-id",
                "reflect": false
            },
            "session": {
                "type": "unknown",
                "mutable": false,
                "complexType": {
                    "original": "ISession",
                    "resolved": "ISession",
                    "references": {
                        "ISession": {
                            "location": "import",
                            "path": "../../types/Session",
                            "id": "src/types/Session.ts::ISession"
                        }
                    }
                },
                "required": false,
                "optional": false,
                "docs": {
                    "tags": [],
                    "text": ""
                }
            },
            "totalTime": {
                "type": "number",
                "mutable": false,
                "complexType": {
                    "original": "number",
                    "resolved": "number",
                    "references": {}
                },
                "required": false,
                "optional": false,
                "docs": {
                    "tags": [],
                    "text": ""
                },
                "attribute": "total-time",
                "reflect": false,
                "defaultValue": "0"
            }
        };
    }
    static get states() {
        return {
            "value": {},
            "valuePercent": {}
        };
    }
}
//# sourceMappingURL=document-page-info.js.map
