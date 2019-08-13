# A Python wrapper for the Clash of Clans API
# Copyright (C) 2019 Gabriel Hearot
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import requests

from typing import Dict
from urllib.parse import quote

_endpoint = 'https://api.clashofclans.com/v1'


def api_response(headers: Dict[str, str], timeout: int,
                 uri: str, params: dict):
    return requests.get(
        _endpoint + uri, params=params,
        headers=headers, timeout=timeout).json()


class Api:
    def __init__(self, token, timeout=20):
        self.token = token
        self.timeout = timeout
        self.headers = {'authorization': 'Bearer %s' % token,
                        'Accept': 'application/json'}

    def clans(self, **kwargs):
        """Search all clans by name and/or filtering
        the results using various criteria.

        At least one filtering criteria must be
        defined and if name is used as part of search,
        it is required to be at least three characters long.

        It is not possible to specify ordering
        for results so clients should not rely
        on any specific ordering as that may
        change in the future releases of the API.
        """
        return api_response(self.headers, self.timeout,
                            '/clans', kwargs)

    def clan_information(self, clan_tag: str, **kwargs):
        """Get information about a single clan by clan tag.

        Clan tags can be found using clan search operation.

        Note that clan tags start with hash character '#' and
        that needs to be URL-encoded properly to work in URL,
        so for example clan tag '#2ABC' would become
        '%232ABC' in the URL.
        """
        return api_response(self.headers, self.timeout,
                            '/clans/%s' % quote(clan_tag), kwargs)

    def clan_members(self, clan_tag: str, **kwargs):
        """List clan members."""
        return api_response(self.headers, self.timeout,
                            '/clans/%s/members' %
                            quote(clan_tag), kwargs)

    def clan_war_log(self, clan_tag: str, **kwargs):
        """Retrieve clan's clan war log."""
        return api_response(self.headers, self.timeout,
                            '/clans/%s/warlog' %
                            quote(clan_tag), kwargs)

    def clan_current_war(self, clan_tag: str, **kwargs):
        """Retrieve information about
        clan's current clan war."""
        return api_response(self.headers, self.timeout,
                            '/clans/%s/currentwar' %
                            quote(clan_tag), kwargs)

    def clan_league_group(self, clan_tag: str, **kwargs):
        """Retrieve information about clan's
        current clan war league group"""
        return api_response(self.headers, self.timeout,
                            '/clans/%s/currentwar/leaguegroup' %
                            quote(clan_tag), kwargs)

    def war_league(self, war_tag: str, **kwargs):
        """Retrieve information about
        individual clan war league war"""
        return api_response(self.headers, self.timeout,
                            '/clanwarleagues/wars/%s' %
                            quote(war_tag), kwargs)

    def player(self, player_tag: str, **kwargs):
        """Get information about a single player
        by player tag.

        Player tags can be found either in game or
        by from clan member lists.

        Note that player tags start with hash character '#'
        and that needs to be URL-encoded properly to work in URL,
        so for example player tag '#2ABC' would become
        '%232ABC' in the URL."""
        return api_response(self.headers, self.timeout,
                            '/players/%s' %
                            quote(player_tag), kwargs)

    def leagues(self, **kwargs):
        """List leagues."""
        return api_response(self.headers, self.timeout,
                            '/leagues', kwargs)

    def league_information(self, league_id: str, **kwargs):
        """Get league information."""
        return api_response(self.headers, self.timeout,
                            '/leagues/%s' % quote(league_id), kwargs)

    def league_seasons(self, league_id: str, **kwargs):
        """Get league seasons.

        Note that league season information
        is available only for Legend League."""
        return api_response(self.headers, self.timeout,
                            '/leagues/%s/seasons' %
                            quote(league_id), kwargs)

    def league_season_rankings(self, league_id: str, season_id: str, **kwargs):
        """Get league season rankings.

        Note that league season information
        is available only for Legend League."""
        return api_response(self.headers, self.timeout,
                            '/leagues/%s/seasons/%s' %
                            (quote(league_id), quote(season_id)), kwargs)

    def locations(self, **kwargs):
        """List locations."""
        return api_response(self.headers, self.timeout,
                            '/locations', kwargs)

    def location_information(self, location_id: str, **kwargs):
        """Get information about specific
        location."""
        return api_response(self.headers, self.timeout,
                            '/locations/%s' %
                            quote(location_id), kwargs)

    def location_clan_rankings(self, location_id: str, **kwargs):
        """Get clan rankings for a
        specific location."""
        return api_response(self.headers, self.timeout,
                            '/locations/%s/rankings/clans' %
                            quote(location_id), kwargs)

    def location_player_rankings(self, location_id: str, **kwargs):
        """Get player rankings for a
        specific location."""
        return api_response(self.headers, self.timeout,
                            '/locations/%s/rankings/players' %
                            quote(location_id), kwargs)

    def location_clan_versus_rankings(self, location_id: str,
                                      **kwargs):
        """Get clan versus rankings for a
        specific location."""
        return api_response(self.headers, self.timeout,
                            '/locations/%s/rankings/clans-versus' %
                            quote(location_id), kwargs)

    def location_player_versus_rankings(self, location_id: str,
                                        **kwargs):
        """Get player versus rankings for
        a specific location."""
        return api_response(self.headers, self.timeout,
                            '/locations/%s/rankings/players-versus' %
                            quote(location_id), kwargs)
