export const COMPANIES = {
  GET_COMPANIES: 'GET_COMPANIES',
  GET_COMPANIES_SUCCESS: 'GET_COMPANIES_SUCCESS',
  GET_COMPANIES_ERROR: 'GET_COMPANIES_ERROR',
  // UPDATE
  UPDATE_COMPANY: 'UPDATE_COMPANY',
  UPDATE_COMPANY_SUCCESS: 'UPDATE_COMPANY_SUCCESS',
  UPDATE_COMPANY_ERROR: 'UPDATE_COMPANY_ERROR',
  // ADD
  ADD_COMPANY: 'ADD_COMPANY',
  ADD_COMPANY_SUCCESS: 'ADD_COMPANY_SUCCESS',
  ADD_COMPANY_ERROR: 'ADD_COMPANY_ERROR',
};

const getCompanies = () => ({
  type: COMPANIES.GET_COMPANIES,
});

const updateCompany = payload => ({
  type: COMPANIES.UPDATE_COMPANY,
  payload,
});
const addCompany = payload => ({
  type: COMPANIES.ADD_COMPANY,
  payload,
});

export { getCompanies, updateCompany, addCompany };
