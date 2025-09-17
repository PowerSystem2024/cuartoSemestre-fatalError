/**
 * Retrieves account payment methods for authenticated users
 *
 * @param fastPaymentToken - Base64 encoded token data containing authentication and parameters
 * @returns Promise with account payment methods response
 */
declare const getAccountPaymentMethods: (fastPaymentToken: string) => Promise<import("./types").AccountPaymentMethodsResponse | undefined>;
export default getAccountPaymentMethods;
