var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
import { MercadoPagoInstance } from '../../mercadoPago/initMercadoPago';
/**
 * Retrieves card ID from a pseudotoken
 *
 * @param fastPaymentToken - Base64 encoded token data containing authentication
 * @param pseudotoken - The pseudotoken to get card ID for
 * @returns Promise with card ID response
 */
const getCardId = (fastPaymentToken, pseudotoken) => __awaiter(void 0, void 0, void 0, function* () {
    const instanceMercadoPago = yield MercadoPagoInstance.getInstance();
    return instanceMercadoPago === null || instanceMercadoPago === void 0 ? void 0 : instanceMercadoPago.getCardId(fastPaymentToken, pseudotoken);
});
export default getCardId;
