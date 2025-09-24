#include <stdint.h>
#include <gsl/gsl_blas.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_matrix.h>
#include "math.h"
#include "defines.h"
#include "misc.h"
#include "const.h"
#include "utilities.h"
#include "2d_array.h"
#include "output.h"
#include "s_ccd.h"
#include "distribution_math.h"
#include <time.h>
#define N_Columns 8
#define Max_DOF 30

int lasso_blist_sccd[NUM_LASSO_BANDS] = {1, 2, 3, 4, 5};

/******************************************************************************
MODULE:  sccd_offline

PURPOSE:  main function for stochastic ccd for offline mode

RETURN VALUE:
Type = int (SUCCESS OR FAILURE)

HISTORY:
Date        Programmer       Reason
--------    ---------------  -------------------------------------
11/14/2018   Su Ye         Original Development
04/14/2022   Su Ye         update
******************************************************************************/
int sccd(
    int64_t *buf_b,                      /* I:  Landsat blue spectral time series.The dimension is (n_obs, 7). Invalid (qa is filled value (255)) must be removed */
    int64_t *buf_g,                      /* I:  Landsat green spectral time series.The dimension is (n_obs, 7). Invalid (qa is filled value (255)) must be removed */
    int64_t *buf_r,                      /* I:  Landsat red spectral time series.The dimension is (n_obs, 7). Invalid (qa is filled value (255)) must be removed */
    int64_t *buf_n,                      /* I:  Landsat NIR spectral time series.The dimension is (n_obs, 7). Invalid (qa is filled value (255)) must be removed */
    int64_t *buf_s1,                     /* I:  Landsat swir1 spectral time series.The dimension is (n_obs, 7). Invalid (qa is filled value (255)) must be removed */
    int64_t *buf_s2,                     /* I:  Landsat swir2 spectral time series.The dimension is (n_obs, 7). Invalid (qa is filled value (255)) must be removed */
    int64_t *buf_t,                      /* I:  Landsat thermal spectral time series.The dimension is (n_obs, 7). Invalid (qa is filled value (255)) must be removed */
    int64_t *fmask_buf,                  /* I:  mask-based time series              */
    int64_t *valid_date_array,           /* I: valid date time series               */
    int valid_num_scenes,                /* I: number of valid scenes under cfmask fill counts  */
    double tcg,                          /* I: the change threshold  */
    int *num_fc,                         /* O: number of fitting curves                       */
    int *nrt_mode,                       /* O: 2nd digit: 0 - void; 1 - monitor mode for standard; 2 - queue mode for standard; 3 - monitor mode for snow; 4 - queue mode for snow; 1st digit: 1 - predictability untest */
    Output_sccd *rec_cg,                 /* O: historical change records for SCCD results    */
    output_nrtmodel *nrt_model,          /* O: nrt model structure for SCCD results    */
    int *num_obs_queue,                  /* O: the number of multispectral observations    */
    output_nrtqueue *obs_queue,          /* O: multispectral observations in queue    */
    short int *min_rmse,                 /* O: adjusted rmse for the pixel    */
    int conse,                           /* I: consecutive observation number for change detection   */
    bool b_c2,                           /* I: a temporal parameter to indicate if collection 2. C2 needs ignoring thermal band due to the current low quality  */
    bool output_anomaly,                 /* I: output anomaly break for training purpose  */
    Output_sccd_anomaly *rec_cg_anomaly, /* O: historical change records for SCCD results    */
    int *num_fc_anomaly,
    double anomaly_tcg,
    int anomaly_conse,
    double predictability_tcg,
    bool b_output_state, /* I: indicate whether to output state  */
    double state_intervaldays,
    int *n_state,
    int64_t *state_days,
    double *states_ensemble, /* O: states records for blue band */
    bool fitting_coefs,
    double lambda)
{
    int clear_sum = 0;  /* Total number of clear cfmask pixels          */
    int water_sum = 0;  /* counter for cfmask water pixels.             */
    int shadow_sum = 0; /* counter for cfmask shadow pixels.            */
    int sn_sum = 0;     /* Total number of snow cfmask pixels           */
    int cloud_sum = 0;  /* counter for cfmask cloud pixels.             */
    double sn_pct;      /* Percent of snow pixels.                      */
    int status;
    int *id_range;
    int i, k, i_b;
    char FUNC_NAME[] = "sccd";
    int result = SUCCESS;
    int n_clr = 0;
    int *clrx;                 /* I: clear pixel curve in X direction (date)             */
    float **clry;              /* O: clear pixel curve in Y direction (spectralbands)    */
    bool b_snow;               // indicate if snow pixels
    float max_date_difference; /* maximum difference between two neighbor dates        */
    float date_vario;          /* median date                                          */
    float min_rmse_float[TOTAL_IMAGE_BANDS_SCCD];
    int len_clrx; /* length of clrx  */
    int n_clr_record;
    int valid_nrt_mode[] = {0, 1, 2, 3, 4, 5, 11, 12};
    bool isinvalid_nrtmode = TRUE;
    int arrLen = sizeof valid_nrt_mode / sizeof valid_nrt_mode[0];
    nrt_coefs_records *coefs_records;
    int n_coefs_records = 0;
    double days;
    int cur_coefs = 0;
    double w = TWO_PI / AVE_DAYS_IN_A_YEAR;

    // nrt_coefs_records *coefs_records;

    for (int i = 0; i < arrLen; i++)
    {
        if (valid_nrt_mode[i] == *nrt_mode)
        {
            isinvalid_nrtmode = FALSE;
            break;
        }
    }

    if (isinvalid_nrtmode == TRUE)
    {
        RETURN_ERROR("Invalid nrt_mode", FUNC_NAME, ERROR);
    }

    // mode update condition 1: replace NRT_MONITOR2QUEUE with NRT_QUEUE_STANDARD as input
    // if (*nrt_mode % 10 == NRT_MONITOR2QUEUE)
    //     *nrt_mode = 10 + NRT_QUEUE_STANDARD;

    if ((*nrt_mode == NRT_QUEUE_SNOW) | (*nrt_mode % 10 == NRT_QUEUE_STANDARD) | (*nrt_mode % 10 == NRT_MONITOR2QUEUE))
        len_clrx = valid_num_scenes + *num_obs_queue;
    else if ((*nrt_mode == NRT_MONITOR_SNOW) | (*nrt_mode % 10 == NRT_MONITOR_STANDARD))
        len_clrx = valid_num_scenes + DEFAULT_CONSE_SCCD;
    else
        len_clrx = valid_num_scenes;

    id_range = (int *)calloc(len_clrx, sizeof(int));
    clrx = (int *)malloc(len_clrx * sizeof(int));
    if (clrx == NULL)
    {
        RETURN_ERROR("Allocating clrx memory", FUNC_NAME, FAILURE);
    }

    clry = (float **)allocate_2d_array(TOTAL_IMAGE_BANDS_SCCD, len_clrx,
                                       sizeof(float));
    if (clry == NULL)
    {
        RETURN_ERROR("Allocating clry memory", FUNC_NAME, FAILURE);
    }

    coefs_records = (nrt_coefs_records *)malloc(len_clrx * sizeof(nrt_coefs_records));

    status = preprocessing(buf_b, buf_g, buf_r, buf_n, buf_s1, buf_s2, buf_t,
                           fmask_buf, &valid_num_scenes, id_range, &clear_sum,
                           &water_sum, &shadow_sum, &sn_sum, &cloud_sum, b_c2);

    if (status != SUCCESS)
    {
        RETURN_ERROR("Error for preprocessing.", FUNC_NAME, ERROR);
    }

    // void status need to first decide if it is snow pixel by sn_pct
    if (*nrt_mode == NRT_VOID)
    {
        sn_pct = (double)sn_sum / (double)(sn_sum + clear_sum + 0.01);
        if (sn_pct < T_SN)
            b_snow = FALSE;
        else
            b_snow = TRUE;
    }
    else
    {
        if ((*nrt_mode == NRT_QUEUE_SNOW) | (*nrt_mode == NRT_MONITOR_SNOW))
            b_snow = TRUE;
        else
            b_snow = FALSE;
    }

    /*********************************************************************/
    /*                                                                   */
    /*     initializing clrx and clry using existing obs in queue        */
    /*                                                                   */
    /*********************************************************************/
    if ((*nrt_mode == NRT_QUEUE_SNOW) | (*nrt_mode % 10 == NRT_QUEUE_STANDARD) | (*nrt_mode % 10 == NRT_MONITOR2QUEUE))
    {
        // if queue mode, will append old observation first
        for (i = 0; i < *num_obs_queue; i++)
        {
            clrx[i] = obs_queue[i].clrx_since1982 + ORDINAL_LANDSAT4_LAUNCH;
            for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                clry[i_b][i] = obs_queue[i].clry[i_b];
            n_clr++;
        }
    }
    else if ((*nrt_mode == NRT_MONITOR_SNOW) | (*nrt_mode % 10 == NRT_MONITOR_STANDARD))
    {
        //  if monitor mode, will append output_nrtmodel default conse-1 obs
        for (k = 0; k < DEFAULT_CONSE_SCCD; k++)
        {
            if (k < conse)
            {
                for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                {
                    clry[i_b][k] = nrt_model->obs[i_b][k];
                }
                clrx[k] = nrt_model->obs_date_since1982[k] + ORDINAL_LANDSAT4_LAUNCH;
                n_clr++;
            }
        }
    }

    n_clr_record = n_clr;

    /**************************************************************/
    /*                                                            */
    /*  standard procedure for non-snow pixels                    */
    /*                                                            */
    /**************************************************************/
    if (FALSE == b_snow)
    {

        /**************************************************************/
        /*                                                            */
        /*  append new collected observations                         */
        /*                                                            */
        /**************************************************************/
        for (i = 0; i < valid_num_scenes; i++)
        {
            if ((fmask_buf[i] < 2) && (id_range[i] == 1))
            {
                // remain the first element for replicated date
                if ((n_clr > 0) && (valid_date_array[i] == clrx[n_clr - 1]))
                    continue;
                else
                {
                    clrx[n_clr] = (int)valid_date_array[i];
                    for (k = 0; k < TOTAL_IMAGE_BANDS_SCCD; k++)
                    {
                        if (k == 0)
                            clry[k][n_clr] = (float)buf_b[i];
                        else if (k == 1)
                            clry[k][n_clr] = (float)buf_g[i];
                        else if (k == 2)
                            clry[k][n_clr] = (float)buf_r[i];
                        else if (k == 3)
                            clry[k][n_clr] = (float)buf_n[i];
                        else if (k == 4)
                            clry[k][n_clr] = (float)buf_s1[i];
                        else if (k == 5)
                            clry[k][n_clr] = (float)buf_s2[i];
                        else if (k == 6)
                            clry[k][n_clr] = (float)buf_t[i];
                    }
                    n_clr++;
                }
            }
        }

        if (n_clr > n_clr_record)
        {

            /* need to calculate min_rmse at the beginning of the monitoring */
            if (*num_fc == 0)
            {
                if (*nrt_mode == NRT_VOID)
                {
                    status = adjust_median_variogram(clrx, clry, TOTAL_IMAGE_BANDS_SCCD, 0,
                                                     n_clr - 1, &date_vario, &max_date_difference,
                                                     min_rmse_float, 1);
                    for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                        min_rmse[i_b] = (short int)min_rmse_float[i_b];
                }
            }

            result = sccd_standard(clrx, clry, &n_clr, tcg, rec_cg, num_fc, nrt_mode, nrt_model, num_obs_queue, obs_queue, min_rmse, conse, output_anomaly, rec_cg_anomaly, num_fc_anomaly, anomaly_tcg, anomaly_conse, predictability_tcg, b_output_state, &n_coefs_records, coefs_records, fitting_coefs, lambda);
        }
    }
    else
    {
        /**************************************************************/
        /*                                                            */
        /*  append new collected observations                         */
        /*                                                            */
        /**************************************************************/
        for (i = 0; i < valid_num_scenes; i++)
        {
            if ((fmask_buf[i] == CFMASK_SNOW) || (fmask_buf[i] < 2))
            {
                // remain the first element for replicated date
                if ((n_clr > 0) && (valid_date_array[i] == clrx[n_clr - 1]))
                    continue;
                else
                {
                    clrx[n_clr] = (int)valid_date_array[i];
                    for (k = 0; k < TOTAL_IMAGE_BANDS_SCCD; k++)
                    {
                        if (k == 0)
                            clry[k][n_clr] = (float)buf_b[i];
                        else if (k == 1)
                            clry[k][n_clr] = (float)buf_g[i];
                        else if (k == 2)
                            clry[k][n_clr] = (float)buf_r[i];
                        else if (k == 3)
                            clry[k][n_clr] = (float)buf_n[i];
                        else if (k == 4)
                            clry[k][n_clr] = (float)buf_s1[i];
                        else if (k == 5)
                            clry[k][n_clr] = (float)buf_s2[i];
                        else if (k == 6)
                            clry[k][n_clr] = (float)buf_t[i];
                    }
                    n_clr++;
                }
            }
        }

        result = sccd_snow(clrx, clry, n_clr, nrt_mode, nrt_model, num_obs_queue, obs_queue, b_output_state, &n_coefs_records, coefs_records, lambda);
    }

    days = clrx[0];
    if (b_output_state)
    {
        while (cur_coefs < n_coefs_records)
        {
            state_days[*n_state] = days;

            for (i = 0; i < TOTAL_IMAGE_BANDS_SCCD; i++)
            {
                states_ensemble[*n_state * 3 * TOTAL_IMAGE_BANDS_SCCD + i] = (double)coefs_records[cur_coefs].nrt_coefs[i][0] + (double)coefs_records[cur_coefs].nrt_coefs[i][1] * days / SLOPE_SCALE;
            }
            for (i = 0; i < TOTAL_IMAGE_BANDS_SCCD; i++)
            {
                states_ensemble[*n_state * 3 * TOTAL_IMAGE_BANDS_SCCD + TOTAL_IMAGE_BANDS_SCCD + i] = (double)(coefs_records[cur_coefs].nrt_coefs[i][2] * cos((double)days * w) + coefs_records[cur_coefs].nrt_coefs[i][3] * sin((double)days * w));
            }
            for (i = 0; i < TOTAL_IMAGE_BANDS_SCCD; i++)
            {
                states_ensemble[*n_state * 3 * TOTAL_IMAGE_BANDS_SCCD + 2 * TOTAL_IMAGE_BANDS_SCCD + i] = (double)(coefs_records[cur_coefs].nrt_coefs[i][4] * cos((double)days * w * 2) + coefs_records[cur_coefs].nrt_coefs[i][5] * sin((double)days * w * 2));
            }
            *n_state = *n_state + 1;
            days = days + state_intervaldays;
            if ((cur_coefs < n_coefs_records - 1) & (days >= coefs_records[cur_coefs + 1].clrx))
            {
                cur_coefs = cur_coefs + 1;
            }
            if (days > clrx[n_clr - conse]) // we will output the states for the last obs that can't reach conse observations
                break;
        }
    }

    free(clrx);
    clrx = NULL;
    status = free_2d_array((void **)clry);
    if (status != SUCCESS)
    {
        RETURN_ERROR("Freeing memory: clry\n", FUNC_NAME, FAILURE);
    }

    free(id_range);
    free(coefs_records);
    return result;
}

// Solve for f so that Pr[F < f] = pr where F has an F distribution with
// v1, v2 degrees of freedom.

