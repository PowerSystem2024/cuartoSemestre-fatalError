/**
 * Retrieves card ID from a pseudotoken
 *
 * @param fastPaymentToken - Base64 encoded token data containing authentication
 * @param pseudotoken - The pseudotoken to get card ID for
 * @returns Promise with card ID response
 */
declare const getCardId: (fastPaymentToken: string, pseudotoken: string) => Promise<import("./types").CardIdResponse | undefined>;
export default getCardId;
