import { IDocumentPage } from '../../types/DocumentPage';
import { ISession } from '../../types/Session';
export declare class DocumentPageInfo {
    page: IDocumentPage;
    documentId: string;
    session: ISession;
    totalTime: number;
    private value;
    private valuePercent;
    componentWillLoad(): void;
    render(): any[];
}