double F(int v1, int v2, double pr)
{
    double f0 = 0.0;
    double f = 2.0;
    double diff;
    double delta = 0.1;
    double p;
    int n = 0;

    f = 1.0;
    while ((p = F_Distribution(f, v1, v2)) < pr)
    {
        f += delta;
        if (p > 0.999)
        {
            delta /= 10.0;
            f = (f - delta) / 10;
        }
    }

    f0 = f - delta;
    while ((p = F_Distribution(f0, v1, v2)) > pr)
    {
        f0 -= delta;
        if (p < 0.001)
        {
            delta /= 10.0;
            f0 = (f0 + delta) / 10;
        }
    }

    while (fabs(f - f0) > 1.e-6)
    {
        diff = F_Distribution(f, v1, v2) - pr;
        diff /= F_Density(f, v1, v2);
        diff /= 2.0;
        f0 = f;
        f -= diff;
        n++;
        if (n > 40)
            exit(0);
    }
    return f;
}

int step1_ssm_initialize(
    ssmodel_constants *instance, /* I/O: the outputted initial SSM model, we will assign H     */
    int *clrx,                   /* I: clear pixel curve in X direction (date)             */
    float *clry,                 /* I: clear pixel curve in Y direction (spectralbands)    */
    int stable_start,            /* I:  the start of the stable stage  */
    int stable_end,              /* I:  the start of the stable stage  */
    float **fit_cft,             /*I: the lasso coefficientis */
    gsl_matrix *cov_p,           /* I/O:  initial P1  */
    int i_b,                     /* I:  the band order */
    unsigned int *sum_square_vt, /* I/O:  the sum of predicted square of residuals  */
    int n_clr,
    bool b_coefs_records,
    int *n_coefs_records,
    nrt_coefs_records *coefs_records)
{
    char FUNC_NAME[] = "step1_ssm_initialize";
    float *state_sum;
    float ini_p;
    int k, i;
    double vt;
    int *clrx_extend;
    float *clry_extend;
    int num_year_range = (int)ceil((clrx[stable_end] - clrx[stable_start] + 1) / AVE_DAYS_IN_A_YEAR);
    int stable_nobs = stable_end - stable_start + 1;
    gsl_vector *state_a;
    int n_coefs_records_cp = *n_coefs_records;
    double tmp;

    // we need add an additional obs to allow KF_ts_filter_regular
    clrx_extend = (int *)malloc((stable_nobs * 2 + 1) * sizeof(int));
    if (clrx_extend == NULL)
    {
        RETURN_ERROR("Allocating clrx_extend memory", FUNC_NAME, FAILURE);
    }

    clry_extend = (float *)malloc((stable_nobs * 2 + 1) * sizeof(float));
    if (clrx_extend == NULL)
    {
        RETURN_ERROR("Allocating clry_extend memory", FUNC_NAME, FAILURE);
    }
    state_a = gsl_vector_alloc(instance->m);

    /* generate a copy of observation at the head of clrx_extend and clry_extend */
    //    for (i = 0; i < stable_nobs + EXTEND_OBS  + 1; i++)
    //    {
    //        if (i < EXTEND_OBS)
    //        {
    //            clrx_extend[i] = clrx[stable_start] - EXTEND_OBS_INTERVAL * EXTEND_OBS + EXTEND_OBS_INTERVAL * i;
    //            auto_ts_predict(clrx_extend, fit_cft, SCCD_NUM_C, i_b, i, i, &tmp);

    //            clry_extend[i] = (float)floor(tmp);
    //        }else{
    //            clrx_extend[i] = clrx[stable_start + i - EXTEND_OBS];
    //            clry_extend[i] = clry[stable_start + i - EXTEND_OBS];
    //        }
    //        // printf("i = %d, clrx = %d, clry = %d \n", i, clrx_extend[i], (int)clry_extend[i]);

    //    }
    for (i = 0; i < stable_nobs * 2 + 1; i++)
    {
        if (i < stable_nobs)
        {
            clrx_extend[i] = (int)(clrx[stable_start + i] - num_year_range * AVE_DAYS_IN_A_YEAR);
            // auto_ts_predict(clrx_extend, fit_cft, SCCD_NUM_C, i_b, i, i, &tmp);
            // clry_extend[i] = (float)tmp;
            clry_extend[i] = (float)clry[stable_start + i] - num_year_range * AVE_DAYS_IN_A_YEAR * fit_cft[i_b][1] / SLOPE_SCALE;
            // clry_extend[i] = (float)clry[stable_start + i];
        }
        else
        {
            if (stable_start + i - stable_nobs > n_clr - 1)
            {
                clrx_extend[i] = clrx[n_clr - 1];
                clry_extend[i] = clry[n_clr - 1];
            }
            else
            {
                clrx_extend[i] = clrx[stable_start + i - stable_nobs];
                clry_extend[i] = clry[stable_start + i - stable_nobs];
            }
        }

        // printf("i = %d, clrx = %d, clry = %d \n", i, clrx_extend[i], (int)clry_extend[i]);
    }

    //    printf("fit_cft[0][0]: %f\n", fit_cft[i_b][0]);
    //    printf("fit_cft[0][1]: %f\n", fit_cft[i_b][1]);
    //    printf("fit_cft[0][2]: %f\n", fit_cft[i_b][2]);
    //    printf("fit_cft[0][3]: %f\n", fit_cft[i_b][3]);
    //    printf("fit_cft[0][4]: %f\n", fit_cft[i_b][4]);
    //    printf("fit_cft[0][5]: %f\n", fit_cft[i_b][5]);
    //    fit_cft2vec_a(fit_cft, state_a, clrx[stable_start]);
    //    vec_a2fit_cft(state_a, fit_cft, clrx[stable_start]);
    //    printf("fit_cft[0][0]: %f\n", fit_cft[0]);
    //    printf("fit_cft[0][1]: %f\n", fit_cft[1]);
    //    printf("fit_cft[0][2]: %f\n", fit_cft[2]);
    //    printf("fit_cft[0][3]: %f\n", fit_cft[3]);
    //    printf("fit_cft[0][4]: %f\n", fit_cft[4]);
    //    printf("fit_cft[0][5]: %f\n", fit_cft[5]);

    /* assign memory and initialize them to zero */
    state_sum = (float *)calloc(instance->m, sizeof(float));
    if (state_sum == NULL)
    {
        RETURN_ERROR("Allocating state_sum memory", FUNC_NAME, FAILURE);
    }

    /************************************************************************************************/
    /* first step: update a and p between prev_i_break - 1(included) and stable_start(not included) */
    /************************************************************************************************/

    /* initialize a1 */
    // fit_cft2vec_a(fit_cft[i_b], state_a, clrx[stable_start], instance->m, instance->structure);
    /*  initialize p */
    // ini_p = caculate_ini_p(instance->m, state_a, instance->Z);
    // ini_p = INI_P;
    ini_p = pow((fit_cft[i_b][1] * clrx_extend[stable_nobs] / SLOPE_SCALE + fit_cft[i_b][0]), 2) * INITIAL_P_RATIO;
    // ini_p = pow(clry_extend[0], 2) * INITIAL_P_RATIO;
    for (k = 0; k < instance->m; k++)
    {
        if (k == 1)
        {
            gsl_matrix_set(cov_p, k, k, ini_p / SLOPE_SS_SCALE);
        }
        else
        {
            gsl_matrix_set(cov_p, k, k, ini_p);
        }
    }

    //        printf("instance->Q[1] = %f\n", gsl_matrix_get(instance->Q, 1, 1));
    //        printf("instance->Q[2] = %f\n", gsl_matrix_get(instance->Q, 2, 2));
    //        printf("instance->Q[3] = %f\n", gsl_matrix_get(instance->Q, 3, 3));
    //        printf("instance->Q[4] = %f\n", gsl_matrix_get(instance->Q, 4, 4));
    //        printf("instance->Q[5] = %f\n", gsl_matrix_get(instance->Q, 5, 5));
    //        printf("instance->H = %f\n", instance->H);

    /********************************************************/
    /*     running regular kalman filter for stable stage   */
    /********************************************************/
    *sum_square_vt = 0;
    for (i = 0; i < 2 * stable_nobs; i++)
    {
        KF_ts_filter_regular(instance, clrx_extend, clry_extend, cov_p, fit_cft, i, i_b, &vt, FALSE);
        *sum_square_vt = *sum_square_vt + (unsigned int)(vt * vt);
        if (i > stable_nobs - 1)
        {

            if (b_coefs_records == TRUE)
            {
                coefs_records[n_coefs_records_cp].clrx = clrx_extend[i];
                for (k = 0; k < SCCD_NUM_C; k++)
                {
                    coefs_records[n_coefs_records_cp].nrt_coefs[i_b][k] = fit_cft[i_b][k];
                }

                n_coefs_records_cp = n_coefs_records_cp + 1;
            }
        }
    }
    *sum_square_vt = (*sum_square_vt) / 2.0;
    if (i_b == (TOTAL_IMAGE_BANDS_SCCD - 1))
        *n_coefs_records = n_coefs_records_cp;

    //    for(i = 0; i < stable_nobs + EXTEND_OBS; i++){
    //        KF_ts_filter_regular(instance, clrx_extend, clry_extend, cov_p,fit_cft, i, i_b, &vt);
    //        if (i > EXTEND_OBS - 1)
    //            *sum_square_vt = *sum_square_vt + vt * vt;
    //    }
    //    for(i = stable_start; i < stable_end + 1; i++){
    //        KF_ts_filter_regular(instance, clrx, clry, cov_p,fit_cft, i, i_b, &vt);
    //        *sum_square_vt = *sum_square_vt + vt * vt;
    //    }

    //    for(i = 1; i < 6; i++)
    //        printf("instance->Q: %f\n", gsl_matrix_get(instance->Q, i, i));

    //    printf("instance->H: %f\n", instance->H);

    /* free memory*/
    free(state_sum);
    free(clrx_extend);
    free(clry_extend);
    gsl_vector_free(state_a);
    return SUCCESS;
}

