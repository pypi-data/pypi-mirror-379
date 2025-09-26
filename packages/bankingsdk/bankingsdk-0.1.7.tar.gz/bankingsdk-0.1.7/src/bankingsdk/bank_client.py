import httpx
from typing import Optional, List, Literal, Union
from .schemas import DemandeSimple, DemandeDetailed, AgenceSimple, SituationProSimple, SituationFamilialeSimple, ApportSimple, AnalyticsResponse
from .bank_config import BankConfig

import pandas as pd


class DemandeClient:
    def __init__(self, config: Optional[BankConfig] = None):
        self.config = config or BankConfig()
        self.bank_base_url = self.config.bank_base_url

    def _format_output(self, data, model, output_format: Literal["pydantic", "dict", "pandas"]):
        if output_format == "pydantic":
            return [model(**item) for item in data]
        elif output_format == "dict":
            return data
        elif output_format == "pandas":
            import pandas as pd
            return pd.DataFrame(data)
        else:
            raise ValueError("Invalid output_format. Choose from 'pydantic', 'dict', or 'pandas'.")    

    def health_check(self) -> dict:
        url = f"{self.bank_base_url}/"
        response = httpx.get(url)
        response.raise_for_status()
        return response.json()
    
    def get_demande(self, demande_id: int) -> DemandeDetailed:
        url = f"{self.bank_base_url}/demandes/{demande_id}"
        response = httpx.get(url)
        response.raise_for_status()
        return DemandeDetailed(**response.json())

    # --- Demandes ---
    def list_demandes(
        self,
        skip: int = 0,
        limit: int = 100,
        montant_operation: Optional[int] = None,
        duree: Optional[int] = None,
        numero_client: int = None,
        accord: Optional[str] = None,
        numero_agence: Optional[int] = None,
        duree_de_traitement: Optional[int] = None,
        code_accord: Optional[int] = None,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[DemandeSimple], List[dict], "pd.DataFrame"]:
        url = f"{self.bank_base_url}/demandes"
        params = {"skip": skip, "limit": limit}
        if montant_operation:
            params["montant"] = montant_operation
        if duree:
            params["duree"] = duree
        if numero_client:
            params["client"] = numero_client
        if accord:
            params["accord"] = accord
        if numero_agence:
            params["agence"] = numero_agence
        if duree_de_traitement:
            params["traitement"] = duree_de_traitement
        if code_accord:
            params["code_accord"] = code_accord

        response = httpx.get(url, params=params)
        response.raise_for_status()
        return self._format_output(response.json(), DemandeSimple, output_format)

     
    ## Agences ##
    def get_agence(self, agence_id: int) -> AgenceSimple:
        url = f"{self.bank_base_url}/agences/{agence_id}"
        response = httpx.get(url)
        response.raise_for_status()
        return AgenceSimple(**response.json())
    
    def list_agences(
        self,
        skip: int = 0,
        limit: int = 100,
        numero_agence: Optional[int] = None,
        ville: Optional[str] = None,
        adresse: Optional[str] = None,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[AgenceSimple], List[dict], "pd.DataFrame"]:
        url = f"{self.bank_base_url}/agences"
        params = {"skip": skip, "limit": limit}
        if numero_agence:
            params["agences"] = numero_agence
        if ville:
            params["ville"] = ville
        if adresse:
            params["adresse"] = adresse
        
        response = httpx.get(url, params=params)
        response.raise_for_status()
        return self._format_output(response.json(), AgenceSimple, output_format)
    

    def get_situation_pro(self, client_id: int) -> SituationProSimple:
        url = f"{self.bank_base_url}/situations_pro/{client_id}"
        response = httpx.get(url)
        response.raise_for_status()
        return SituationProSimple(**response.json())
    
    def list_situation_pros(
        self,
        skip: int = 0,
        limit: int = 100,
        numero_client: Optional[int] = None,
        revenu_mensuel_moyen: Optional[int] = None,
        code_regularite_revenus: Optional[int] = None,
        regularite_des_revenus: Optional[str] = None,
        code_statut_emploi: Optional[int] = None,
        regularite_emploi: Optional[str] = None,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[AgenceSimple], List[dict], "pd.DataFrame"]:
        url = f"{self.bank_base_url}/situations_pro"
        params = {"skip": skip, "limit": limit}
        if numero_client:
            params["clients"] = numero_client
        if revenu_mensuel_moyen:
            params["revenus_moyen"] = revenu_mensuel_moyen
        if code_regularite_revenus:
            params["code_regularite_revenus"] = code_regularite_revenus
        if regularite_des_revenus:
            params["revenus"] = regularite_des_revenus
        if code_statut_emploi:
            params["code_statut_emploi"] = code_statut_emploi        
        if regularite_emploi:
            params["emploi"] = regularite_emploi
        
        response = httpx.get(url, params=params)
        response.raise_for_status()
        return self._format_output(response.json(), SituationProSimple, output_format)
    
    

    
    def get_situation_famille(self, client_id: int) -> SituationFamilialeSimple:
        url = f"{self.bank_base_url}/situations_famille/{client_id}"
        response = httpx.get(url)
        response.raise_for_status()
        return SituationFamilialeSimple(**response.json())
    
    def list_situations_famille(
        self,
        skip: int = 0,
        limit: int = 100,
        numero_client: Optional[int] = None,
        statut_familliale: Optional[str] = None,
        nombre_enfants: Optional[int] = None,
        age: Optional[str] = None,
        nom_client: Optional[str] = None,
        statut_activite: Optional[str] = None,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[SituationFamilialeSimple], List[dict], "pd.DataFrame"]:
        url = f"{self.bank_base_url}/situations_famille"
        params = {"skip": skip, "limit": limit}
        if numero_client:
            params["clients"] = numero_client
        if statut_familliale:
            params["statut_familliale"] = statut_familliale
        if nombre_enfants:
            params["nombre_enfants"] = nombre_enfants
        if nom_client:
            params["code_statut_emploi"] = nom_client  
        if statut_activite:
            params["activité"] = statut_activite
        
        response = httpx.get(url, params=params)
        response.raise_for_status()
        return self._format_output(response.json(), SituationFamilialeSimple, output_format)
    

    
    def get_apport(self, demande_id: int) -> SituationProSimple:
        url = f"{self.bank_base_url}/apports/{demande_id}"
        response = httpx.get(url)
        response.raise_for_status()
        return ApportSimple(**response.json())
    
    def list_apports(
        self,
        skip: int = 0,
        limit: int = 100,
        numero_demande: Optional[int] = None,
        apport: Optional[int] = None,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[SituationFamilialeSimple], List[dict], "pd.DataFrame"]:
        url = f"{self.bank_base_url}/situations_pro"
        params = {"skip": skip, "limit": limit}
        if numero_demande:
            params["demandes"] = numero_demande
        if apport:
            params["apports"] = apport        
        
        response = httpx.get(url, params=params)
        response.raise_for_status()
        return self._format_output(response.json(), ApportSimple, output_format)
    

    def get_analytics(self) -> AnalyticsResponse:
        url = f"{self.movie_base_url}/analytics"
        response = httpx.get(url)
        response.raise_for_status()
        return AnalyticsResponse(**response.json())