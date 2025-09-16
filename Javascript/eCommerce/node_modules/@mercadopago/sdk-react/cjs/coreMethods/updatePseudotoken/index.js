"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
const initMercadoPago_1 = require("../../mercadoPago/initMercadoPago");
/**
 * Updates a pseudotoken with card token information
 *
 * @param fastPaymentToken - Base64 encoded token data containing authentication
 * @param pseudotoken - The pseudotoken to update
 * @param cardToken - The card token to associate with the pseudotoken
 * @returns Promise that resolves when update is complete
 */
const updatePseudotoken = (fastPaymentToken, pseudotoken, cardToken) => __awaiter(void 0, void 0, void 0, function* () {
    const instanceMercadoPago = yield initMercadoPago_1.MercadoPagoInstance.getInstance();
    return instanceMercadoPago === null || instanceMercadoPago === void 0 ? void 0 : instanceMercadoPago.updatePseudotoken(fastPaymentToken, pseudotoken, cardToken);
});
exports.default = updatePseudotoken;