int step1_cold_initialize(
    int conse,           /* I: adjusted consecutive observation number               */
    short int *min_rmse, /* I: the adjusted RMS                        */
    int *n_clr,          /* I: number of clear observations                         */
    double tcg,          /* I: the threshold of change magnitude                       */
    int *i_dense,        /* I: used to count i for dense time point check          */
    int *num_curve,      /* I/O: the number of fitting curve                        */
    int *clrx,           /* I/O: clear pixel curve in X direction (date)             */
    float **clry,        /* I/O: clear pixel curve in Y direction (spectralbands)    */
    int *cur_i,          /* I/O: the current number of monitoring observation          */
    int *i_start,        /* I/O: the start number of current curve                   */
    Output_sccd *rec_cg, /* I/O: records of change points info                    */
    int i_span_min,      /* I: the minimum value for i_span                    */
    int *prev_i_break,   /*I : the i_break of the last curve                    */
    float *rmse,         /* I/O: Root Mean Squared Error array used for initialized kalman filter model    */
    double lambda)
{
    int status;
    int k, m, b;
    int i_b;
    int *bl_ids, *ids;
    int *rm_ids;
    int i_span;
    int rm_ids_len;
    int *cpx;
    float **cpy;
    int k_new;
    int i_rec;
    float v_dif_norm;

    double time_span;
    float mini_rmse; /* Mimimum RMSE                          */
    float *v_start;  /* Vector for start of observation(s)    */
    float *v_end;    /* Vector for n_clr of observastion(s)     */
    float *v_slope;  /* Vector for astandardized slope values   */
    float *v_dif;    /* Vector for difference values          */
    float **v_diff;
    float *vec_magg; /* this one is never freed */
    float vec_magg_min;
    float **v_dif_mag; /* vector for magnitude of differences.  */
    float **v_dif_magg;
    int i_conse;
    int ini_conse;
    int i_ini;
    float ts_pred_temp;
    float **tmp_v_dif; /* temporal regression difference       */
    float **rec_v_dif;
    float v_dif_mean;
    float **fit_cft; /* I/O: Fitted coefficients 2-D array.                   */
    float **fit_cft_tmp;
    float mean_angle; /* I: mean angle of vec_diff                              */
    char FUNC_NAME[] = "step1_cold_initialize";
    int update_num_c;
    int max_date_diff = 0;
    int tmp_end;
    // i_dense = *i_start;

    if (*cur_i < N_TIMES * MID_NUM_C - 1)
    {
        return INCOMPLETE;
    }

    /****************************************************/
    /*                                                  */
    /*     allocac memory for variables                 */
    /*                                                  */
    /****************************************************/
    rec_v_dif = (float **)allocate_2d_array(TOTAL_IMAGE_BANDS_SCCD, *n_clr,
                                            sizeof(float));
    if (rec_v_dif == NULL)
    {
        RETURN_ERROR("Allocating rec_v_dif memory", FUNC_NAME, FAILURE);
    }

    ids = (int *)malloc(*n_clr * sizeof(int));
    if (ids == NULL)
    {
        RETURN_ERROR("ERROR allocating ids memory", FUNC_NAME, FAILURE);
    }

    bl_ids = (int *)malloc(*n_clr * sizeof(int));
    if (bl_ids == NULL)
    {
        RETURN_ERROR("ERROR allocating bl_ids memory", FUNC_NAME, FAILURE);
    }

    rm_ids = (int *)malloc(*n_clr * sizeof(int));
    if (rm_ids == NULL)
    {
        RETURN_ERROR("ERROR allocating rm_ids memory", FUNC_NAME, FAILURE);
    }

    v_start = (float *)malloc(NUM_LASSO_BANDS * sizeof(float));
    if (v_start == NULL)
    {
        RETURN_ERROR("ERROR allocating v_start memory", FUNC_NAME, FAILURE);
    }

    v_end = (float *)malloc(NUM_LASSO_BANDS * sizeof(float));
    if (v_end == NULL)
    {
        RETURN_ERROR("ERROR allocating v_end memory", FUNC_NAME, FAILURE);
    }

    v_slope = (float *)malloc(NUM_LASSO_BANDS * sizeof(float));
    if (v_slope == NULL)
    {
        RETURN_ERROR("ERROR allocating v_slope memory", FUNC_NAME, FAILURE);
    }

    v_dif = (float *)malloc(NUM_LASSO_BANDS * sizeof(float));
    if (v_dif == NULL)
    {
        RETURN_ERROR("ERROR allocating v_dif memory", FUNC_NAME, FAILURE);
    }

    tmp_v_dif = (float **)allocate_2d_array(TOTAL_IMAGE_BANDS_SCCD, *n_clr,
                                            sizeof(float));
    if (tmp_v_dif == NULL)
    {
        RETURN_ERROR("Allocating tmp_v_dif memory", FUNC_NAME, FAILURE);
    }

    v_dif_mag = (float **)allocate_2d_array(TOTAL_IMAGE_BANDS_SCCD, conse,
                                            sizeof(float));
    if (v_dif_mag == NULL)
    {
        RETURN_ERROR("Allocating v_dif_mag memory",
                     FUNC_NAME, FAILURE);
    }

    fit_cft = (float **)allocate_2d_array(TOTAL_IMAGE_BANDS_SCCD, SCCD_NUM_C, sizeof(float));
    if (fit_cft == NULL)
    {
        RETURN_ERROR("Allocating fit_cft memory", FUNC_NAME, FAILURE);
    }

    /*************************************************  */
    /*                                                  */
    /*  check maximum time gap as first                 */
    /*                                                  */
    /****************************************************/

    for (k = *i_start; k < *cur_i; k++)
    {
        if (clrx[k + 1] - clrx[k] > max_date_diff)
        {
            max_date_diff = clrx[k + 1] - clrx[k];
        }
    }

    if (max_date_diff > NUM_YEARS) // SY 09192018
    {
        // *cur_i = *cur_i + 1;
        *i_start = *i_start + 1;
        *i_dense = *i_dense + 1;

        status = free_2d_array((void **)rec_v_dif);
        if (status != SUCCESS)
        {
            RETURN_ERROR("Freeing memory: rec_v_dif\n",
                         FUNC_NAME, FAILURE);
        }
        status = free_2d_array((void **)fit_cft);
        if (status != SUCCESS)
        {
            RETURN_ERROR("Freeing memory: fit_cft\n",
                         FUNC_NAME, FAILURE);
        }

        free(ids);
        free(bl_ids);
        free(rm_ids);
        free(v_start);
        free(v_end);
        free(v_slope);
        free(v_dif);

        status = free_2d_array((void **)tmp_v_dif);
        if (status != SUCCESS)
        {
            RETURN_ERROR("Freeing memory: tmp_v_dif\n",
                         FUNC_NAME, FAILURE);
        }

        status = free_2d_array((void **)v_dif_mag);
        if (status != SUCCESS)
        {
            RETURN_ERROR("Freeing memory: v_dif_mag\n",
                         FUNC_NAME, FAILURE);
        }

        return INCOMPLETE;
    }
    /*************************************************  */
    /*                                                  */
    /* Step 2: noise removal.                           */
    /*                                                  */
    /****************************************************/
    tmp_end = min(*cur_i + conse - 1, *n_clr - 1);
    status = auto_mask(clrx, clry, *i_start, tmp_end, (double)(clrx[tmp_end] - clrx[*i_start]) / NUM_YEARS,
                       min_rmse[1], min_rmse[4], SCCD_T_CONST, bl_ids, 2, 5);
    if (status != SUCCESS)
    {
        RETURN_ERROR("ERROR calling auto_mask during model initilization",
                     FUNC_NAME, FAILURE);
    }

    /**************************************************/
    /*                                                */
    /* Clear the IDs buffers.                         */
    /*                                                */
    /**************************************************/

    for (k = 0; k < *n_clr; k++)
        ids[k] = 0;

    /**************************************************/
    /*                                                */
    /* IDs to be removed.                             */
    /*                                                */
    /**************************************************/

    for (k = *i_start; k < *cur_i + 1; k++)
    {
        ids[k - *i_start] = k;
    }

    m = 0;

    i_span = 0;

    for (k = 0; k < *cur_i - *i_start + 1; k++)
    {
        if (bl_ids[k] == 1)
        {
            rm_ids[m] = ids[k];
            m++;
        }
        else
            i_span++; /* update i_span after noise removal */
    }

    rm_ids_len = m;

    /**************************************************/
    /*                                                */
    /* Check if there are enough observation.         */
    /*                                                */
    /**************************************************/

    if (i_span < i_span_min)
    {
        /**********************************************/
        /*                                            */
        /* Move forward to the i+1th clear observation*/
        /*                                            */
        /**********************************************/

        // *cur_i= *cur_i + 1;

        /**********************************************/
        /*                                            */
        /* Not enough clear observations.             */
        /*                                            */
        /**********************************************/
        status = free_2d_array((void **)rec_v_dif);
        if (status != SUCCESS)
        {
            RETURN_ERROR("Freeing memory: rec_v_dif\n",
                         FUNC_NAME, FAILURE);
        }
        status = free_2d_array((void **)fit_cft);
        if (status != SUCCESS)
        {
            RETURN_ERROR("Freeing memory: fit_cft\n",
                         FUNC_NAME, FAILURE);
        }

        free(ids);
        free(bl_ids);
        free(rm_ids);
        free(v_start);
        free(v_end);
        free(v_slope);
        free(v_dif);

        status = free_2d_array((void **)tmp_v_dif);
        if (status != SUCCESS)
        {
            RETURN_ERROR("Freeing memory: tmp_v_dif\n",
                         FUNC_NAME, FAILURE);
        }

        status = free_2d_array((void **)v_dif_mag);
        if (status != SUCCESS)
        {
            RETURN_ERROR("Freeing memory: v_dif_mag\n",
                         FUNC_NAME, FAILURE);
        }

        return INCOMPLETE;
    }

    if (*n_clr == 0)
        RETURN_ERROR("No available data point", FUNC_NAME, FAILURE);

    /**************************************************/
    /*                                                */
    /* Allocate memory for cpx, cpy.                  */
    /*                                                */
    /**************************************************/

    cpx = malloc((*n_clr) * sizeof(int));
    if (cpx == NULL)
        RETURN_ERROR("ERROR allocating cpx memory", FUNC_NAME, FAILURE);

    cpy = (float **)allocate_2d_array(TOTAL_IMAGE_BANDS_SCCD, *n_clr,
                                      sizeof(float));
    if (cpy == NULL)
    {
        RETURN_ERROR("Allocating cpy memory", FUNC_NAME, FAILURE);
    }

    /**************************************************/
    /*                                                */
    /* Remove noise pixels between i_start & i.       */
    /*                                                */
    /**************************************************/

    m = 0;
    for (k = 0, k_new = 0; k < *n_clr; k++)
    {
        if (m < rm_ids_len && k == rm_ids[m])
        {
            m++;
            continue;
        }
        cpx[k_new] = clrx[k];
        for (b = 0; b < TOTAL_IMAGE_BANDS_SCCD; b++)
        {
            cpy[b][k_new] = clry[b][k];
        }
        k_new++;
    }

    /**************************************************/
    /*                                                */
    /* Record i before noise removal.                 */
    /* This is very important, ie model is not yet    */
    /* initialized.   The multitemporal masking shall */
    /* be done again instead of removing outliers  In */
    /* every masking.                                 */
    /*                                                */
    /**************************************************/

    i_rec = *cur_i;

    /**************************************************/
    /*                                                */
    /* Update i afer noise removal.                   */
    /*     (i_start stays the same).                  */
    /*                                                */
    /**************************************************/

    *cur_i = *i_start + i_span - 1;

    /**************************************************/
    /*                                                */
    /* Update span of time (num of years).            */
    /*                                                */
    /**************************************************/

    time_span = (cpx[*cur_i] - cpx[*i_start]) / NUM_YEARS;

    /**************************************************/
    /*                                                */
    /* Check if there is enough time.                 */
    /*                                                */
    /**************************************************/

    if (time_span < MIN_YEARS)
    {
        *cur_i = i_rec; /* keep the original i */

        /**********************************************/
        /*                                            */
        /* Move forward to the i+1th clear observation*/
        /*                                            */
        /**********************************************/

        // *cur_i= *cur_i + 1;

        status = free_2d_array((void **)rec_v_dif);
        if (status != SUCCESS)
        {
            RETURN_ERROR("Freeing memory: rec_v_dif\n",
                         FUNC_NAME, FAILURE);
        }

        status = free_2d_array((void **)fit_cft);
        if (status != SUCCESS)
        {
            RETURN_ERROR("Freeing memory: fit_cft\n",
                         FUNC_NAME, FAILURE);
        }

        free(ids);
        free(bl_ids);
        free(rm_ids);
        //    free(rmse);
        //    rmse = NULL;
        free(v_start);
        free(v_end);
        free(v_slope);
        free(v_dif);

        status = free_2d_array((void **)tmp_v_dif);
        if (status != SUCCESS)
        {
            RETURN_ERROR("Freeing memory: tmp_v_dif\n",
                         FUNC_NAME, FAILURE);
        }

        status = free_2d_array((void **)v_dif_mag);
        if (status != SUCCESS)
        {
            RETURN_ERROR("Freeing memory: v_dif_mag\n",
                         FUNC_NAME, FAILURE);
        }

        free(cpx);
        status = free_2d_array((void **)cpy);
        if (status != SUCCESS)
        {
            RETURN_ERROR("Freeing memory: cpy\n",
                         FUNC_NAME, FAILURE);
        }

        return INCOMPLETE; /* not enough time */
    }

    // SY 09272018

    /**************************************************/
    /*                                                */
    /* Remove noise in original arrays.               */
    /*                                                */
    /**************************************************/
    *n_clr = k_new;
    for (k = 0; k < *n_clr; k++)
    {
        clrx[k] = cpx[k];
        for (m = 0; m < TOTAL_IMAGE_BANDS_SCCD; m++)
        {
            clry[m][k] = cpy[m][k];
        }
    }

    free(cpx);
    status = free_2d_array((void **)cpy);
    if (status != SUCCESS)
    {
        RETURN_ERROR("Freeing memory: cpy\n",
                     FUNC_NAME, FAILURE);
    }

    /**************************************************/
    /*                                                */
    /* Step 3) model fitting: initialize model testing*/
    /*         variables defining computed variables. */
    /*                                                */
    /**************************************************/
    //    if (*cur_i - *i_start + 1 > N_TIMES * SCCD_NUM_C - 1)
    //       update_num_c = SCCD_NUM_C;
    //    else
    update_num_c = MIN_NUM_C;

    // update_num_c = MIN_NUM_C;

    for (b = 0; b < TOTAL_IMAGE_BANDS_SCCD; b++)
    {
        /**********************************************/
        /*                                            */
        /* Initial model fit.                         */
        /*                                            */
        /**********************************************/

        status = auto_ts_fit_sccd(clrx, clry, b, b, *i_start, *cur_i,
                                  update_num_c, fit_cft, &rmse[b], rec_v_dif, lambda);

        if (status != SUCCESS)
        {
            RETURN_ERROR("Calling auto_ts_fit_sccd during model initilization\n",
                         FUNC_NAME, FAILURE);
        }
    }

    v_dif_norm = 0.0;

    for (i_b = 0; i_b < NUM_LASSO_BANDS; i_b++)
    {

        /**********************************************/
        /*                                            */
        /* Calculate min. rmse.                       */
        /*                                            */
        /**********************************************/

        mini_rmse = max(min_rmse[lasso_blist_sccd[i_b]], rmse[lasso_blist_sccd[i_b]]);
        // mini_rmse = rmse[lasso_blist_sccd[i_b]];
        /**********************************************/
        /*                                            */
        /* Compare the first observation.             */
        /*                                            */
        /**********************************************/

        v_start[i_b] = (rec_v_dif[lasso_blist_sccd[i_b]][0]) / mini_rmse;

        /**********************************************/
        /*                                            */
        /* Compare the last clear observation.        */
        /*                                            */
        /**********************************************/

        v_end[i_b] = rec_v_dif[lasso_blist_sccd[i_b]][*cur_i - *i_start] / mini_rmse;

        /**********************************************/
        /*                                            */
        /* Astandardized slope values.                  */
        /*                                            */
        /**********************************************/
        v_slope[i_b] = fit_cft[lasso_blist_sccd[i_b]][1] *
                       (clrx[*cur_i] - clrx[*i_start]) / mini_rmse / SLOPE_SCALE;

        /**********************************************/
        /*                                            */
        /* Difference in model intialization.         */
        /*                                            */
        /**********************************************/

        v_dif[i_b] = fabs(v_slope[i_b]) + max(fabs(v_start[i_b]), fabs(v_end[i_b]));
        // v_dif[i_b] = fabs(v_slope[i_b]) + 1;
        v_dif_norm += v_dif[i_b] * v_dif[i_b];
    }

    /**************************************************/
    /*                                                */
    /* Find stable start for each curve.              */
    /*                                                */
    /**************************************************/
    if (v_dif_norm > tcg)
    {
        /**********************************************/
        /*                                            */
        /* Start from next clear observation.         */
        /*                                            */
        /**********************************************/

        *i_start = *i_start + 1;
        /**********************************************/
        /*                                            */
        /* Move forward to the i+1th clear observation*/
        /*                                            */
        /**********************************************/

        //*cur_i = *cur_i + 1;

        /**********************************************/
        /*                                            */
        /* Keep all data and move to the next obs.    */
        /*                                            */
        /**********************************************/

        status = free_2d_array((void **)rec_v_dif);
        if (status != SUCCESS)
        {
            RETURN_ERROR("Freeing memory: rec_v_dif\n",
                         FUNC_NAME, FAILURE);
        }

        status = free_2d_array((void **)fit_cft);
        if (status != SUCCESS)
        {
            RETURN_ERROR("Freeing memory: fit_cft\n",
                         FUNC_NAME, FAILURE);
        }

        free(ids);
        free(bl_ids);
        free(rm_ids);
        //    free(rmse);
        //    rmse = NULL;
        free(v_start);
        free(v_end);
        free(v_slope);
        free(v_dif);

        status = free_2d_array((void **)tmp_v_dif);
        if (status != SUCCESS)
        {
            RETURN_ERROR("Freeing memory: tmp_v_dif\n",
                         FUNC_NAME, FAILURE);
        }

        status = free_2d_array((void **)v_dif_mag);
        if (status != SUCCESS)
        {
            RETURN_ERROR("Freeing memory: v_dif_mag\n",
                         FUNC_NAME, FAILURE);
        }

        return INCOMPLETE;
    }

    /**************************************************/
    /*                                                */
    /* Step 4) look back: to include fitting points   */
    /*         and find change points.                */
    /*                                                */
    /**************************************************/
    if (*num_curve == 0)
    {
        *prev_i_break = *i_dense;
    }

    if (*i_start > *prev_i_break)
    {
        /**********************************************/
        /*                                            */
        /* Model fit at the beginning of the time     */
        /* series.                                    */
        /*                                            */
        /**********************************************/

        for (i_ini = *i_start - 1; i_ini >= *prev_i_break; i_ini--) // SY 09192018
        {
            // printf("ini is %d\n", i_ini);
            if (i_ini - *prev_i_break + 1 < conse)
            {
                ini_conse = i_ini - *prev_i_break + 1;
            }
            else
            {
                ini_conse = conse;
            }

            if (ini_conse == 0)
            {
                RETURN_ERROR("No data point for model fit at "
                             "the begining",
                             FUNC_NAME, FAILURE);
            }

            /******************************************/
            /*                                        */
            /* Allocate memory for model_v_dif,       */
            /* v_diff, vec_magg for the non-stdin     */
            /* branch here.                           */
            /*                                        */
            /******************************************/

            v_diff = (float **)allocate_2d_array(NUM_LASSO_BANDS,
                                                 ini_conse, sizeof(float));
            if (v_diff == NULL)
            {
                RETURN_ERROR("Allocating v_diff memory",
                             FUNC_NAME, FAILURE);
            }

            vec_magg = (float *)malloc(ini_conse * sizeof(float));
            if (vec_magg == NULL)
            {
                RETURN_ERROR("Allocating vec_magg memory",
                             FUNC_NAME, FAILURE);
            }

            /******************************************/
            /*                                        */
            /* Detect change.                         */
            /* value of difference for conse          */
            /* Record the magnitude of change.        */
            /*                                        */
            /******************************************/

            vec_magg_min = 9999.0;
            for (i_conse = 1; i_conse < ini_conse + 1; i_conse++) // SY 09192018
            {
                v_dif_norm = 0.0;
                for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                {

                    /**********************************/
                    /*                                */
                    /* Absolute differences.          */
                    /*                                */
                    /**********************************/

                    // SY 09192018 moving fitting into (i_b == lasso_blist_sccd[b])to save time //
                    // SY 02/13/2019 delete these speed-up modification as non-lasso bands
                    // are important for change agent classification
                    // printf("i_b = %d\n", i_b);
                    auto_ts_predict_float(clrx, fit_cft, update_num_c, i_b, i_ini - i_conse + 1,
                                          i_ini - i_conse + 1, &ts_pred_temp);
                    v_dif_mag[i_b][i_conse - 1] = (float)clry[i_b][i_ini - i_conse + 1] -
                                                  ts_pred_temp; // SY 09192018

                    /**********************************/
                    /*                                */
                    /* standardize to z-score.          */
                    /*                                */
                    /**********************************/

                    for (b = 0; b < NUM_LASSO_BANDS; b++)
                    {
                        if (i_b == lasso_blist_sccd[b])
                        {
                            /**************************/
                            /*                        */
                            /* Minimum rmse.          */
                            /*                        */
                            /**************************/

                            mini_rmse = max(min_rmse[i_b], rmse[i_b]);

                            /**************************/
                            /*                        */
                            /* z-scores.              */
                            /*                        */
                            /**************************/

                            v_diff[b][i_conse - 1] = v_dif_mag[i_b][i_conse - 1] // SY 09192018
                                                     / mini_rmse;
                            v_dif_norm += v_diff[b][i_conse - 1] * v_diff[b][i_conse - 1]; // SY 09192018
                        }
                    }
                }

                vec_magg[i_conse - 1] = v_dif_norm; // SY 09192018

                if (vec_magg_min > vec_magg[i_conse - 1])
                {
                    vec_magg_min = vec_magg[i_conse - 1]; // SY 09192018
                }
            }

            /******************************************/
            /*                                        */
            /* Change angle.                      */
            /*                                        */
            /******************************************/

            mean_angle = MeanAngl_float(v_diff, NUM_LASSO_BANDS, ini_conse);

            if ((vec_magg_min > tcg) && (mean_angle < NSIGN)) /* i_start found*/
            {
                free(vec_magg);
                status = free_2d_array((void **)v_diff);
                if (status != SUCCESS)
                {
                    RETURN_ERROR("Freeing memory: v_diff\n",
                                 FUNC_NAME, FAILURE);
                }
                break;
            }
            else if ((vec_magg[0] > T_MAX_CG_SCCD) && (i_ini >= *prev_i_break)) /* false change */
            {
                for (k = i_ini; k < *n_clr - 1; k++)
                {
                    clrx[k] = clrx[k + 1];
                    for (b = 0; b < TOTAL_IMAGE_BANDS_SCCD; b++)
                    {
                        clry[b][k] = clry[b][k + 1];
                    }
                }
                *cur_i = *cur_i - 1;
                *n_clr = *n_clr - 1;
            }

            /**************************************/
            /*                                    */
            /* Update i_start if i_ini is not a   */
            /* confirmed break.                   */
            /*                                    */
            /**************************************/

            *i_start = i_ini;

            /******************************************/
            /*                                        */
            /* Free the temporary memory.             */
            /*                                        */
            /******************************************/

            free(vec_magg);
            status = free_2d_array((void **)v_diff);
            if (status != SUCCESS)
            {
                RETURN_ERROR("Freeing memory: v_diff\n",
                             FUNC_NAME, FAILURE);
            }
        } //  for (i_ini = i_start-1; i_ini >= prev_i_break; i_ini--)
    } //  for if (i_start > prev_i_break)

    /**************************************************/
    /*                                                */
    /* Enough to fit simple model and confirm a break.*/
    /*                                                */
    /**************************************************/
    /* fit all curve 09102019 SY */
    if (*num_curve == 0 && *i_start - *i_dense >= LASSO_MIN)
    {
        /**********************************************/
        /*                                            */
        /* Defining computed variables.               */
        /*                                            */
        /**********************************************/
        // printf("%d\n", conse);
        fit_cft_tmp = (float **)allocate_2d_array(TOTAL_IMAGE_BANDS_SCCD, SCCD_NUM_C, sizeof(float));
        if (fit_cft_tmp == NULL)
        {
            RETURN_ERROR("Allocating fit_cft_tmp memory", FUNC_NAME, FAILURE);
        }
        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
        {
            if (*num_curve == 0)
                status = auto_ts_fit_sccd(clrx, clry, i_b, i_b, *i_dense, *i_start,
                                          MIN_NUM_C, fit_cft_tmp, &rmse[i_b], tmp_v_dif, lambda);
            else
                status = auto_ts_fit_sccd(clrx, clry, i_b, i_b, *prev_i_break, *i_start,
                                          MIN_NUM_C, fit_cft_tmp, &rmse[i_b], tmp_v_dif, lambda); // SY 09182018
            if (status != SUCCESS)
            {
                RETURN_ERROR("Calling auto_ts_fit_sccd with enough observations\n",
                             FUNC_NAME, FAILURE);
            }
        }

        ini_conse = conse;

        v_dif_magg = (float **)allocate_2d_array(TOTAL_IMAGE_BANDS_SCCD,
                                                 ini_conse, sizeof(float));
        if (v_dif_magg == NULL)
        {
            RETURN_ERROR("Allocating v_dif_magg memory",
                         FUNC_NAME, FAILURE);
        }

        for (i_conse = 1; i_conse < ini_conse + 1; i_conse++) // SY 09192018
        {
            v_dif_norm = 0.0;
            for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
            {
                auto_ts_predict_float(clrx, fit_cft, MIN_NUM_C, i_b, *i_start - i_conse,
                                      *i_start - i_conse, &ts_pred_temp);
                v_dif_magg[i_b][i_conse - 1] = (float)clry[i_b][*i_start - i_conse] -
                                               ts_pred_temp; // SY 09192018
            }
        }

        // rec_cg[*num_curve].t_end = clrx[*i_start-1];
        /**********************************************/
        /*                                            */
        /* Record break time, fit category, change    */
        /* probability, time of curve start, number   */
        /* of observations, change magnitude.         */
        /*                                            */
        /**********************************************/
        rec_cg[*num_curve].t_break = clrx[*i_start];
        rec_cg[*num_curve].t_start = clrx[0];
        rec_cg[*num_curve].num_obs = *i_start - *prev_i_break; // SY 09182018
        *prev_i_break = *i_start;

        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
        {
            quick_sort_float(v_dif_magg[i_b], 0, ini_conse - 1);
            matlab_2d_float_median(v_dif_magg, i_b, ini_conse,
                                   &v_dif_mean);
            mini_rmse = max((float)min_rmse[i_b], rmse[i_b]);
            rec_cg[*num_curve].magnitude[i_b] = (float)(-v_dif_mean);
            // rec_cg[*num_curve].magnitude[i_b] = -v_dif_mean;
        }

        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
        {
            for (k = 0; k < SCCD_NUM_C; k++)
            {
                /**************************************/
                /*                                    */
                /* Record fitted coefficients.        */
                /*                                    */
                /**************************************/
                rec_cg[*num_curve].coefs[i_b][k] = fit_cft_tmp[i_b][k];
            }

            /******************************************/
            /*                                        */
            /* Record rmse of the pixel.              */
            /*                                        */
            /******************************************/

            rec_cg[*num_curve].rmse[i_b] = rmse[i_b];
        }

        /**********************************************/
        /*                                            */
        /* Identified and move on for the next        */
        /* functional curve.                          */
        /*                                            */
        /**********************************************/
        status = free_2d_array((void **)fit_cft_tmp);
        if (status != SUCCESS)
        {
            RETURN_ERROR("Freeing memory: fit_cft_tmp\n", FUNC_NAME, FAILURE);
        }

        *num_curve = *num_curve + 1;

        status = free_2d_array((void **)v_dif_magg);
        if (status != SUCCESS)
        {
            RETURN_ERROR("Freeing memory: v_diff\n",
                         FUNC_NAME, FAILURE);
        }
    }

    status = free_2d_array((void **)rec_v_dif);
    if (status != SUCCESS)
    {
        RETURN_ERROR("Freeing memory: rec_v_dif\n",
                     FUNC_NAME, FAILURE);
    }

    free(ids);
    free(bl_ids);
    free(rm_ids);
    //    free(rmse);
    //    rmse = NULL;
    free(v_start);
    free(v_end);
    free(v_slope);
    free(v_dif);

    status = free_2d_array((void **)fit_cft);
    if (status != SUCCESS)
    {
        RETURN_ERROR("Freeing memory: fit_cft", FUNC_NAME, FAILURE);
    }

    status = free_2d_array((void **)tmp_v_dif);
    if (status != SUCCESS)
    {
        RETURN_ERROR("Freeing memory: tmp_v_dif\n",
                     FUNC_NAME, FAILURE);
    }

    status = free_2d_array((void **)v_dif_mag);
    if (status != SUCCESS)
    {
        RETURN_ERROR("Freeing memory: v_dif_mag\n",
                     FUNC_NAME, FAILURE);
    }

    return (SUCCESS);
}

