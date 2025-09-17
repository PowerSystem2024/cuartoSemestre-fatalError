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
const initMercadoPago_1 = require("../mercadoPago/initMercadoPago");
/**
 * Creates a new authenticator instance for SuperToken authentication
 * This feature is disabled by deafult, to enable it, please contact the offical *Mercado Pago* support via developer's website: www.mercadopago.com/developers
 * @param amount - The amount to be processed on the payment request
 * @param payerEmail - The email of the payer
 * @returns Promise that resolves to an authenticator instance
 */
const createAuthenticator = (amount, payerEmail) => __awaiter(void 0, void 0, void 0, function* () {
    const mp = yield initMercadoPago_1.MercadoPagoInstance.getInstance();
    if (!mp) {
        throw new Error('MercadoPago instance not found. Make sure to call initMercadoPago first.');
    }
    return yield mp.authenticator(amount, payerEmail);
});
exports.default = createAuthenticator;