/************************************************************************
FUNCTION: step2_KF_ChangeDetection

PURPOSE:
Step 2 of S-CCD: change detection using kalman filter.
RETURN VALUE:
Type = int (SUCCESS OR FAILURE)

Programmer: Su Ye
**************************************************************************/
int step2_KF_ChangeDetection(
    ssmodel_constants *instance, /* I: ssm constant structure */
    int *clrx,                   /* I: dates   */
    float **clry,                /* I: observations   */
    int cur_i,                   /* I: the ith of observation to be processed   */
    int i_start,                 /* I: the ith of observation that the segment starts   */
    int *num_curve,              /* I: the number of curves   */
    int conse,                   /* I: the consecutive number of observations   */
    short int *min_rmse,         /* I: adjusted RMSE   */
    float tcg,                   /* I: the change threshold  */
    int *n_clr,                  /* I: the total observation of current observation queue  */
    gsl_matrix **cov_p,          /* I/O: covariance matrix */
    float **fit_cft,             /* I/O: state variables  */
    Output_sccd *rec_cg,         /* I/O: the outputted S-CCD result structure   */
    unsigned int *sum_square_vt, /* I/O:  the sum of predicted square of residuals  */
    int *num_obs_processed,      /* I/O:  the number of current non-noise observations being processed */
    int t_start,
    bool output_anomaly,
    Output_sccd_anomaly *rec_cg_anomaly, /* O: historical change records for SCCD results    */
    int *num_fc_anomaly,
    double anomaly_tcg,
    short int *norm_cm_scale100,
    short int *mean_angle_scale100,
    float *CM_outputs,
    float t_max_cg_sccd,
    bool b_coefs_records,
    int *n_coefs_records,
    nrt_coefs_records *coefs_records,
    bool fitting_coefs,
    double lambda,
    int anomaly_conse)
{
    int i_b, b, m, k, j;
    int status;
    int i_conse;
    // int j_conse;
    float pred_y;
    float pred_y_f;
    char FUNC_NAME[] = "step2_KF_ChangeDetection";
    float **v_dif_mag;
    float **v_dif;
    float *v_dif_mag_norm;
    // bool grad_change_flag;
    int RETURN_VALUE;
    // double c0, c1;
    float *medium_v_dif;
    float max_rmse[TOTAL_IMAGE_BANDS_SCCD];
    bool change_flag = TRUE;
    float mean_angle = 0;
    float tmp;
    double vt;
    float rmse_band[TOTAL_IMAGE_BANDS_SCCD];
    bool steady = FALSE;
    float break_mag = 9999.0;
    short int tmp_CM = -9999;
    int conse_last;
    float **v_diff_tmp;
    float **v_dif_mag_tmp;
    int current_CM_n;
    int current_anomaly;
    float tmp_rmse;
    float **temp_v_dif; /* temperory residual for per-pixel      */

    v_dif = (float **)allocate_2d_array(NUM_LASSO_BANDS, conse, sizeof(float));
    if (v_dif == NULL)
    {
        RETURN_ERROR("Allocating v_dif memory",
                     FUNC_NAME, FAILURE);
    }

    v_dif_mag = (float **)allocate_2d_array(TOTAL_IMAGE_BANDS_SCCD, conse,
                                            sizeof(float));
    if (v_dif_mag == NULL)
    {
        RETURN_ERROR("Allocating v_dif_mag memory",
                     FUNC_NAME, FAILURE);
    }

    v_dif_mag_norm = (float *)malloc(conse * sizeof(float));
    if (v_dif_mag_norm == NULL)
    {
        RETURN_ERROR("Allocating v_dif_mag_norm memory", FUNC_NAME, FAILURE);
    }
    for (k = 0; k < conse; k++)
    {
        v_dif_mag_norm[k] = 0.0;
    }

    medium_v_dif = (float *)malloc(TOTAL_IMAGE_BANDS_SCCD * sizeof(float));
    if (medium_v_dif == NULL)
    {
        RETURN_ERROR("Allocating medium_v_dif memory", FUNC_NAME, FAILURE);
    }

    temp_v_dif = (float **)allocate_2d_array(TOTAL_IMAGE_BANDS, cur_i - i_start + 1,
                                             sizeof(float));
    if (temp_v_dif == NULL)
    {
        RETURN_ERROR("Allocating temp_v_dif memory", FUNC_NAME, FAILURE);
    }

    for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
        rmse_band[i_b] = (float)sum_square_vt[i_b] / (*num_obs_processed - SCCD_NUM_C);

    /* sccd examine i to be break or not so current obs is included in conse windw, while cold is not */
    // we do reverse to facilitate probability calculate
    for (i_conse = 0; i_conse < conse; i_conse++)
    {
        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
        {
            KF_ts_predict_conse(&instance[i_b], clrx, cov_p[i_b], fit_cft, cur_i + i_conse, cur_i + i_conse,
                                i_b, cur_i, &pred_y, &pred_y_f, FALSE);
            // max_rmse[i_b] = max(min_rmse[i_b], sqrtf(pred_y_f));
            max_rmse[i_b] = max(min_rmse[i_b], sqrtf(rmse_band[i_b]));
            // max_rmse[i_b] = sqrtf(rmse_band[i_b]);
            //            if (cur_i + conse - 1 - i_conse > *n_clr - 1){
            //                printf("############################be careful! \n");
            //            }
            v_dif_mag[i_b][i_conse] = clry[i_b][cur_i + i_conse] - pred_y;
            for (b = 0; b < NUM_LASSO_BANDS; b++)
            {
                if (i_b == lasso_blist_sccd[b])
                {
                    v_dif[b][i_conse] = v_dif_mag[i_b][i_conse] / max_rmse[i_b];
                    v_dif_mag_norm[i_conse] = v_dif_mag_norm[i_conse] + v_dif[b][i_conse] * v_dif[b][i_conse];
                    break;
                }
            }
        }

        if (v_dif_mag_norm[i_conse] < break_mag)
        {
            break_mag = v_dif_mag_norm[i_conse];
        }

        if (output_anomaly == TRUE)
        {
            if ((break_mag < anomaly_tcg) & (i_conse < anomaly_conse))
            {
                change_flag = FALSE;
                break;
            }
        }
        else
        {
            if (break_mag < tcg)
            {
                change_flag = FALSE;
                break;
            }
        }

        /* for fast computing*/
        //        if(b_outputcm == FALSE)
        //        {
        //            if(v_dif_mag_norm[i_conse] < tcg){
        //                change_flag = FALSE;
        //                break;
        //            }
        //        }
        //        else
        //        {
        //            // if(v_dif_mag_norm[i_conse] < T_MIN_CG_SCCD)   // put it back if anomaly is reused
        //            if(v_dif_mag_norm[i_conse] < tcg)   // smaller than minimum threshold, it is impossible to be
        //            {
        //                change_flag = FALSE;
        //                break;
        //            }
        //        }
    }

    if (output_anomaly == TRUE)
    {
        if (i_conse >= anomaly_conse)
        { // meaning that over 3 anomaly pixel
            current_CM_n = (clrx[cur_i] - ORDINAL_DATE_1982_1_1) / AVE_DAYS_IN_A_YEAR;
            if (CM_outputs[current_CM_n] == 0)
            { // meaning that hasn't been assigned with anomaly
                current_anomaly = *num_fc_anomaly;
            }
            else
            {
                current_anomaly = *num_fc_anomaly - 1;
            }

            if (break_mag > CM_outputs[current_CM_n])
            // if ((*num_fc_anomaly == 0) | (clrx[cur_i] - rec_cg_anomaly[*num_fc_anomaly - 1].t_break > AVE_DAYS_IN_A_YEAR))// must has a gap of 1 year with the last anomaly break
            {
                for (conse_last = 1; conse_last <= conse; conse_last++)
                {
                    v_diff_tmp = (float **)allocate_2d_array(NUM_LASSO_BANDS, conse_last, sizeof(float)); // used to calculate angle
                    v_dif_mag_tmp = (float **)allocate_2d_array(TOTAL_IMAGE_BANDS_SCCD, conse_last,
                                                                sizeof(float));
                    for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                    {
                        for (b = 0; b < NUM_LASSO_BANDS; b++)
                        {
                            if (i_b == lasso_blist_sccd[b])
                            {
                                for (j = 0; j < conse_last; j++)
                                    v_diff_tmp[b][j] = v_dif[b][j];
                            }
                        }
                        for (j = 0; j < conse_last; j++)
                            v_dif_mag_tmp[i_b][j] = v_dif_mag[i_b][j];
                    }

                    float min_cm = 999999;
                    float mean_angle_anomaly;
                    // mean_angle = angl_scatter_measure(medium_v_dif, v_diff_tmp, NUM_LASSO_BANDS, conse_last, lasso_blist_sccd);
                    mean_angle_anomaly = MeanAngl_float(v_diff_tmp, NUM_LASSO_BANDS, conse_last) * 100;

                    for (j = 0; j < conse_last; j++)
                        if (v_dif_mag_norm[j] * 100 < min_cm)
                            min_cm = v_dif_mag_norm[j] * 100;

                    if (min_cm > MAX_SHORT)
                        min_cm = MAX_SHORT;
                    if (mean_angle_anomaly > MAX_SHORT)
                        mean_angle_anomaly = MAX_SHORT;
                    rec_cg_anomaly[current_anomaly].cm_angle[conse_last - 1] = (short int)mean_angle_anomaly;
                    rec_cg_anomaly[current_anomaly].norm_cm[conse_last - 1] = (short int)min_cm;
                    for (k = 0; k < DEFAULT_CONSE_SCCD; k++)
                    {
                        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                        {
                            rec_cg_anomaly[current_anomaly].obs[i_b][k] = (short int)clry[i_b][cur_i + k];
                        }
                        rec_cg_anomaly[current_anomaly].obs_date_since1982[k] = (short int)(clrx[cur_i + k] - ORDINAL_LANDSAT4_LAUNCH);
                    }
                    for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                    {
                        for (k = 0; k < SCCD_NUM_C; k++)
                        {
                            /**********************************/
                            /*                                */
                            /* Record fitted coefficients.    */
                            /*                                */
                            /**********************************/
                            rec_cg_anomaly[current_anomaly].coefs[i_b][k] = fit_cft[i_b][k];
                        }
                    } // for(i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)

                    //                    for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++){
                    //                        for (b = 0; b < NUM_LASSO_BANDS; b++)
                    //                        {
                    //                            if (i_b == lasso_blist_sccd[b])
                    //                            {
                    //                                for(j = 0; j < conse_last; j++)
                    //                                    v_diff_tmp[b][j] = v_dif[b][j];
                    //                            }
                    //                        }
                    //                        quick_sort_float(v_dif_mag_tmp[i_b], 0, conse_last - 1);
                    //                        matlab_2d_float_median(v_dif_mag_tmp, i_b, conse_last,
                    //                                               &tmp);
                    //                        rec_cg_anomaly[*num_fc_anomaly].cm_bands[conse_last-1][i_b] = tmp;

                    //                    }
                    rec_cg_anomaly[current_anomaly].t_break = clrx[cur_i];

                    status = free_2d_array((void **)v_diff_tmp);
                    if (status != SUCCESS)
                    {
                        RETURN_ERROR("Freeing memory: v_diff_tmp\n",
                                     FUNC_NAME, FAILURE);
                    }
                    status = free_2d_array((void **)v_dif_mag_tmp);
                    if (status != SUCCESS)
                    {
                        RETURN_ERROR("Freeing memory: v_dif_mag_tmp\n",
                                     FUNC_NAME, FAILURE);
                    }
                } // for (conse_last = 1; conse_last <= conse; conse_last++)

                if (CM_outputs[current_CM_n] == 0)
                { // meaning that hasn't been assigned with anomaly
                    *num_fc_anomaly = *num_fc_anomaly + 1;
                }
                CM_outputs[current_CM_n] = break_mag;
            }
        }
    }

    if (change_flag == TRUE)
    {
        if (break_mag < tcg)
        {
            change_flag = FALSE;
        }
        else
        {
            // mean_angle = angl_scatter_measure(medium_v_dif, v_dif, NUM_LASSO_BANDS, conse, lasso_blist_sccd);
            mean_angle = MeanAngl_float(v_dif, NUM_LASSO_BANDS, conse);

            // prob_MCM = Chi_Square_Distribution(break_mag, NUM_LASSO_BANDS);
            tmp = round(break_mag * 100);
            if (tmp > MAX_SHORT) // MAX_SHORT is upper limit of short 16
                tmp = MAX_SHORT;
            tmp_CM = (short int)(tmp);

            if (mean_angle > NSIGN)
            // if (mean_angle > NSIGN)
            {
                change_flag = FALSE;
            }
        }
    }

    if (change_flag == TRUE)
    {
        tmp = (mean_angle * 100);
        if (tmp > MAX_SHORT)
            tmp = MAX_SHORT;
        *mean_angle_scale100 = tmp;
        tmp = break_mag * 100;
        if (tmp > MAX_SHORT)
            tmp = MAX_SHORT;
        *norm_cm_scale100 = tmp;

        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
        {
            rec_cg[*num_curve].rmse[i_b] = sqrtf((float)rmse_band[i_b]);
        }

        rec_cg[*num_curve].num_obs = *num_obs_processed;
        rec_cg[*num_curve].t_start = t_start;

        if (fitting_coefs == TRUE)
        {
            for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
            {
                status = auto_ts_fit_sccd(clrx, clry, i_b, i_b, i_start, cur_i, SCCD_NUM_C,
                                          fit_cft, &tmp_rmse, temp_v_dif, lambda);
                if (status != SUCCESS)
                {
                    RETURN_ERROR("Calling auto_ts_fit_float for clear persistent pixels\n",
                                 FUNC_NAME, FAILURE);
                }
                rec_cg[*num_curve].rmse[i_b] = tmp_rmse;
            }
        }

        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
        {
            quick_sort_float(v_dif_mag[i_b], 0, conse - 1);
            matlab_2d_float_median(v_dif_mag, i_b, conse,
                                   &tmp);
            rec_cg[*num_curve].magnitude[i_b] = (float)tmp;
            for (k = 0; k < SCCD_NUM_C; k++)
            {
                /**********************************/
                /*                                */
                /* Record fitted coefficients.    */
                /*                                */
                /**********************************/
                rec_cg[*num_curve].coefs[i_b][k] = fit_cft[i_b][k];
            }
        } // for(i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)

        /* record break  */
        rec_cg[*num_curve].t_break = clrx[cur_i];
        *num_curve = *num_curve + 1;
        // *num_obs_processed = *num_obs_processed + 1;

        /**********************************************/
        /*                                            */
        /* Identified and move on for the next        */
        /* functional curve.                          */
        /*                                            */
        /**********************************************/

        RETURN_VALUE = CHANGEDETECTED;
    } // if (TRUE == change_flag)
    else if (v_dif_mag_norm[0] > t_max_cg_sccd) // the current one
    {
        /**********************************************/
        /*                                            */
        /*    only update p,                          */
        /*    but treat cur_i as missing value        */
        /*                                            */
        /**********************************************/
        if (steady == FALSE)
        {
            for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
            {
                KF_ts_filter_falsechange(&instance[i_b], clrx, cov_p[i_b], cur_i);
            }
        }

        /**********************************************/
        /*                                            */
        /*    Remove noise.                           */
        /*                                            */
        /**********************************************/
        for (m = cur_i; m < *n_clr - 1; m++)
        {
            clrx[m] = clrx[m + 1];
            for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                clry[i_b][m] = clry[i_b][m + 1];
        }

        RETURN_VALUE = FALSECHANGE;
    }
    else
    {
        /**********************************************/
        /*                                            */
        /*    need to update both p and fit_cft       */
        /*                                            */
        /**********************************************/
        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
        {
            KF_ts_filter_regular(&instance[i_b], clrx, clry[i_b], cov_p[i_b],
                                 fit_cft, cur_i, i_b, &vt, steady);
            if (b_coefs_records == TRUE)
            {
                coefs_records[*n_coefs_records].clrx = clrx[cur_i];
                for (k = 0; k < SCCD_NUM_C; k++)
                {
                    coefs_records[*n_coefs_records].nrt_coefs[i_b][k] = fit_cft[i_b][k];
                }
                if (i_b == (TOTAL_IMAGE_BANDS_SCCD - 1))
                {
                    *n_coefs_records = *n_coefs_records + 1;
                }
            }
            sum_square_vt[i_b] = sum_square_vt[i_b] + vt * vt;
        }
        *num_obs_processed = *num_obs_processed + 1;

        RETURN_VALUE = REGULAREND;
    }

    /**********************************************/
    /*                                            */
    /* Free allocated memories.                   */
    /*                                            */
    /**********************************************/

    status = free_2d_array((void **)v_dif);
    if (status != SUCCESS)
    {
        RETURN_ERROR("Freeing memory: v_dif\n", FUNC_NAME,
                     FAILURE);
    }

    status = free_2d_array((void **)v_dif_mag);
    if (status != SUCCESS)
    {
        RETURN_ERROR("Freeing memory: v_dif_mag\n", FUNC_NAME,
                     FAILURE);
    }

    status = free_2d_array((void **)temp_v_dif);
    if (status != SUCCESS)
    {
        RETURN_ERROR("Freeing memory: temp_v_dif\n",
                     FUNC_NAME, FAILURE);
    }

    free(v_dif_mag_norm);
    v_dif_mag_norm = NULL;
    free(medium_v_dif);

    return (RETURN_VALUE);
}

/************************************************************************
FUNCTION: step3_processing_end

PURPOSE:
Step 3 of S-CCD: processing the end oftime series.
RETURN VALUE:
Type = int (SUCCESS OR FAILURE)

Programmer: Su Ye
**************************************************************************/

int step3_processing_end(
    ssmodel_constants *instance,
    gsl_matrix **cov_p,
    float **fit_cft,
    int *clrx,
    float **clry,
    int cur_i,
    int *n_clr,
    int *nrt_mode,
    int i_start,
    int prev_i_break,           /* I: the i_break of the last curve*/
    output_nrtmodel *nrt_model, /* I/O: the NRT change records */
    int *num_obs_queue,         /* O: the number of multispectral observations    */
    output_nrtqueue *obs_queue, /* O: multispectral observations in queue    */
    unsigned *sum_square_vt,    /* I/O:  the sum of predicted square of residuals  */
    int num_obs_processed,
    int t_start,
    int conse,
    short int *min_rmse,
    double anomaly_tcg,
    bool change_detected,
    double predictability_tcg,
    double lambda,
    bool fitting_coefs,
    int *num_curve,
    Output_sccd *rec_cg)
{
    int k, k1, k2;
    int i_b, b;
    int status;
    char FUNC_NAME[] = "step3_processingn_end";
    int *bl_ids, *ids;
    int *rm_ids;
    // double rmse_sqrt_tmp;
    float *rmse; /* Root Mean Squared Error array.        */
    double w, w2;
    // double tmp_q;
    float **temp_v_dif;
    int istart_queue;
    int i_conse, j;
    float **v_diff_tmp;
    float **v_dif_mag_tmp;
    float pred_y;
    float pred_y_f;
    float rmse_band[TOTAL_IMAGE_BANDS_SCCD];
    float max_rmse;
    float *v_dif_mag_norm;
    float **v_dif;
    float mean_angle_scale100 = 0;
    float *medium_v_dif;
    clock_t t_time = clock();
    float **v_dif_mag;
    int update_num_c, i;
    float tmp_rmse;
    float tmp;

    // double time_taken;
    t_time = clock();
    int conse_last;
    int valid_conse_last; // valid conse number after excluding the observations included in the model fitting
    int stable_count = 0;

    w = TWO_PI / AVE_DAYS_IN_A_YEAR;
    w2 = 2.0 * w;

    rmse = (float *)malloc(TOTAL_IMAGE_BANDS_SCCD * sizeof(float));
    if (rmse == NULL)
    {
        RETURN_ERROR("Allocating rmse memory", FUNC_NAME, FAILURE);
    }

    rm_ids = (int *)malloc(*n_clr * sizeof(int));
    if (rm_ids == NULL)
    {
        RETURN_ERROR("ERROR allocating rm_ids memory", FUNC_NAME, FAILURE);
    }
    ids = (int *)malloc(*n_clr * sizeof(int));
    if (ids == NULL)
    {
        RETURN_ERROR("ERROR allocating ids memory", FUNC_NAME, FAILURE);
    }

    bl_ids = (int *)malloc(*n_clr * sizeof(int));
    if (bl_ids == NULL)
    {
        RETURN_ERROR("ERROR allocating bl_ids memory", FUNC_NAME, FAILURE);
    }

    v_dif = (float **)allocate_2d_array(NUM_LASSO_BANDS, conse, sizeof(float));
    if (v_dif == NULL)
    {
        RETURN_ERROR("Allocating v_dif memory",
                     FUNC_NAME, FAILURE);
    }

    v_dif_mag_norm = (float *)malloc(conse * sizeof(float));
    if (v_dif_mag_norm == NULL)
    {
        RETURN_ERROR("Allocating v_dif_mag_norm memory", FUNC_NAME, FAILURE);
    }

    v_dif_mag = (float **)allocate_2d_array(TOTAL_IMAGE_BANDS_SCCD, conse,
                                            sizeof(float));
    if (v_dif_mag == NULL)
    {
        RETURN_ERROR("Allocating v_dif_mag memory",
                     FUNC_NAME, FAILURE);
    }

    medium_v_dif = (float *)malloc(TOTAL_IMAGE_BANDS_SCCD * sizeof(float));
    if (medium_v_dif == NULL)
    {
        RETURN_ERROR("Allocating v_dif_mag_norm memory", FUNC_NAME, FAILURE);
    }

    temp_v_dif = (float **)allocate_2d_array(TOTAL_IMAGE_BANDS, cur_i - i_start + 1,
                                             sizeof(float));
    if (temp_v_dif == NULL)
    {
        RETURN_ERROR("Allocating temp_v_dif memory", FUNC_NAME, FAILURE);
    }

    //    time_taken = (clock() - (double)t_time)/CLOCKS_PER_SEC; // calculate the elapsed time
    //    printf("step3 timepoint 1 took %f seconds to execute\n", time_taken);
    //    t_time = clock();
    if (*nrt_mode % 10 == NRT_MONITOR_STANDARD)
    {
        /****************************************************/
        /*   need to save nrt records for monitor mode      */
        /****************************************************/
        // note that covariance and P are forceibly assigned with 0 if the status is not monitor mode
        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
        {
            /*   1. covariance matrix   */
            for (k1 = 0; k1 < DEFAULT_N_STATE; k1++)
            {
                for (k2 = 0; k2 < DEFAULT_N_STATE; k2++)
                {
                    // printf("k1 = %d, k2 = %d,  p = %f \n", k1, k2, gsl_matrix_get(cov_p[i_b], k1, k2));
                    if (*nrt_mode % 10 == NRT_MONITOR_STANDARD)
                        nrt_model->covariance[i_b][k1 * DEFAULT_N_STATE + k2] = (float)gsl_matrix_get(cov_p[i_b], k1, k2);
                    else
                        nrt_model->covariance[i_b][k1 * DEFAULT_N_STATE + k2] = 0;
                }
            }
            /*   2. nrt harmonic coefficients   */
            if (fitting_coefs == TRUE)
            {
                status = auto_ts_fit_sccd(clrx, clry, i_b, i_b, i_start, cur_i, SCCD_NUM_C,
                                          fit_cft, &tmp_rmse, temp_v_dif, lambda);
                if (status != SUCCESS)
                {
                    RETURN_ERROR("Calling auto_ts_fit_scc for clear persistent pixels\n",
                                 FUNC_NAME, FAILURE);
                }
            }
            for (k2 = 0; k2 < SCCD_NUM_C; k2++)
                nrt_model->nrt_coefs[i_b][k2] = fit_cft[i_b][k2];
        }

        /*     3. t_start  !!     */
        nrt_model->t_start_since1982 = (short int)(t_start - ORDINAL_LANDSAT4_LAUNCH);

        /*     4. number of observations !!      */
        nrt_model->num_obs = (short int)(num_obs_processed);

        /*     5. observations in tail       */
        for (k = 0; k < DEFAULT_CONSE_SCCD; k++)
        {
            if (num_obs_processed > 0)
            {
                if (k < conse)
                {
                    for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                    {
                        nrt_model->obs[i_b][k] = (short int)clry[i_b][cur_i + k];
                    }
                    nrt_model->obs_date_since1982[k] = (short int)(clrx[cur_i + k] - ORDINAL_LANDSAT4_LAUNCH);
                }
                else
                {
                    for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                    {
                        nrt_model->obs[i_b][k] = 0;
                    }
                    nrt_model->obs_date_since1982[k] = 0;
                }
            }
            else
            {
                for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                {
                    nrt_model->obs[i_b][k] = 0;
                }
                nrt_model->obs_date_since1982[k] = 0;
            }
        }

        /*     6. square adjust rmse, H, sum       */
        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
        {
            // nrt_model->min_rmse[i_b] = (short int)min_rmse[i_b];
            if (*nrt_mode % 10 == NRT_MONITOR_STANDARD)
                nrt_model->H[i_b] = instance[i_b].H;
            else
                nrt_model->H[i_b] = 0;
            nrt_model->rmse_sum[i_b] = sum_square_vt[i_b];
        }

        //        nrt_model->norm_cm = norm_cm[current_CM_n];
        //        nrt_model->norm_cm_date = norm_cm_date[current_CM_n];

        /**********************************************************/
        /*                                                        */
        /* If no break, find at the end of the time series,       */
        /* define probability of change based on conse.       */
        /*                                                        */
        /**********************************************************/
        update_cft(num_obs_processed, N_TIMES, MIN_NUM_C, MID_NUM_C, MID_NUM_C,
                   SCCD_NUM_C, &update_num_c);
        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
            rmse_band[i_b] = (float)sum_square_vt[i_b] / (num_obs_processed - update_num_c);

        //        time_taken = (clock() - (double)t_time)/CLOCKS_PER_SEC; // calculate the elapsed time
        //        printf("step3 timepoint 2 took %f seconds to execute\n", time_taken);
        //        t_time = clock();

        for (i_conse = 0; i_conse < conse; i_conse++)
        {
            v_dif_mag_norm[i_conse] = 0;
            for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
            {
                KF_ts_predict_conse(&instance[i_b], clrx, cov_p[i_b], fit_cft, *n_clr - 1 - i_conse, *n_clr - 1 - i_conse,
                                    i_b, cur_i, &pred_y, &pred_y_f, FALSE);
                // max_rmse[i_b] = max(min_rmse[i_b], sqrtf(pred_y_f));
                max_rmse = max(min_rmse[i_b], sqrtf(rmse_band[i_b]));
                v_dif_mag[i_b][i_conse] = clry[i_b][*n_clr - 1 - i_conse] - pred_y;
                for (b = 0; b < NUM_LASSO_BANDS; b++)
                {
                    if (i_b == lasso_blist_sccd[b])
                    {
                        v_dif[b][i_conse] = v_dif_mag[i_b][i_conse] / max_rmse;
                        v_dif_mag_norm[i_conse] = v_dif_mag_norm[i_conse] + v_dif[b][i_conse] * v_dif[b][i_conse];
                        break;
                    }
                }
            }
        }

        nrt_model->norm_cm = NA_VALUE;
        nrt_model->cm_angle = NA_VALUE;
        nrt_model->anomaly_conse = 0;

        // num_obs_processed == 0 meaning that the observation number is smaller than 6, no model could be fitted
        if (num_obs_processed > 0)
        {
            /**********************************************************/
            /*                                                        */
            /*      predictability test                               */
            /*                                                        */
            /**********************************************************/
            if (*nrt_mode % 10 == NRT_MONITOR_STANDARD) // for bi status, but not for the change just detected
            {
                valid_conse_last = conse;
            }
            else
            {
                valid_conse_last = *n_clr - num_obs_processed - prev_i_break;
                if (valid_conse_last > conse)
                {
                    valid_conse_last = conse;
                }
            }

            /**********************************************************/
            /*                                                        */
            /*         test predictability                            */
            /*                                                        */
            /**********************************************************/
            if (*nrt_mode / 10 == 1)
            {
                if (valid_conse_last > 1)
                {
                    for (i = 0; i < valid_conse_last; i++)
                    {
                        if (v_dif_mag_norm[i] < predictability_tcg)
                        {
                            stable_count = stable_count + 1;
                        }
                    }

                    // won't tested predictability for nrt_mode == 2. temporal!
                    if (*nrt_mode % 10 == 1)
                    {
                        // if pass the predictability test, change the first digit to zero
                        if ((float)stable_count / valid_conse_last > CORRECT_RATIO_PREDICTABILITY)
                        {
                            *nrt_mode = *nrt_mode - 10;
                        }
                    }
                }
            }

            /**********************************************************/
            /*                                                        */
            /*      Assign norm_cm, cm_angle, conse_last              */
            /*                                                        */
            /**********************************************************/
            for (conse_last = 1; conse_last <= valid_conse_last; conse_last++) // equal to *n_clr - 1 to *n_clr - 1 - conse + 1
            {
                v_diff_tmp = (float **)allocate_2d_array(NUM_LASSO_BANDS, conse_last, sizeof(float));
                v_dif_mag_tmp = (float **)allocate_2d_array(TOTAL_IMAGE_BANDS_SCCD, conse_last,
                                                            sizeof(float));
                for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                {
                    for (b = 0; b < NUM_LASSO_BANDS; b++)
                    {
                        if (i_b == lasso_blist_sccd[b])
                        {
                            for (j = 0; j < conse_last; j++)
                                v_diff_tmp[b][j] = v_dif[b][j];
                        }
                    }
                    for (j = 0; j < conse_last; j++)
                        v_dif_mag_tmp[i_b][j] = v_dif_mag[i_b][j];
                }

                // NOTE THAT USE THE DEFAULT CHANGE THRESHOLD (0.99) TO CALCULATE PROBABILITY
                if (v_dif_mag_norm[conse_last - 1] <= anomaly_tcg)
                // if (v_dif_mag_norm[conse_last - 1] <= DEFAULT_COLD_TCG)
                {
                    /**************************************************/
                    /*                                                */
                    /* The last stable ID.                            */
                    /*                                                */
                    /**************************************************/

                    if (conse_last > 1)
                    {
                        float min_cm = 999999;
                        for (j = 0; j < conse_last - 1; j++)
                            if (v_dif_mag_norm[j] * 100 < min_cm)
                                min_cm = v_dif_mag_norm[j] * 100;

                        if (min_cm > MAX_SHORT)
                            min_cm = MAX_SHORT;
                        // mean_angle = angl_scatter_measure(medium_v_dif, v_diff_tmp, NUM_LASSO_BANDS, conse_last, lasso_blist_sccd);
                        mean_angle_scale100 = MeanAngl_float(v_diff_tmp, NUM_LASSO_BANDS, conse_last - 1) * 100;
                        if (mean_angle_scale100 > MAX_SHORT)
                            mean_angle_scale100 = MAX_SHORT;

                        nrt_model->norm_cm = (short int)(min_cm);
                        //                        for(i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                        //                        {
                        //                            quick_sort_float(v_dif_mag_tmp[i_b], 0, conse_last - 1);
                        //                            matlab_2d_float_median(v_dif_mag_tmp, i_b, conse_last,
                        //                                                   &tmp);
                        //                            nrt_model->cm_bands[i_b] = (short int) (tmp);
                        //                        }
                        nrt_model->anomaly_conse = conse_last - 1; // meaning change happens in the last obs, so conse_last - 1
                        nrt_model->cm_angle = (short int)mean_angle_scale100;
                    }

                    status = free_2d_array((void **)v_diff_tmp);
                    if (status != SUCCESS)
                    {
                        RETURN_ERROR("Freeing memory: v_diff_tmp\n",
                                     FUNC_NAME, FAILURE);
                    }
                    status = free_2d_array((void **)v_dif_mag_tmp);
                    if (status != SUCCESS)
                    {
                        RETURN_ERROR("Freeing memory: v_dif_mag_tmp\n",
                                     FUNC_NAME, FAILURE);
                    }
                    break;
                }
                else
                {
                    if (conse_last == valid_conse_last)
                    { // all observation in the last conse passed T_MIN_CG_SCCD
                        float min_cm = 999999;
                        for (j = 0; j < conse_last; j++)
                            if (v_dif_mag_norm[j] * 100 < min_cm)
                                min_cm = v_dif_mag_norm[j] * 100;
                        if (min_cm > MAX_SHORT)
                            min_cm = MAX_SHORT;
                        mean_angle_scale100 = MeanAngl_float(v_diff_tmp, NUM_LASSO_BANDS, conse_last) * 100;
                        if (mean_angle_scale100 > MAX_SHORT)
                            mean_angle_scale100 = MAX_SHORT;

                        nrt_model->norm_cm = (short int)min_cm;
                        nrt_model->cm_angle = (short int)mean_angle_scale100;
                        //                        for(i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                        //                        {
                        //                            quick_sort_float(v_dif_mag_tmp[i_b], 0, conse_last - 1);
                        //                            matlab_2d_float_median(v_dif_mag_tmp, i_b, conse_last,
                        //                                                   &tmp);
                        //                            nrt_model->cm_bands[i_b] = (short int) (tmp);
                        //                        }
                        nrt_model->anomaly_conse = conse_last; // for new change, at last conse

                        /**********************************************************/
                        /*            check if a new break is detected            */
                        /**********************************************************/
                        if ((nrt_model->anomaly_conse >= conse) && (nrt_model->norm_cm >= anomaly_tcg * 100) && (nrt_model->cm_angle < NSIGN * 100) && (*nrt_mode % 10 == NRT_MONITOR_STANDARD))
                        {
                            for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                            {
                                rec_cg[*num_curve].rmse[i_b] = sqrtf((float)rmse_band[i_b]);
                            }

                            rec_cg[*num_curve].num_obs = num_obs_processed + 1;
                            rec_cg[*num_curve].t_start = t_start;

                            for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                            {
                                quick_sort_float(v_dif_mag[i_b], 0, conse - 1);
                                matlab_2d_float_median(v_dif_mag, i_b, conse,
                                                       &tmp);
                                rec_cg[*num_curve].magnitude[i_b] = (float)tmp;
                                for (k = 0; k < SCCD_NUM_C; k++)
                                {
                                    /**********************************/
                                    /*                                */
                                    /* Record fitted coefficients.    */
                                    /*                                */
                                    /**********************************/
                                    rec_cg[*num_curve].coefs[i_b][k] = fit_cft[i_b][k];
                                }
                            } // for(i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)

                            /* record break  */
                            rec_cg[*num_curve].t_break = clrx[cur_i];
                            *num_curve = *num_curve + 1;
                            prev_i_break = cur_i;
                            i_start = cur_i;

                            *nrt_mode = NRT_MONITOR2QUEUE;
                        }
                    }
                }

                status = free_2d_array((void **)v_diff_tmp);
                if (status != SUCCESS)
                {
                    RETURN_ERROR("Freeing memory: v_diff_tmp\n",
                                 FUNC_NAME, FAILURE);
                }
                status = free_2d_array((void **)v_dif_mag_tmp);
                if (status != SUCCESS)
                {
                    RETURN_ERROR("Freeing memory: v_dif_mag_tmp\n",
                                 FUNC_NAME, FAILURE);
                }
            }
        }
    }

    if ((*nrt_mode % 10 == NRT_QUEUE_STANDARD) | (*nrt_mode % 10 == NRT_MONITOR2QUEUE))
    {
        *num_obs_queue = *n_clr - prev_i_break;
        if (*num_obs_queue > MAX_OBS_QUEUE)
        {
            istart_queue = *n_clr - 1 - MAX_OBS_QUEUE;
            *num_obs_queue = MAX_OBS_QUEUE;
        }
        else
        {
            istart_queue = prev_i_break;
        }
        for (k = 0; k < *num_obs_queue; k++)
        {
            obs_queue[k].clrx_since1982 = (short int)(clrx[istart_queue + k] - ORDINAL_LANDSAT4_LAUNCH);
            for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                obs_queue[k].clry[i_b] = (short int)(clry[i_b][istart_queue + k]);
        }
    }

    status = free_2d_array((void **)temp_v_dif);
    if (status != SUCCESS)
    {
        RETURN_ERROR("Freeing memory: fit_cft\n", FUNC_NAME, FAILURE);
    }
    free(rmse);
    free(rm_ids);
    free(ids);
    free(bl_ids);
    status = free_2d_array((void **)v_dif);
    if (status != SUCCESS)
    {
        RETURN_ERROR("Freeing memory: v_dif\n", FUNC_NAME,
                     FAILURE);
    }
    free(v_dif_mag_norm);
    v_dif_mag_norm = NULL;
    free(medium_v_dif);
    status = free_2d_array((void **)v_dif_mag);
    if (status != SUCCESS)
    {
        RETURN_ERROR("Freeing memory: v_dif_mag\n", FUNC_NAME,
                     FAILURE);
    }

    return SUCCESS;
}

int sccd_standard(
    int *clrx,    /* I: clear pixel curve in X direction (date)             */
    float **clry, /* I: clear pixel curve in Y direction (spectralbands)    */
    int *n_clr,
    double tcg,                 /* I:  threshold of change magnitude   */
    Output_sccd *rec_cg,        /* O: offline change records */
    int *num_fc,                /* O: intialize NUM of Functional Curves    */
    int *nrt_mode,              /* O: 1 - monitor mode; 2 - queue mode    */
    output_nrtmodel *nrt_model, /* O: nrt records    */
    int *num_obs_queue,         /* O: the number of multispectral observations    */
    output_nrtqueue *obs_queue, /* O: multispectral observations in queue    */
    short int *min_rmse,        /* O: adjusted rmse for the pixel    */
    int conse,
    bool output_anomaly,
    Output_sccd_anomaly *rec_cg_anomaly, /* O: historical change records for SCCD results    */
    int *num_fc_anomaly,
    double anomaly_tcg,
    int anomaly_conse,
    double predictability_tcg,
    bool b_coefs_records,
    int *n_coefs_records,
    nrt_coefs_records *coefs_records,
    bool fitting_coefs,
    double lambda)
{
    int i_b;
    int status;
    int k, k1, k2;
    int i = 0;
    char FUNC_NAME[] = "sccd_standard";
    // char msg_str[MAX_STR_LEN];       /* Input data scene name                 */
    float **fit_cft; /* Fitted coefficients 2-D array.        */
                     /* Mimimum RMSE                          */
    float *rmse_ini; /* Root Mean Squared Error array for initialization stages       */
    // int rec_fc;                      /* Record num. of functional curves      */
    int i_span;
    double time_span; /* Span of time in no. of years.         */
    int update_num_c;
    double base_value;

    ssmodel_constants *instance;

    // gsl_vector** state_a;          /* a vector of a for current i,  multiple band */
    gsl_matrix **cov_p; /* a vector p matrix for current i,  for multiple band */
    int prev_i_break = 0;
    float **rec_v_dif;
    int bl_train = 0; // indicate both ccd and kalman filter initialization
    float unadjusted_rmse;
    unsigned int sum_square_vt[TOTAL_IMAGE_BANDS_SCCD] = {0, 0, 0, 0, 0, 0};
    int num_obs_processed = 0; // num of clear observation already being processed for the current segment
    int i_start = 0;
    int i_dense = 0;
    int t_start;
    short int cm_angle_scale100 = 0;
    short int norm_cm_scale100 = NA_VALUE; /* I/O: maximum change magnitudes at every norm_cm_INTERVAL days */
    short int norm_cm_date = NA_VALUE;     /* I/O: dates for maximum change magnitudes at every norm_cm_INTERVAL days */
    int n_cm = (clrx[*n_clr - 1] - ORDINAL_DATE_1982_1_1) / AVE_DAYS_IN_A_YEAR + 1;
    ;
    float *CM_outputs;
    bool change_detected = FALSE; // change_detected is only used to mark change to be detected for online mode

    cov_p = (gsl_matrix **)allocate_2d_array(TOTAL_IMAGE_BANDS_SCCD, 1, sizeof(gsl_matrix));
    if (cov_p == NULL)
    {
        RETURN_ERROR("Allocating cov_p memory", FUNC_NAME, FAILURE);
    }

    /* alloc memory for ssm matrix */
    instance = malloc(TOTAL_IMAGE_BANDS_SCCD * sizeof(ssmodel_constants));
    if (instance == NULL)
    {
        RETURN_ERROR("Allocating instance memory", FUNC_NAME, FAILURE);
    }

    CM_outputs = (float *)malloc(n_cm * sizeof(float));
    if (CM_outputs == NULL)
    {
        RETURN_ERROR("Allocating n_cm memory", FUNC_NAME, FAILURE);
    }

    for (k = 0; k < n_cm; k++)
    {
        CM_outputs[k] = 0;
    }

    /* alloc memory for ssm instance */
    for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
    {
        instance[i_b].Z = gsl_vector_alloc(DEFAULT_N_STATE);
        if (instance[i_b].Z == NULL)
        {
            RETURN_ERROR("Allocating instance[i_b].Z memory", FUNC_NAME, FAILURE);
        }
        instance[i_b].T = gsl_matrix_calloc(DEFAULT_N_STATE, DEFAULT_N_STATE);
        if (instance[i_b].T == NULL)
        {
            RETURN_ERROR("Allocating instance[i_b].T memory", FUNC_NAME, FAILURE);
        }
        instance[i_b].Q = gsl_matrix_calloc(DEFAULT_N_STATE, DEFAULT_N_STATE);
        if (instance[i_b].Q == NULL)
        {
            RETURN_ERROR("Allocating instance[i_b].Q memory", FUNC_NAME, FAILURE);
        }
        cov_p[i_b] = gsl_matrix_calloc(DEFAULT_N_STATE, DEFAULT_N_STATE);
        if (cov_p[i_b] == NULL)
        {
            RETURN_ERROR("Allocating cov_p[i_b] memory", FUNC_NAME, FAILURE);
        }
    }

    fit_cft = (float **)allocate_2d_array(TOTAL_IMAGE_BANDS_SCCD, SCCD_NUM_C, sizeof(float));
    if (fit_cft == NULL)
    {
        RETURN_ERROR("Allocating fit_cft memory", FUNC_NAME, FAILURE);
    }

    rmse_ini = (float *)malloc(TOTAL_IMAGE_BANDS_SCCD * sizeof(float));
    if (rmse_ini == NULL)
    {
        RETURN_ERROR("Allocating rmse_ini memory", FUNC_NAME, FAILURE);
    }

    rec_v_dif = (float **)allocate_2d_array(TOTAL_IMAGE_BANDS_SCCD, *n_clr,
                                            sizeof(float));
    if (rec_v_dif == NULL)
    {
        RETURN_ERROR("Allocating rec_v_dif memory", FUNC_NAME, FAILURE);
    }

    /* if the mode is void, we need copy paramater from existing results */
    if (*nrt_mode % 10 == NRT_MONITOR_STANDARD)
    {
        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
        {
            /*   1. covariance matrix   */
            for (k1 = 0; k1 < DEFAULT_N_STATE; k1++)
            {
                for (k2 = 0; k2 < DEFAULT_N_STATE; k2++)
                {
                    // printf("k1 = %d, k2 = %d,  p = %f \n", k1, k2, gsl_matrix_get(cov_p[i_b], k1, k2));
                    gsl_matrix_set(cov_p[i_b], k1, k2, nrt_model->covariance[i_b][k1 * DEFAULT_N_STATE + k2]);
                }
            }
            /*   2. nrt harmonic coefficients   */
            for (k2 = 0; k2 < SCCD_NUM_C; k2++)
                fit_cft[i_b][k2] = nrt_model->nrt_coefs[i_b][k2];
        }

        /*     3. t_start       */
        t_start = ORDINAL_LANDSAT4_LAUNCH + nrt_model->t_start_since1982;

        /*     4. number of observations       */
        num_obs_processed = nrt_model->num_obs;

        /*     5. adjust rmse, sum       */
        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
        {
            sum_square_vt[i_b] = nrt_model->rmse_sum[i_b];
            /*     6. initialize state-space model coefficients       */
            base_value = (double)fit_cft[i_b][0] + (double)fit_cft[i_b][1] * clrx[0] / SLOPE_SCALE;
            initialize_ssmconstants(DEFAULT_N_STATE, nrt_model->H[i_b], base_value, &instance[i_b]);
        }
    }
    else if ((*nrt_mode % 10 == NRT_QUEUE_STANDARD) | (*nrt_mode % 10 == NRT_MONITOR2QUEUE))
    {
        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
        {
            /*   1. covariance matrix   */
            //            for(k1 = 0; k1 < DEFAULT_N_STATE; k1++)
            //            {
            //                for(k2 = 0; k2 < DEFAULT_N_STATE; k2++){
            //                    // printf("k1 = %d, k2 = %d,  p = %f \n", k1, k2, gsl_matrix_get(cov_p[i_b], k1, k2));
            //                    gsl_matrix_set(cov_p[i_b], k1, k2, 0);
            //                }
            //            }
            /*   2. nrt harmonic coefficients   */
            for (k2 = 0; k2 < SCCD_NUM_C; k2++)
                fit_cft[i_b][k2] = 0;
        }

        /*     3. t_start       */
        t_start = clrx[0];

        // num_obs_processed and sum_square_vt will be updated through the lasso regression procedure after step 2
        /*     4. number of observations       */
        num_obs_processed = 0;

        //        /*     5. adjust rmse, sum       */
        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
        {
            sum_square_vt[i_b] = 0;
            //            /*     6. initialize state-space model coefficients       */
            //            initialize_ssmconstants(DEFAULT_N_STATE, 0, &instance[i_b]);
        }
    }

    if (*nrt_mode % 10 == NRT_MONITOR_STANDARD)
        bl_train = 1;
    else
        bl_train = 0;

    /**************************************************************/
    /*                                                            */
    /* While loop - process til the conse -1 observation remains  */
    /*                                                            */
    /**************************************************************/
    while (i + conse <= *n_clr - 1) // the first conse obs have been investigated in the last run
    {

        if (0 == bl_train)
        {
            /**********************************************************/
            /*                                                        */
            /* span of "i"                                            */
            /*                                                        */
            /**********************************************************/

            i_span = i - i_start + 1;

            /**********************************************************/
            /*                                                        */
            /* span of time (num of years)                            */
            /*                                                        */
            /**********************************************************/
            time_span = (double)(clrx[i] - clrx[i_start]) / NUM_YEARS;

            /***************************************************************/
            /*                                                             */
            /* for the first curve, we need more time points to start with */
            /*                                                             */
            /***************************************************************/
            status = INCOMPLETE;
            if ((i_span >= N_TIMES * MID_NUM_C) && (time_span >= (double)MIN_YEARS))
            {
                /**************************************************************/
                /*                                                            */
                /* step1: initialize a ccd model.                            */
                /*                                                            */
                /**************************************************************/
                status = step1_cold_initialize(conse, min_rmse, n_clr, tcg, &i_dense, num_fc, clrx,
                                               clry, &i, &i_start, rec_cg, N_TIMES * MID_NUM_C,
                                               &prev_i_break, rmse_ini, lambda);
            }

            if (INCOMPLETE == status)
            {
                i++;
            }
            else if (SUCCESS == status)
            {
                /**************************************************************/
                /*                                                            */
                /* step 1 - conti: initialize ssm models .                    */
                /*                                                            */
                /**************************************************************/

                for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                {

                    status = auto_ts_fit_sccd(clrx, clry, i_b, i_b, i_start, i, SCCD_NUM_C,
                                              fit_cft, &rmse_ini[i_b], rec_v_dif, lambda);
                    if (status != SUCCESS)
                    {
                        RETURN_ERROR("Calling auto_ts_fit_sccd during continuous monitoring\n",
                                     FUNC_NAME, FAILURE);
                    }
                }

                for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                {
                    unadjusted_rmse = rmse_ini[i_b] * rmse_ini[i_b];
                    base_value = (double)fit_cft[i_b][0] + (double)fit_cft[i_b][1] * clrx[i_start] / SLOPE_SCALE;
                    initialize_ssmconstants(DEFAULT_N_STATE, unadjusted_rmse, base_value, &instance[i_b]);
                    /**************************************************************/
                    /*                                                            */
                    /*  initialize a and p                                        */
                    /*                                                            */
                    /**************************************************************/
                    step1_ssm_initialize(&instance[i_b], clrx, clry[i_b], i_start, i, fit_cft, cov_p[i_b],
                                         i_b, &sum_square_vt[i_b], *n_clr, b_coefs_records, n_coefs_records, coefs_records);
                }
                num_obs_processed = i - i_start + 1;
                t_start = clrx[i_start];
                /* initialization stage stops, and continious change detection starts */
                i++;
                bl_train = 1;

                // update mode - condition 1
                // *nrt_mode = NRT_MONITOR_STANDARD;   // once the initialization is finished, the predictability is forced to be confirmed
            } /* else if(SUCCESS == status) */
            //            time_taken = (clock() - (double)t_time)/CLOCKS_PER_SEC; // calculate the elapsed time
            //            printf("Initialization took %f seconds to execute\n", time_taken);
            //            t_time = clock();

        } /* if(0 == bl_train) */
        /**************************************************************/
        /*                                                            */
        /*    step 2: kalman-filter change detection                  */
        /*                                                            */
        /**************************************************************/
        else
        {
            status = step2_KF_ChangeDetection(instance, clrx, clry, i, i_start, num_fc, conse, min_rmse, tcg, n_clr, cov_p, fit_cft, rec_cg, sum_square_vt, &num_obs_processed, t_start, output_anomaly, rec_cg_anomaly, num_fc_anomaly, anomaly_tcg, &norm_cm_scale100, &cm_angle_scale100, CM_outputs, T_MAX_CG_SCCD, b_coefs_records, n_coefs_records, coefs_records, fitting_coefs, lambda, anomaly_conse);

            if (status == CHANGEDETECTED)
            {
                /**********************************************/
                /*                                            */
                /* Start from i for the next functional     */
                /* curve.                                     */
                /*                                            */
                /**********************************************/
                i_start = i;
                prev_i_break = i;
                /**********************************************/
                /*                                            */
                /* reset training flags.                      */
                /*                                            */
                /**********************************************/
                bl_train = 0;

                /****************************************************/
                /*   need to save nrt records into nrt_model        */
                /****************************************************/
                for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                {
                    /*   1. covariance matrix   */
                    for (k1 = 0; k1 < DEFAULT_N_STATE; k1++)
                    {
                        for (k2 = 0; k2 < DEFAULT_N_STATE; k2++)
                        {
                            // printf("k1 = %d, k2 = %d,  p = %f \n", k1, k2, gsl_matrix_get(cov_p[i_b], k1, k2));
                            nrt_model->covariance[i_b][k1 * DEFAULT_N_STATE + k2] = (float)gsl_matrix_get(cov_p[i_b], k1, k2);
                        }
                    }
                    /*   2. nrt harmonic coefficients   */
                    for (k2 = 0; k2 < SCCD_NUM_C; k2++)
                        nrt_model->nrt_coefs[i_b][k2] = fit_cft[i_b][k2];
                }

                /*     3. t_start  !!     */
                nrt_model->t_start_since1982 = (short int)(t_start - ORDINAL_LANDSAT4_LAUNCH);

                /*     4. number of observations !!      */
                nrt_model->num_obs = (short int)(num_obs_processed);

                /*     5. observations in tail       */
                for (k = 0; k < DEFAULT_CONSE_SCCD; k++)
                {
                    if (k < conse)
                    {
                        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                        {
                            nrt_model->obs[i_b][k] = (short int)clry[i_b][i + k];
                        }
                        nrt_model->obs_date_since1982[k] = (short int)(clrx[i + k] - ORDINAL_LANDSAT4_LAUNCH);
                    }
                    else
                    {
                        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                        {
                            nrt_model->obs[i_b][k] = 0;
                        }
                        nrt_model->obs_date_since1982[k] = 0;
                    }
                }

                /*     6. square adjust rmse, H, sum       */
                for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                {
                    // nrt_model->min_rmse[i_b] = (short int)min_rmse[i_b];
                    nrt_model->H[i_b] = instance[i_b].H;
                    nrt_model->rmse_sum[i_b] = sum_square_vt[i_b];
                }

                /*     7. square adjust rmse, H, sum       */
                nrt_model->norm_cm = (short int)norm_cm_scale100;
                nrt_model->cm_angle = (short int)cm_angle_scale100;
                nrt_model->anomaly_conse = (unsigned char)conse; // for new change, at last conse
                if (*nrt_mode != NRT_VOID)
                    change_detected = TRUE;
            }
            else if (status == FALSECHANGE)
            {
                // printf("%d\n", clrx[i]);
                *n_clr = *n_clr - 1;
                i--;
            }
            i++;
        }

    } /* n_clr for while (i < n_clr - conse) */

    //    int k1, k2;
    //    for(i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
    //    {
    //         for(k1 = 0; k1 < DEFAULT_N_STATE; k1++)
    //         {
    //             for(k2 = 0; k2 < DEFAULT_N_STATE; k2++){
    //                 printf("k1 = %d, k2 = %d,  p = %f \n", k1, k2, gsl_matrix_get(cov_p[i_b], k1, k2));
    //             }
    //         }
    //    }

    // calculate fit_cft for queue mode; num_obs_processed and sum_square_vt are also updated if the status is queue
    // if (bl_train == 0)
    // {
    //     t_start = clrx[prev_i_break];
    //     if (n_clr - prev_i_break < conse)
    //     {
    //         num_obs_processed = 0;
    //         for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
    //         {
    //             for (k2 = 0; k2 < SCCD_NUM_C; k2++)
    //                 fit_cft[i_b][k2] = NA_VALUE;
    //             sum_square_vt[i_b] = 0;
    //         }
    //     }
    //     //    RETURN_ERROR("The observation in the queue cannot be smaller than conse \n", FUNC_NAME, FAILURE);
    //     else
    //     {
    //         num_obs_processed = n_clr - prev_i_break - conse;
    //         if (num_obs_processed < conse)
    //             num_obs_processed = conse;

    //         update_cft(num_obs_processed, N_TIMES, MIN_NUM_C, MID_NUM_C, MID_NUM_C,
    //                    SCCD_NUM_C, &update_num_c);
    //         for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
    //         {
    //             status = auto_ts_fit_sccd(clrx, clry, i_b, i_b, prev_i_break, prev_i_break + num_obs_processed - 1,
    //                                       update_num_c, fit_cft, &rmse_ini[i_b], rec_v_dif);
    //             if (status != SUCCESS)
    //             {
    //                 RETURN_ERROR("Calling auto_ts_fit_sccd at the end of time series\n",
    //                              FUNC_NAME, FAILURE);
    //             }
    //             sum_square_vt[i_b] = rmse_ini[i_b] * rmse_ini[i_b] * (num_obs_processed - update_num_c);
    //         }
    //     }
    // }

    /**************************************************************/
    /*                                                            */
    /*    change status before entering step 3                    */
    /*                                                            */
    /**************************************************************/
    int new_mode = *nrt_mode;
    if (*nrt_mode == NRT_VOID)
    {
        if (bl_train == 1)
            new_mode = NRT_MONITOR_STANDARD;
        else
            new_mode = NRT_QUEUE_STANDARD + 10;
    }
    else
    {
        if (change_detected == TRUE)
        {
            if (*nrt_mode / 10 == 1)
            { // the change has been detected previously, so predictability is not been confirmed
                new_mode = NRT_QUEUE_STANDARD + 10;
            }
            else
                new_mode = NRT_MONITOR2QUEUE; // NRT_MONITOR2QUEU always has firm predictability
        }
        else
        {
            if (*nrt_mode % 10 == NRT_QUEUE_STANDARD)
            {
                if (bl_train == 1)
                    new_mode = NRT_MONITOR_STANDARD;
            }
            else if (*nrt_mode % 10 == NRT_MONITOR2QUEUE)
            {
                if (clrx[*n_clr - conse] - nrt_model->obs_date_since1982[0] - ORDINAL_LANDSAT4_LAUNCH < STATUS_DELEY_DAYS)
                {
                    prev_i_break = 0;
                }
                else
                {
                    new_mode = NRT_QUEUE_STANDARD + 10;
                }
            }
        }
    }
    *nrt_mode = new_mode;

    status = step3_processing_end(instance, cov_p, fit_cft, clrx, clry, i, n_clr, nrt_mode,
                                  i_start, prev_i_break, nrt_model, num_obs_queue,
                                  obs_queue, sum_square_vt, num_obs_processed, t_start,
                                  conse, min_rmse, anomaly_tcg, change_detected, predictability_tcg, lambda, fitting_coefs, num_fc, rec_cg);

    // update mode - condition 4
    //    if ((*nrt_mode % 10 == NRT_MONITOR_STANDARD) && (bl_train == 0))
    //    {
    //        if (*nrt_mode / 10 == 1)  // the change has been detected previously, so predictability is not been confirmed
    //           *nrt_mode =  NRT_QUEUE_STANDARD + 10;
    //        else
    //            *nrt_mode =  NRT_MONITOR2QUEUE;   // the third mode
    //    }

    for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
    {
        gsl_vector_free(instance[i_b].Z);
        //(&instance[i_b])->Z = NULL;
        // gsl_matrix_free (instance[i_b].H);
        gsl_matrix_free(instance[i_b].T);
        //(&instance[i_b])->T = NULL;
        gsl_matrix_free(instance[i_b].Q);
        gsl_matrix_free(cov_p[i_b]);
    }
    status = free_2d_array((void **)cov_p);
    if (status != SUCCESS)
    {
        RETURN_ERROR("Freeing memory: cov_p\n", FUNC_NAME, FAILURE);
    }

    status = free_2d_array((void **)fit_cft);
    if (status != SUCCESS)
    {
        RETURN_ERROR("Freeing memory: fit_cft\n", FUNC_NAME, FAILURE);
    }

    // printf("free stage 4 \n");
    free(rmse_ini);
    rmse_ini = NULL;

    free(instance);
    instance = NULL;

    status = free_2d_array((void **)rec_v_dif);
    if (status != SUCCESS)
    {
        RETURN_ERROR("Freeing memory: rec_v_dif\n",
                     FUNC_NAME, FAILURE);
    }
    free(CM_outputs);

    return SUCCESS;
}

int sccd_snow(
    int *clrx,    /* I: clear pixel curve in X direction (date)             */
    float **clry, /* I: clear pixel curve in Y direction (spectralbands)    */
    int n_clr,
    int *nrt_status,            /* O: 1 - monitor mode; 2 - queue mode    */
    output_nrtmodel *nrt_model, /* O: nrt records    */
    int *num_obs_queue,         /* O: the number of multispectral observations    */
    output_nrtqueue *obs_queue, /* O: multispectral observations in queue    */
    bool b_coefs_records,
    int *n_coefs_records,
    nrt_coefs_records *coefs_records,
    double lambda)
{
    int k;
    int i_start = 0;    /* the first observation for TSFit */
    float **temp_v_dif; /* for the thermal band.......           */
    char FUNC_NAME[] = "snow_procedure";
    int i_b, k1, k2;
    int status;
    float *rmse;
    float **fit_cft; /* Fitted coefficients 2-D array.        */
    ssmodel_constants *instance;
    unsigned sum_square_vt[TOTAL_IMAGE_BANDS_SCCD] = {0, 0, 0, 0, 0, 0};
    int i;
    double vt;
    double base_value;

    gsl_vector **state_a; /* a vector of a for current i,  multiple band */
    gsl_matrix **cov_p;

    temp_v_dif = (float **)allocate_2d_array(TOTAL_IMAGE_BANDS_SCCD, n_clr,
                                             sizeof(float));
    if (temp_v_dif == NULL)
    {
        RETURN_ERROR("Allocating temp_v_dif memory", FUNC_NAME, FAILURE);
    }

    rmse = (float *)malloc(TOTAL_IMAGE_BANDS_SCCD * sizeof(float));
    if (rmse == NULL)
    {
        RETURN_ERROR("Allocating rmse memory", FUNC_NAME, FAILURE);
    }

    state_a = (gsl_vector **)allocate_2d_array(TOTAL_IMAGE_BANDS_SCCD, 1, sizeof(gsl_vector));
    if (state_a == NULL)
    {
        RETURN_ERROR("Allocating state_a memory", FUNC_NAME, FAILURE);
    }

    cov_p = (gsl_matrix **)allocate_2d_array(TOTAL_IMAGE_BANDS_SCCD, 1, sizeof(gsl_matrix));
    if (cov_p == NULL)
    {
        RETURN_ERROR("Allocating cov_p memory", FUNC_NAME, FAILURE);
    }

    /* alloc memory for ssm matrix */
    instance = malloc(TOTAL_IMAGE_BANDS_SCCD * sizeof(ssmodel_constants));
    if (instance == NULL)
    {
        RETURN_ERROR("Allocating instance memory", FUNC_NAME, FAILURE);
    }

    for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
    {
        instance[i_b].Z = gsl_vector_alloc(DEFAULT_N_STATE);
        if (instance[i_b].Z == NULL)
        {
            RETURN_ERROR("Allocating instance[i_b].Z memory", FUNC_NAME, FAILURE);
        }
        instance[i_b].T = gsl_matrix_calloc(DEFAULT_N_STATE, DEFAULT_N_STATE);
        if (instance[i_b].T == NULL)
        {
            RETURN_ERROR("Allocating instance[i_b].T memory", FUNC_NAME, FAILURE);
        }
        instance[i_b].Q = gsl_matrix_calloc(DEFAULT_N_STATE, DEFAULT_N_STATE);
        if (instance[i_b].Q == NULL)
        {
            RETURN_ERROR("Allocating instance[i_b].Q memory", FUNC_NAME, FAILURE);
        }
        state_a[i_b] = gsl_vector_alloc(DEFAULT_N_STATE);
        cov_p[i_b] = gsl_matrix_calloc(DEFAULT_N_STATE, DEFAULT_N_STATE);
    }

    fit_cft = (float **)allocate_2d_array(TOTAL_IMAGE_BANDS_SCCD, SCCD_NUM_C, sizeof(float));
    if (fit_cft == NULL)
    {
        RETURN_ERROR("Allocating fit_cft memory", FUNC_NAME, FAILURE);
    }

    if ((*nrt_status == NRT_QUEUE_SNOW) | (*nrt_status == NRT_VOID))
    {
        /* if n_clr is not enough, save observations and return queue mode*/
        if (n_clr < N_TIMES * SCCD_NUM_C)
        {
            *nrt_status = NRT_QUEUE_SNOW;
            *num_obs_queue = n_clr;
            for (k = 0; k < n_clr; k++)
            {
                obs_queue[k].clrx_since1982 = clrx[k] - ORDINAL_LANDSAT4_LAUNCH;
                for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
                    obs_queue[k].clry[i_b] = clry[i_b][k];
            }

            status = free_2d_array((void **)temp_v_dif);
            if (status != SUCCESS)
            {
                RETURN_ERROR("Freeing memory: rec_v_dif\n",
                             FUNC_NAME, FAILURE);
            }

            free(rmse);
            rmse = NULL;

            for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
            {
                gsl_vector_free(instance[i_b].Z);
                //(&instance[i_b])->Z = NULL;
                // gsl_matrix_free (instance[i_b].H);
                gsl_matrix_free(instance[i_b].T);
                //(&instance[i_b])->T = NULL;
                gsl_matrix_free(instance[i_b].Q);
                gsl_vector_free(state_a[i_b]);
                gsl_matrix_free(cov_p[i_b]);
            }

            status = free_2d_array((void **)cov_p);
            if (status != SUCCESS)
            {
                RETURN_ERROR("Freeing memory: cov_p\n", FUNC_NAME, FAILURE);
            }
            status = free_2d_array((void **)state_a);
            if (status != SUCCESS)
            {
                RETURN_ERROR("Freeing memory: state_a\n", FUNC_NAME, FAILURE);
            }

            free(instance);
            instance = NULL;

            status = free_2d_array((void **)fit_cft);
            if (status != SUCCESS)
            {
                RETURN_ERROR("Freeing memory: fit_cft\n", FUNC_NAME, FAILURE);
            }

            return SUCCESS;
        }

        /**********************************************************/
        /*                                                        */
        /* Treat saturated and unsaturated pixels differently.    */
        /*                                                        */
        /**********************************************************/

        for (k = 0; k < TOTAL_IMAGE_BANDS_SCCD; k++) //
        {

            status = auto_ts_fit_sccd(clrx, clry, k, k, 0, n_clr - 1, MIN_NUM_C,
                                      fit_cft, &rmse[k], temp_v_dif, lambda);

            if (status != SUCCESS)
                RETURN_ERROR("Calling auto_ts_fit_sccd\n", FUNC_NAME, EXIT_FAILURE);
        }

        /**************************************************************/
        /*                                                            */
        /* step 1 - conti: initialize ssm models .                    */
        /*                                                            */
        /**************************************************************/
        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
        {
            base_value = (double)fit_cft[i_b][0] + (double)fit_cft[i_b][1] * clrx[0] / SLOPE_SCALE;
            initialize_ssmconstants(DEFAULT_N_STATE, rmse[i_b], base_value, &instance[i_b]);
            /**************************************************************/
            /*                                                            */
            /*  initialize a and p                                        */
            /*                                                            */
            /**************************************************************/
            step1_ssm_initialize(&instance[i_b], clrx, clry[i_b], i_start, n_clr - 1,
                                 fit_cft, cov_p[i_b], i_b, &sum_square_vt[i_b], n_clr,
                                 b_coefs_records, n_coefs_records, coefs_records);
            nrt_model[0].H[i_b] = instance[i_b].H;
        }

        nrt_model[0].t_start_since1982 = (short int)(clrx[0] - ORDINAL_LANDSAT4_LAUNCH);
        nrt_model[0].num_obs = n_clr;

        *nrt_status = NRT_MONITOR_SNOW;
    }
    else // monitor mode
    {
        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
        {
            /*   1. covariance matrix   */
            for (k1 = 0; k1 < DEFAULT_N_STATE; k1++)
            {
                for (k2 = 0; k2 < DEFAULT_N_STATE; k2++)
                {
                    // printf("k1 = %d, k2 = %d,  p = %f \n", k1, k2, gsl_matrix_get(cov_p[i_b], k1, k2));
                    gsl_matrix_set(cov_p[i_b], k1, k2, nrt_model[0].covariance[i_b][k1 * DEFAULT_N_STATE + k2]);
                }
            }
            /*   2. nrt harmonic coefficients   */
            for (k2 = 0; k2 < SCCD_NUM_C; k2++)
                fit_cft[i_b][k2] = nrt_model[0].nrt_coefs[i_b][k2];
        }

        /*     5. adjust rmse, sum       */
        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
        {
            sum_square_vt[i_b] = nrt_model[0].rmse_sum[i_b];
            /*     6. initialize state-space model coefficients       */
            base_value = (double)fit_cft[i_b][0] + (double)fit_cft[i_b][1] * clrx[0] / SLOPE_SCALE;
            initialize_ssmconstants(DEFAULT_N_STATE, nrt_model[0].H[i_b], base_value, &instance[i_b]);
        }

        nrt_model[0].num_obs = nrt_model[0].num_obs + n_clr - DEFAULT_CONSE_SCCD;

        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
        {
            for (i = 0; i < n_clr - DEFAULT_CONSE_SCCD; i++)
            {
                KF_ts_filter_regular(&instance[i_b], clrx, clry[i_b], cov_p[i_b], fit_cft, i, i_b, &vt, FALSE);
                sum_square_vt[i_b] = sum_square_vt[i_b] + (unsigned int)(vt * vt);
                if (b_coefs_records == TRUE)
                {
                    coefs_records[*n_coefs_records].clrx = clrx[i];
                    for (k = 0; k < SCCD_NUM_C; k++)
                    {
                        coefs_records[*n_coefs_records].nrt_coefs[i_b][k] = fit_cft[i_b][k];
                    }
                    if (i_b == (TOTAL_IMAGE_BANDS_SCCD - 1))
                    {
                        *n_coefs_records = *n_coefs_records + 1;
                    }
                }
            }
        }
    }

    for (k = 0; k < DEFAULT_CONSE_SCCD; k++)
    {
        for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
        {
            nrt_model[0].obs[i_b][k] = (short int)clry[i_b][n_clr - DEFAULT_CONSE_SCCD + k];
        }
        nrt_model[0].obs_date_since1982[k] = (short int)(clrx[n_clr - DEFAULT_CONSE_SCCD + k] - ORDINAL_LANDSAT4_LAUNCH);
    }

    for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
    {
        nrt_model->rmse_sum[i_b] = sum_square_vt[i_b];
    }

    for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
    {
        for (k1 = 0; k1 < DEFAULT_N_STATE; k1++)
        {
            for (k2 = 0; k2 < DEFAULT_N_STATE; k2++)
            {
                nrt_model[0].covariance[i_b][k1 * DEFAULT_N_STATE + k2] = (float)(gsl_matrix_get(cov_p[i_b], k1, k2));
            }
            nrt_model[0].nrt_coefs[i_b][k1] = fit_cft[i_b][k1];
        }
        // nrt_model[0].rmse_sum[i_b] =
    }

    nrt_model[0].norm_cm = NA_VALUE;
    nrt_model[0].cm_angle = NA_VALUE;
    nrt_model[0].anomaly_conse = 0;

    /* monitor mode */
    *nrt_status = NRT_MONITOR_SNOW;

    status = free_2d_array((void **)temp_v_dif);
    if (status != SUCCESS)
    {
        RETURN_ERROR("Freeing memory: rec_v_dif\n",
                     FUNC_NAME, FAILURE);
    }

    free(rmse);
    rmse = NULL;

    for (i_b = 0; i_b < TOTAL_IMAGE_BANDS_SCCD; i_b++)
    {
        gsl_vector_free(instance[i_b].Z);
        //(&instance[i_b])->Z = NULL;
        // gsl_matrix_free (instance[i_b].H);
        gsl_matrix_free(instance[i_b].T);
        //(&instance[i_b])->T = NULL;
        gsl_matrix_free(instance[i_b].Q);
        gsl_vector_free(state_a[i_b]);
        gsl_matrix_free(cov_p[i_b]);
    }

    status = free_2d_array((void **)cov_p);
    if (status != SUCCESS)
    {
        RETURN_ERROR("Freeing memory: cov_p\n", FUNC_NAME, FAILURE);
    }
    status = free_2d_array((void **)state_a);
    if (status != SUCCESS)
    {
        RETURN_ERROR("Freeing memory: state_a\n", FUNC_NAME, FAILURE);
    }

    free(instance);
    instance = NULL;

    status = free_2d_array((void **)fit_cft);
    if (status != SUCCESS)
    {
        RETURN_ERROR("Freeing memory: fit_cft\n", FUNC_NAME, FAILURE);
    }

    return SUCCESS;
}
